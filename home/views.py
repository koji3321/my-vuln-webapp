from django.shortcuts import render,redirect
from django.utils.safestring import mark_safe

def home(request):
    return render(request,"home/index.html")

def xss(request):
    return render(request,"home/xss.html")

def xsspages(request,id):
    try:
        id=int(id)
    except:
        return redirect("/")
    
    try:
        payload=request.GET['q']
    except:
        payload=''


    match (id):
        case (1):
            return render(request,"home/xss/1.html",{"xss":mark_safe(payload)})
        case (2):
            return render(request,"home/xss/2.html",{"xss":mark_safe(payload)})
        case (3):
            return render(request,"home/xss/3.html",{"xss":payload})
        case (4):
            return render(request,"home/xss/4.html",{"xss":mark_safe(payload.replace("<","&lt;").replace(">","&gt;"))})

def rce(request):
    return render(request,"home/xss.html")

def sqli(request):
    return render(request,"home/xss.html")