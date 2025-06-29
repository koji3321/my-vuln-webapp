from django.urls import path
from . import views

urlpatterns=[
    path('',views.home),
    path('xss',views.xss,name="xss"),
    path('xss/',views.xss,name="xss"),
    path('xss/<str:id>',views.xsspages,name="xsspage"),
    path('sqli',views.sqli,name="sqli"),
    path('sqli/',views.sqli,name="sqli"),
    path('sqli/<str:id>',views.sqlipages,name="sqlipages"),
    path('rce',views.rce,name="rce"),
    path('rce/',views.rce,name="rce"),
    path('rce/<str:id>',views.rcepages,name="rce"),
]