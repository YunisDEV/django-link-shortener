from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import LoginForm, RegisterForm


def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        logged_user = authenticate(username=username, password=password)
        if logged_user:
            login(request, logged_user)
    else:
        print(form.errors)
    return redirect('index')


def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        if new_user is not None:
            login(request, new_user)
    else:
        print(form.errors)
    return redirect('index')

def logout_view(request):
    logout(request)
    return redirect('index')