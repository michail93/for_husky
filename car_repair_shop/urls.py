from django.urls import path
from . import views

app_name="car_repair_shop"

urlpatterns = [
    path('register/', views.register, name="index")
]