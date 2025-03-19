from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import CustomUser
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

def landing_page(request):
    return render(request, 'securelogin/landingpage.html')

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not CustomUser.objects.filter(username=username).exists():
            messages.error(request, 'Invalid Username')
            return redirect(reverse('login_page'))

        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request, "Invalid Password")
            return redirect(reverse('login_page'))
        else:
            login(request, user)
            return redirect(reverse('home_page'))

    return render(request, 'securelogin/login.html')

def register_page(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = CustomUser.objects.filter(username=username)
        user_email = CustomUser.objects.filter(email=email)

        errors = {}
        
        if user.exists():
            errors['username'] = "Username already exists."
        
        if user_email.exists():
            errors['email'] = "Email already exists."

        if not errors:
            user = CustomUser.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                password=password
            )
            user.save()
            messages.info(request, "Account created successfully")
            return redirect(reverse('register_page'))
        
        for field, error_message in errors.items():
            if 'username' and 'email' in errors:
                messages.error(request, "Email or Username aldready exists.")
                break
            else:
                messages.error(request, error_message)

    return render(request, 'securelogin/register.html')




@login_required(login_url="/securelogin/login/")
def home(request):
    return render(request, "home.html")

@login_required
def logout_page(request):
    logout(request)
    return redirect(reverse('login_page'))
