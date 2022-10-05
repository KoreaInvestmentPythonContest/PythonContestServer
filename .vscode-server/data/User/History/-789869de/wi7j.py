from django.shortcuts import render
from feedApp.models import Stocks
from rest_framework.views import APIView

# Create your views here.
class PdnoMain(APIView):
    def get(self, request ,pk):
        pdno = Stocks.objects.get(symbol=pk).values()

        feeds = News.objects.all()[:10].values()
        json.dumps(list(feeds), cls=DjangoJSONEncoder)
        for rc in feeds:
            if rc['extr_stck_cd_list']:
                rc['extr_stck_cd_list'] = list(set(rc['extr_stck_cd_list'].split(',')))
        return render(request, 'pdnoMain.html', context  = dict(pdno = pdno))