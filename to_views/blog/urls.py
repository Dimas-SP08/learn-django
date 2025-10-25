from django.urls import path
from . import views

app_name='blog'
urlpatterns = [

    path('',views.index),
    path('blog/',views.blog),
    path('asd/',views.asd),
    path('dasd',views.dasd),
]
