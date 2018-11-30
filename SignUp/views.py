from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def Signupindex(request):
    return HttpResponse("Hello, Sign Up page.")