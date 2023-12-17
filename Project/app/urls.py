from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage, name='homepage'),
    path('dashboard', views.DashBoard, name='dashboard'),
]
