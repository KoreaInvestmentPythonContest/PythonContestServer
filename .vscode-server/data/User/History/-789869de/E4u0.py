from django.shortcuts import render
from feedApp.models import Stocks
from rest_framework.views import APIView
import json
from django.core.serializers.json import DjangoJSONEncoder

# Create your views here.
class PdnoMain(APIView):
    def get(self, request ,pk):
        pdnolst = Stocks.objects.all().filter(symbol=pk).values()
        json.dumps(list(pdnolst), cls=DjangoJSONEncoder)
    
        for rc in pdnolst:
            rc.update({"symbolurl": "img/" + rc['symbol'] + ".png"})

        return render(request, 'pdnoMain.html', context  = dict(pdno = pdnolst))