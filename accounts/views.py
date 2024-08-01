from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


def login(request):
    
    if request.method == 'POST':
        input_username = request.POST.get('username')
        input_password = request.POST.get('password')
        
        user = auth.authenticate(username = input_username, password=input_password)
        
        if user is not None:
            auth.login(request, user) # session create ho rha h
            return redirect("todo")
    
        else:
            return redirect("home")
            
    
    return render(request, "accounts/login.html")
# agr m redirect use krunga to likhunga redirect("login")



# =========================== REGISTER FUNCTION =================

def register(request):
    
    if request.method == "POST":
        input_username = request.POST.get("username")
        input_password = request.POST.get("password")
        
        new_user = User(
            username = input_username
        )
        
        new_user.set_password(input_password)
        
        new_user.save()
        
        return redirect("login")
        
    return render(request, "accounts/register.html")



