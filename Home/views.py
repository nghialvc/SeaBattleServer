from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    return render(request,'home/index.html')

def loginview(request):
    form = LoginForm()
    if request.method == 'POST':
        user = authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            login(request, user)
            return render(request,'home/login.html',{'form':form,'error':'','username':user.username})
        else:
            return render(request,'home/login.html',{'form':form,'error':'Your username or password is incorrect!','username':''})
    return render(request,'home/login.html',{'form':form,'error':'','username':''})

def registerview(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/')
        else:
            return render(request,'home/register.html',{'form':form,'error':'Your username or password is incorrect!'})
    return render(request,'home/register.html',{'form':form,'error':''})

