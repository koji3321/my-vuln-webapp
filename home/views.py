from django.shortcuts import render
from django.utils.safestring import mark_safe

def home(request):
    return render(request,"home/index.html")

def xss(request):
    try:
        payload=request.GET['q']
    except:
        payload=''
    return render(request,"home/xss.html",{'id':mark_safe(payload)})

def rce(request):
    return render(request,"home/xss.html")

def sqli(request):
    return render(request,"home/xss.html")