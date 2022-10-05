from django.shortcuts import render, redirect
from rest_framework.views import APIView
from feedApp.models import News , Clientcomment ,Clientheart , Stocks
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import get_object_or_404
from django.utils import timezone
from datetime import datetime

class View(APIView):
    def get(self, request):
        feeds = News.objects.order_by('-occr_dt')[:21].values()
        json.dumps(list(feeds), cls=DjangoJSONEncoder)
        for rc in feeds:
            if rc['extr_stck_cd_list']:
                rc['extr_stck_cd_list'] = list(set(rc['extr_stck_cd_list'].split(',')))
            rc['comments'] =Clientcomment.objects.filter(newseq=rc['seq'])
            rc['heart'] = len(Clientheart.objects.filter(newsseq=rc['seq']))
            try:
                rc['heartYN'] = Clientheart.objects.get(newsseq=rc['seq'],clientid=request.user.id)
            except Clientheart.DoesNotExist:
                rc['heartYN'] = None
        return render(request, 'main_board.html', context  = dict(feedLst = feeds))

    def comments_create(request, pk):
        if request.method == 'POST':
            if request.user.is_authenticated:
                comment = Clientcomment()
                comment.newseq = pk
                comment.username = request.user
                comment.text = request.POST['content']
                comment.save()
            return redirect('/')
            
    def comments_delete(request, user, commentSeq):
        if request.method == 'POST':
            if request.user.is_authenticated:
                if request.user == user:
                    dSeq = Clientcomment.objects.get(seq=commentSeq)
                    dSeq.delete()
            return redirect('/')
    
    def add_heart(request, newseq):
        makeheart = Clientheart()
        makeheart.clientid = request.user.id
        makeheart.newsseq = newseq
        makeheart.save()
        return redirect('/')

    def recPdno(request):
        symbolLst = Stocks.objects.values('symbol').distinct()[:30]
        json.dumps(list(symbolLst), cls=DjangoJSONEncoder)
        for rc in symbolLst:
            rc['img']= "img/" + rc['symbol'] + ".png"
        return render(request, 'recommandPdno.html', context  = dict(symbolLst = symbolLst))