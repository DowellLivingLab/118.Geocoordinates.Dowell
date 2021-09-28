from django.urls import path

from unevenshape.views import find_shape_centre

urlpatterns = [
    # path('', index, name="index"),
    path('', find_shape_centre, name="dowellunevenshape"),
]

