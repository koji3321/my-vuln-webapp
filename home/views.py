from django.shortcuts import render
from django.http.response import HttpResponse
from urllib import parse

def home(request):
    return render(request,"home/index.html")

def xss(request):
    return render(request,"home/xss.html")

def rce(request):
    return render(request,"home/xss.html")

def sqli(request):
    return render(request,"home/xss.html")