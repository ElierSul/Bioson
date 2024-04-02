from django.contrib import admin
from api.models import TipoPermiso

@admin.register(TipoPermiso)
class TipoPermisoAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    
