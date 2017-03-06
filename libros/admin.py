
from django.contrib import admin

from libros.models import libromodelo

# Register your models here.

class libroadmin(admin.ModelAdmin):
    list_display = ["ISBN","autor","editorial","precio","nombre"]
    search_field = ["nombre","autor","editorial"]
    list_editable = ["nombre","precio"]
    list_filter = ["nombre","precio"]
    
    class Meta:
        model = libromodelo

admin.site.register(libromodelo,libroadmin)



