from django.shortcuts import render,redirect
from django.utils.safestring import mark_safe
from subprocess import Popen,PIPE
import re
from django.db import connection

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
    return render(request,"home/sqli.html")

def sqlipages(request,id):
    try:
        id=int(id)
    except:
        return redirect("/")
    
    match id:
        case 1:
            try:
                username=request.POST.get('username')
                password=request.POST.get('password')
            except:
                username=''
                password=''
                return render(request,f"home/sqli/{id}.html")
            with connection.cursor() as cursor:
                
                cursor.execute(f"select * from home_user where username='{username}' and password='{password}'")
                user=cursor.fetchone()

            if(user):
                return render(request,"home/sqli/1.html",{"logged":f"welcome {user[1]}"})
            else:
                return render(request,"home/sqli/1.html",{"logged":"not logged in"})
            
        case 2:
            try:
                select_id=request.POST["id"]
            except:
                select_id='1'
                return render(request,f"home/sqli/{id}.html")
            
            with connection.cursor() as cursor:
                cursor.execute(f"select * from home_products where id={select_id}")
                product=cursor.fetchall()
            
            if (product):
                return render(request,"home/sqli/2.html",{"product":product})
            else:
                return render(request,"home/sqli/2.html",{"product":"wrong value"})
        case 3:
            try:
                select_id=request.POST["id"]
            except:
                select_id='1'
                return render(request,f"home/sqli/{id}.html")
            with connection.cursor() as cursor:
                cursor.execute(f"select * from home_products where id={select_id}")
                product=cursor.fetchone()

            if (product):
                return render(request,"home/sqli/3.html",{"product":"item in stock"})
            else:
                return render(request,"home/sqli/3.html",{"product":"item not in stock"})
        case 4:
            try:
                select_id=request.POST["id"]
            except:
                select_id='1'
                return render(request,f"home/sqli/{id}.html")
            with connection.cursor() as cursor:
                try:
                    cursor.execute(f"select * from home_products where id={select_id}")
                    product=cursor.fetchone()
                except Exception as e:
                    err=str(e)
                    return render(request,"home/sqli/4.html",{"product":err})


            if (product):
                return render(request,"home/sqli/4.html",{"product":"not an error"})
            else:
                return render(request,"home/sqli/4.html",{"product":err})