from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    # IMPLEMENT YOUR ROUTES HERE
]
