from django.shortcuts import render,redirect
from django.utils.safestring import mark_safe
from subprocess import Popen,PIPE
import re

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
    return render(request,"home/rce.html")

def rcepages(request,id):
    try:
        id=int(id)
    except:
        return redirect("/")
    
    try:
        payload=request.GET['q']
    except:
        payload=''
        return render(request,f"home/rce/{id}.html")

    if payload!="":
        cmd=f"nslookup {payload}"
    else:
        return render(request,f"home/rce/{id}.html")

    match id:
        case 1:
            stdout = Popen(cmd,shell=True,stdout=PIPE).communicate()[0].decode()
            return render(request,"home/rce/1.html",{"rce":stdout})
        case 2:
            if re.search(r"[&;<>$]",payload):
                stdout="insecure activity detected!!"
            else:
                stdout = Popen(cmd,shell=True,stdout=PIPE).communicate()[0].decode()
            return render(request,"home/rce/2.html",{"rce":stdout})
        case 3:
            stdout = Popen(cmd,shell=True,stdout=PIPE).communicate()[0].decode()
            return render(request,"home/rce/3.html",{"rce":"looked up"})
        case 4:
            if not re.search(r"[&;<>$]",payload):
                stdout = Popen(cmd,shell=True,stdout=PIPE).communicate()[0].decode()
            return render(request,"home/rce/3.html",{"rce":"looked up"})
    
    
    return render(request,"home/xss.html")

def sqli(request):
    return render(request,"home/xss.html")