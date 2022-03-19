from django.http import HttpRequest
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

class Home(View):
    def get(self, request):
        return HttpResponse("Pokemon Collector")
