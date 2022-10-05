from django.shortcuts import render
from feedApp.models import Stocks ,News
from rest_framework.views import APIView
import json
from django.core.serializers.json import DjangoJSONEncoder

# Create your views here.
class PdnoMain(APIView):
    def get(self, request ,pk):
        pdno = Stocks.objects.get(symbol=pk)
        pdnoNews = News.objects.get(headline__contains=pk)
        pdno.symbol = "img/" + pdno.symbol + ".png"
        return render(request, 'pdnoMain.html', context  = dict(pdno = pdno))