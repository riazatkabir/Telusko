from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.


def home(request):
     return render (request, "home.html")


def add(request):
     val1 = int(request.POST['num1'])
     val2 = int(request.POST['num2'])
     res = val1 +val2


     return redirect (request, 'result.html', {'result' : res})

