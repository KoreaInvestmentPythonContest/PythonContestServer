from django.shortcuts import render
from feedApp.models import Stocks
from rest_framework.views import APIView

# Create your views here.
class PdnoMain(APIView):
    def get(self, request ,pk):
        pdno = Stocks.objects.get(symbol=pk)
        json.dumps(pdno, cls=DjangoJSONEncoder)
        pdno.update({"symbolurl": "img/" + pdno['symbol'] + ".png"})
        return render(request, 'pdnoMain.html', context  = dict(pdno = pdno))