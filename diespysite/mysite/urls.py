from django.contrib import admin
from django.urls import path,include
from .views import index
from kontak import views as kontakviews

urlpatterns = [
    path('blog/',include('blog.urls')),
    path('kontak/',kontakviews.index),
    path('', index),
    path('admin/', admin.site.urls),
]

