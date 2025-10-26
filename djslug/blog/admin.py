from django.contrib import admin
from .models import Artikel


class artikelAdmin(admin.ModelAdmin):
    readonly_fields = ['slug']
admin.site.register(Artikel,artikelAdmin)

# Register your models here.
