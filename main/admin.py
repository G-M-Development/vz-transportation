from django.contrib import admin
from .models import *


admin.site.register(Main)
class MainAdmin(admin.ModelAdmin):
    list_display = ('main_title',)  # Основні поля для відображення в списку
    search_fields = ('main_title',)  # Пошук за назвою
admin.site.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('name', 'license_number')  # Основні поля для відображення в списку
    search_fields = ('name', 'license_number') 
