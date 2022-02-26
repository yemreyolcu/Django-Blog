from django.shortcuts import render,redirect
from .forms import registerForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .forms import loginForm,registerForm
# Create your views here.

def loginn(request):
    form = loginForm(request.POST or None)
    context = {
        "form":form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username,password=password)
        if user is None:
            messages.info(request,"Username or password is incorrect!")
            return render(request,"login.html",context)
        messages.success(request,"Welcome, "+str(request.user.username)+" good to see you!")
        login(request,user)
        return redirect("index")
    return render(request,"user/login.html",context)


def register(request):
    form = registerForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        newUser = User(username=username)
        newUser.set_password(password)
        newUser.save()
        login(request,newUser)
        messages.success(request,"Your account has created!")
        return redirect("index")
    context = {
        "form":form
        }
    return render(request,"user/register.html",context)
def logoutt(request):
    logout(request)
    messages.success(request,"See you later!")
    return redirect("index")