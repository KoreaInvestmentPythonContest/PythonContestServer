from django.shortcuts import render
from rest_framework.views import APIView
from .models import News
import copy
from django.db.models import Expression




# Create your views here.

class NewsFeed(APIView):
    def get(self, request):
        newsLst = News.objects.order_by('-occr_dt')[:30]
        context = dict(newsLst = newsLst)
        
        context['extr_stck_cd_list'] = context['extr_stck_cd_list'].split(',')
        return render(request, 'newsFeed.pdno', context  = context)



class Coalesce(Expression):
    template = 'COALESCE( %(expressions)s )'

    def __init__(self, expressions, output_field):
      super().__init__(output_field=output_field)
      if len(expressions) < 2:
          raise ValueError('expressions must have at least 2 elements')
      for expression in expressions:
          if not hasattr(expression, 'resolve_expression'):
              raise TypeError('%r is not an Expression' % expression)
      self.expressions = expressions