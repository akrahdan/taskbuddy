from django.shortcuts import render


def home(request):
    return render(request=request, template_name="home.html")

def login(request):
    return render(request, "login.html", {})

def profile(request):
    return render(request, "account/profile.html", {})