from django.http import HttpResponse
from sklearn.externals import joblib
import numpy as np
# Create your views here.
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect

def home(request):
    return  render(request,'index.html')
def login(request):
    return render(request,'login.html')
def signup(request):
    return render(request,'signup.html')

def predict(request):
    pklout =  open("C:\\Users\\abc\\.spyder-py3\\predict queue wait time\\randomforest.pkl","rb")
    knn_from_joblib = joblib.load(pklout)
    ini_array = np.array([[2, 29, 1]])
    str2 = knn_from_joblib.predict(ini_array) 
    return render(request,'predict.html',{'f':str2})
