from django.urls import path

from unevenshape.views import index, find_shape_centre

urlpatterns = [
    path('', index, name="index"),
    path('dowellunevenshape/', find_shape_centre, name="dowellunevenshape"),
]

