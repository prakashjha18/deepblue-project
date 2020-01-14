from django.http import HttpResponse
from sklearn.externals import joblib
import numpy as np
# Create your views here.
from django.contrib import messages
from .models import PatientRegstration
from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect


def home(request):
    return  render(request,'index.html')
def login(request):
    return render(request,'login.html')
def signup(request):
    return render(request,'signup.html')
def register(request):
    if request.method == "POST":
        pname = request.POST['pname']
        page = request.POST['age']
        ptype = request.POST['ptype']
        pgender = request.POST['gender']
        gen = 0
        patient_type = 1
        if(pgender=='male'):
            gen=0
        else:
            gen =1

        p = PatientRegstration(patient_name=pname,gender=gen,patient_type=int(ptype), age=page)
        p.save()
        print(pname,page,ptype,pgender)
        # return HttpResponse("kwehfke")
    else:
        return render(request,'register.html')
    
    #return render(request,'register.html')

def predict(request):
    pklout =  open("C:\\Users\\abc\\.spyder-py3\\predict queue wait time\\randomforest.pkl","rb")
    knn_from_joblib = joblib.load(pklout)
    ini_array = np.array([[2, 29, 1]])
    str2 = knn_from_joblib.predict(ini_array) 
    return render(request,'predict.html',{'f':str2})
