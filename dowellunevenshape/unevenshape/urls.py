from django.urls import path

from normality_a.views import index, dowellnormality

urlpatterns = [
    path('', index, name="index"),
    path('normality/', dowellnormality, name="dowellnormality"),
]

