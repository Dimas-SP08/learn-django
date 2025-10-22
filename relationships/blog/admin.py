from django.contrib import admin
from .models import Article,Publication,Tag,Reader,Readlist


admin.site.register(Article)
admin.site.register(Publication)
admin.site.register(Tag)
admin.site.register(Reader)
admin.site.register(Readlist)
# Register your models here.
