from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse("index.html")
    return render(request,'index.html')
    
def about(request):
    return HttpResponse("<h1>welcome to the about section</h1>")
def suraj(request):
    return HttpResponse("<h1>welcome to the Suraj vishwakarma</h1>")
