from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def home(request):
    return render(request,'myapp/home.html')

def login_user(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login Successful")
            return redirect('/')
        else:
            messages.error(request, "Invalid Credentials!")
    return render(request,'myapp/login.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username = username).exists():
                messages.error(request, "Username already exists")
            elif User.objects.filter(email = email).exists():
                messages.error(request, "Email already exists")
            else:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password1,
                )
                user.save()
                messages.success(request, "Account created Sucessfully")
                return redirect('/login/')
        else:
            messages.error(request, "Password did not match")
    return render(request,'myapp/register.html')

def logout_user(request):
    logout(request)
    messages.success(request, "Logged out Successfull!")
    return redirect('/login/')

def booked(request):
    return render(request,'myapp/booked.html')

def payment(request):
    return render(request,'myapp/payment.html')

def deleted(request):
    return render(request,'myapp/deleted.html')