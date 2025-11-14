from django.shortcuts import render


def home(request):
    return render(request, "core/home.html")


def ace(request):
    return render(request, "core/ace.html")
