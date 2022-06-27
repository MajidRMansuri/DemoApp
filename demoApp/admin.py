from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Role)
# admin.site.register(Master)
admin.site.register(Profile)
admin.site.register(Shop_Types)
admin.site.register(Del_Status)

@admin.register(Master)
class RoleAdmin(admin.ModelAdmin):
    list_display = ['id', 'Email','Password','IsActive']