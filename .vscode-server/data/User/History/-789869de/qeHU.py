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
        pdno.update({"symbolurl": "img/" + pdno['symbol'] + ".png"})

        return render(request, 'pdnoMtain.html', context=pdno)