from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, "home.html")


def about(request):
    return HttpResponse("<h1> Django E-Commerce Project by Sumit Chawla </h1>")


