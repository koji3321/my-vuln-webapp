from django.urls import path
from . import views

urlpatterns=[
    path('',views.home),
    path('xss',views.xss,name="xss"),
    path('sqli',views.sqli,name="sqli"),
    path('rce',views.rce,name="rce"),
]