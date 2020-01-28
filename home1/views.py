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
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request,'login.html')
def signup(request): 
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirmpassword= request.POST['confirmpassword']
        email = request.POST['email']

        if password==confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('signup')
            else:   
                user = User.objects.create_user(username=username, password=password, email=email,first_name="",last_name="")
                user.save()
                print('user created')
                return redirect('login')

        else:
            messages.info(request,'password not matching..')    
            return redirect('signup')
        return redirect('/')
        
    else:
        return render(request,'signup.html')
 
def register(request):
    if request.method == "POST":
        pname = request.POST['pname']
        page = request.POST['age']
        ptype = request.POST['ptype']
        pgender = request.POST['gender']
        gen = 0
        if(pgender=='male'):
            gen=0
        else:
            gen =1
        p = PatientRegstration(patient_name=pname,gender=gen,patient_type=int(ptype), age=page)
        p.save()
        print(pname,page,ptype,pgender)
        pklout =  open("C:\\Users\\abc\\.spyder-py3\\predict queue wait time\\kmeansage.pkl","rb")
        kmeans_from_joblib = joblib.load(pklout)
        y = kmeans_from_joblib.predict([[int(page)]]) 
        pklout =  open("C:\\Users\\abc\\.spyder-py3\\predict queue wait time\\randomforest.pkl","rb")
        knn_from_joblib = joblib.load(pklout)
        ini_array = np.array([[int(ptype), gen, y]])
        str2 = knn_from_joblib.predict(ini_array) 
        
        return render(request,'predict.html',{'f':str2,'y':y})
    else:
        return render(request,'register.html')

# def predict(request):
#     pklout =  open("C:\\Users\\abc\\.spyder-py3\\predict queue wait time\\randomforest.pkl","rb")
#     knn_from_joblib = joblib.load(pklout)
#     ini_array = np.array([[2, 29, 1]])
#     str2 = knn_from_joblib.predict(ini_array) 
#     return render(request,'predict.html',{'f':str2})
