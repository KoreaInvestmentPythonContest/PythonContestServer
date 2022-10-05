from django.shortcuts import render , redirect
from feedApp.models import Stocks ,News , Clientfollowstock
from rest_framework.views import APIView
import json
from django.core.serializers.json import DjangoJSONEncoder

# Create your views here.
class PdnoMain(APIView):
    def get(self, request ,pk):
        pdno = Stocks.objects.get(symbol=pk)
        pdnoNews = News.objects.filter(extr_stck_cd_list__contains=pk)
        pdno.symbolBack = pdno.symbol
        pdno.symbol = "img/" + pdno.symbol + ".png"
        pdno.newList = pdnoNews
        pdno.followCnt = len(Clientfollowstock.objects.filter(symbol=pk))
        pdno.postCnt = len(pdnoNews)
        try:
            pdno.followyn = Clientfollowstock.objects.get(clientid=request.user.id,symbol=pk)
        except Clientfollowstock.DoesNotExist:
            pdno.followyn = None
        return render(request, 'pdnoMain.html', context  = dict(pdno = pdno))


class MakeFollow(APIView):
    def get(self, request, symbol):
        makeFollow = Clientfollowstock()
        makeFollow.clientid = request.user.id
        makeFollow.symbol = symbol
        makeFollow.save()
        return redirect("/pdno/'{{symbol}}'")