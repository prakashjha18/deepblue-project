from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

def home(request):
    return  render(request,'index.html')
def login(request):
    return render(request,'login.html')
def signup(request):
    return render(request,'signup.html')
