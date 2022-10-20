from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('functionInputs/', views.functionInputs),
    path('api/', views.inscribingAPI),

]