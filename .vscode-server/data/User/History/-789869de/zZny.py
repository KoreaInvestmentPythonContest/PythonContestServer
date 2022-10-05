from django.shortcuts import render
from feedApp.models import Stocks
from rest_framework.views import APIView

# Create your views here.
class PdnoMain(APIView):
    def get(self, request ,pk):
        pdno = Stocks.objects.get(symbol=pk)
        return render(request, 'pdnoMain.html', context  = dict(pdno = pdno))