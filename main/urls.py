
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('form_drivers/', views.form_drivers, name='form_drivers'),
    path('form_operator/', views.form_operator, name='form_operator'),
    path('form_mechanic/', views.form_mechanic, name='form_mechanic'),
]