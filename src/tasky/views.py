from django.shortcuts import render
from .forms import PostForm

def home(request):
    
    if request.method == "POST":
        form = PostForm(request.POST)
        
        if form.is_valid():
            print("Data:", form.cleaned_data)
            obj = form.save(commit=True)
            
    else:
        form = PostForm()
    
    return render(request, "home.html", { "form": form})

def login(request):
    return render(request, "login.html", {})

def profile(request):
    return render(request, "account/profile.html", {})