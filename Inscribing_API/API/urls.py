from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('functionInputs/', views.functionInputs),
    path('processapi/', views.inscribingAPI),
    path('api',views.publicAPI),

]
