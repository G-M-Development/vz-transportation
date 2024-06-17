
from django.urls import path
from . import views



urlpatterns = [
    path("", views.brokerage, name="brokerage"),
    path("<int:pk>", views.TruckDetailsView.as_view(), name="truck_detail"),
]
