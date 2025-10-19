from django.urls import path
from . import views
appp_manage = 'kontak'
urlpatterns = [
    path('',views.index)
]
