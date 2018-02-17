from django.urls import path
from . import views

urlpatterns = [
    path('home/<id_image>', views.home),
]
