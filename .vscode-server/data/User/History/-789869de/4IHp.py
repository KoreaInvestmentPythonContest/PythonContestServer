from django.shortcuts import render
from feedApp.models import Stocks ,News
from rest_framework.views import APIView
import json
from django.core.serializers.json import DjangoJSONEncoder

# Create your views here.
class PdnoMain(APIView):
    def get(self, request ,pk):
        pdno = Stocks.objects.get(symbol=pk)
        pdnoNews = News.objects.filter(extr_stck_cd_list__contains=pk)
        pdno.symbol = "img/" + pdno.symbol + ".png"
        pdno.newList = pdnoNews
        return render(request, 'pdnoMain.html', context  = dict(pdno = pdno))


class MakeFollow(APIView):
    def get(self, request, symbol):
        makeFollow = Clientfollowstock()
        makeFollow.clientid = request.user.id
        makeFollow.symbol = symbol
        makeheart.save()
        return redirect('/')