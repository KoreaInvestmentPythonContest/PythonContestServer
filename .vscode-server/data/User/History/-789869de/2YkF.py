from django.shortcuts import render
from feedApp.models import Stocks
from rest_framework.views import APIView
import json
from django.core.serializers.json import DjangoJSONEncoder

# Create your views here.
class PdnoMain(APIView):
    def get(self, request ,pk):
        pdno = Stocks.objects.all().filter(symbol=pk).values()
        json.dumps(list(pdno), cls=DjangoJSONEncoder)
    
        for rc in pdno:
            rc.update({"symbolurl": "img/" + rc['symbol'] + ".png"})

        return render(request, 'pdnoMtain.html', {"pdno":pdno})