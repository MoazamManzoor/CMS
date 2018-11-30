from django.urls import path

from . import views

urlpatterns = [
    path('', views.Signupindex, name='SignUp'),
]