from django.shortcuts import render
from django.views import View

class index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/index.html')
    
class About(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/about.html')

class Orden(View):
    def get(self, request, *args, **kwargs):
        pass