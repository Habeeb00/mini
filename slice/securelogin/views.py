from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from securelogin.models import CustomUser
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.


def landing_page(request):
    return render(request,'securelogin/landingpage.html')


def login_page(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        if not CustomUser.objects.filter(username=username).exists():
            messages.error(request,'Invalid Username')
            return redirect(reverse('login_page'))
        
        user=authenticate(username=username,password=password)

        if user is None:
            messages.error(request,"Invalid Password")
            return redirect(reverse('login_page'))
        else:
            login(request,user)
            return redirect(reverse('home_page'))
        
    return render(request,'securelogin/login.html')


def register_page(request):
    if request.method=="POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')

        user=CustomUser.objects.filter(username=username)
        user_email=CustomUser.objects.filter(email=email)

        if user.exists():
            messages.info(request,"Username already exist")
            return redirect(reverse('register_page'))
        
        if user_email.exists():
            messages.info(request,"Email already exist")
            return redirect(reverse('register_page'))

    
        user=CustomUser.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email)

        user.set_password(password)
        user.save()

        messages.info(request,"Account created sucessfully")
        return redirect(reverse('register_page'))
    return render(request, 'securelogin/register.html')



@login_required(login_url="/securelogin/login/")
def home(request):
    return render(request,"home.html")


@login_required
def logout_page(request):
    logout(request)
    return redirect(reverse('login_page'))