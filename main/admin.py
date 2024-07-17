from django.contrib import admin
from .models import *


admin.site.register(Main)
class MainAdmin(admin.ModelAdmin):
    list_display = ('main_title',) 
    search_fields = ('main_title',)  
admin.site.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('name', 'license_number')  
    search_fields = ('name', 'license_number') 
