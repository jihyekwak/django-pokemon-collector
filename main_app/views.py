from django.shortcuts import render
from django.views.generic.base import TemplateView
# from django.views import View
# from django.http import HttpResponse

# class Home(View):
#     def get(self, request):
#         return HttpResponse("Pokemon Collector")

class Home(TemplateView):
    template_name='home.html'
