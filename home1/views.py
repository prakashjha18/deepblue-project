from django.http import HttpResponse
from sklearn.externals import joblib
import numpy as np
import joblib as joblib
import psycopg2
import csv
import codecs
# Create your views here.
from django.contrib import messages
from .models import PatientRegstration
from .models import DoctorInfo
from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect
from six.moves.urllib.parse import urlencode, quote # Python URL functions
import urllib3 # Python URL functions
from bs4 import BeautifulSoup
import requests
import json
<<<<<<< HEAD
import requests
import json
import datetime
from django.core import mail
connection = mail.get_connection()
import http.client

# conn = http.client.HTTPSConnection("api.msg91.com")

# Manually open the connection
# connection.open()

# Construct an email message that uses the connection






URL = 'https://www.sms4india.com/api/v1/sendCampaign'

# get request
def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
  req_params = {
  'apikey':apiKey,
  'secret':secretKey,
  'usetype':useType,
  'phone': phoneNo,
  'message':textMessage,
  'senderid':senderId
  }
  return requests.post(reqUrl, req_params)




=======
http=urllib3.PoolManager()

import requests
import json
>>>>>>> master


def home(request):
    return  render(request,'index.html')
def availDoctrs(request):
    doctrs = DoctorInfo.objects.all()

    #return HttpResponse(dict[0])
    return render(request,'availDoctrs.html',{'doctrs':doctrs})
def login(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("dashboard")
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
def dashboard(request):
    return  render(request,'dashboard.html')
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
                return redirect('/login')

        else:
            messages.info(request,'password not matching..')    
            return redirect('signup')
        return redirect('/')
        
    else:
        doctrs = DoctorInfo.objects.all()
        return render(request,'signup.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
def register(request):
    if request.method == "POST":
        pname = request.POST['pname']
        page = request.POST['page']
        ptype = request.POST['ptype']
        pgender = request.POST['gender']
        pnumber= request.POST['pnumber']
        drid = request.POST['dtype']
        pemail=request.POST['pemail']
        drid = int(drid)
        patients=PatientRegstration.objects.filter(DoctorInfo_id=drid,isinqueue=1)
        sum=0
        for patient in patients:
            sum+=patient.predictedtime
        #return HttpResponse(sum)
        gen = 0
        if(pgender=='male'):
            gen=0
        else:
            gen =1
        drs = DoctorInfo.objects.get(id=drid)
        p = PatientRegstration(patient_name=pname,gender=gen,number=pnumber,patient_type=int(ptype), age=page,isinqueue=1,predictedtime=9,actualtime=9,DoctorInfo=drs,email=pemail)
        p.save()        

        print(pname,page,ptype,pgender)
        #phone=json.dump(pnumber)


        

        # Prepare you post parameters

        # pklout =  open("C:\\Users\\rosha\\.spyder-py3\\predict queue wait time\\kmeansage.pkl","rb")
        # kmeans_from_joblib = joblib.load(pklout)
        # y = kmeans_from_joblib.predict([[int(page)]]) 
        # pklout =  open("C:\\Users\\rosha\\.spyder-py3\\predict queue wait time\\randomforest.pkl","rb")
        # knn_from_joblib = joblib.load(pklout)
        # ini_array = np.array([[int(ptype), gen, y]])
        # str2 = knn_from_joblib.predict(ini_array)
        
<<<<<<< HEAD
        now = datetime.datetime.now()
        pklout =  open("C:\\Users\\rosha\\.spyder-py3\\predict queue wait time\\rfpickle.pkl","rb")
        kmeans_from_joblib = joblib.load(pklout)
        str2 = kmeans_from_joblib.predict([[int(now.hour),  int(now.minute),  int(page),  int(ptype)]])
        y=int(str2)
        txt= 'hello {} TEAM PQT12 predicts Your wait time is {} minutes and total wait time is {} minutes .'.format(pname,y,sum)
# get response
        response = sendPostRequest(URL, 'QDBH8QTNFFN5G0R6EJKB2HYQZYXA8939', 'V92JZT8VYY5TG303', 'stage', pnumber,'SMSIND', txt )  
        print(response.text)
        # # email1 = mail.EmailMessage(
        # #     'This is wait time',
        # #     'Your wait time is {} minutes. This is from variable'.format(str2),
        # #     'freebookisroshan@gmail.com',
        # #     [pemail],
        # #     connection=connection,
        # # )
        # email1.send()
        # payload = '''{
        #     "sender": "SOCKET",
        #     "route": "4",
        #     "country": "91",
        #     "sms": [
        #         {
        #         "message": "hi there",
        #         "to": [
        #             "",
        #             "9702380451"
        #         ]
        #     }

        #     ]
        # }'''
        
        conn = http.client.HTTPSConnection("api.msg91.com")
        payload = {
            "sender" : "SOCKET",
            "route" : "4",
            "country" : "91",
        }
        payload["sms"] = [ {"message" : 'TEAM PQT12 predicts your wait time is {} minutes. This is from variable'.format(y), "to":[pnumber]} ]

        payload = json.dumps(payload)
        headers = {
            'authkey': "318073Af6JfE0UJ5s5e44f34dP1",
            'content-type': "application/json"
            }

        conn.request("POST", "/api/v2/sendsms", payload, headers)

        res = conn.getresponse()
        data = res.read()

        print(data.decode("utf-8"))
        
        return render(request,'predict.html',{'f':str2,'y':y,'sum':sum})
 
=======
        pklout =  open("C:\\Users\\Rajesh\\.spyder-py3\\predict queue wait time\\kmeansage.pkl","rb")
        kmeans_from_joblib = joblib.load(pklout)
        y = kmeans_from_joblib.predict([[int(page)]]) 
        pklout =  open("C:\\Users\\Rajesh\\.spyder-py3\\predict queue wait time\\randomforest.pkl","rb")
        knn_from_joblib = joblib.load(pklout)
        ini_array = np.array([[int(ptype), gen, y]])
        str2 = knn_from_joblib.predict(ini_array)  
        p = PatientRegstration(patient_name=pname,gender=gen,patient_type=int(ptype),age=page,isinqueue=1,predictedtime=int(str2),actualtime=0,DoctorInfo=drs)
        p.save()
        return render(request,'predict.html',{'f':str2,'y':y})
>>>>>>> master
        # return render(request, 'register.html')
    else:
        doctrs = DoctorInfo.objects.all()
        return render(request,'register.html',{'doctrs':doctrs})
<<<<<<< HEAD
def availDoctrs(request):
    doctrs=DoctorInfo.objects.all()
    return render(request,'availDoctrs.html',{'doctrs':doctrs})
def checkdrstatus(request,drid):
    patients=PatientRegstration.objects.filter(DoctorInfo_id=drid,isinqueue=1)
    sum=0
    for patient in patients:
        sum+=patient.predictedtime
    return render(request,'checkstatus.html',{'patients':patients,'sum':sum})
def removefromqueue(request,ptid):
    if request.method=="POST":
        actualtime=request.POST['actualtime']
        patient =PatientRegstration.objects.get(patient_id=ptid)
        patient.actualtime=actualtime
        patient.isinqueue=0
        patient.save()
        # field_names = [patient.patient_type, patient.age, patient.gender, patient.created_at, patient.actualtime, patient.tokenno]
        # with codecs.open("C:/Users/RAJESH/Desktop/dataset(2).csv","a", encoding='utf-8') as logfile:
        #     logger = csv.DictWriter(logfile, fieldnames=field_names)
        #     logger.writeheader()
        doctrs = DoctorInfo.objects.all()
        response = redirect('availDoctrs')
        return response
        doctrs=DoctorInfo.objects.all()
        return render(request,'availDoctrs.html',{'doctrs':doctrs})
    else:
        patient=PatientRegstration.objects.get(patient_id=ptid)
        return render(request,'enteractualtime.html',{'patient':patient})
def history(request):
    current_user=request.user
    times  = PatientRegstration.objects.filter(email=current_user.email)
    return render(request,'history.html',{'current_user':current_user,'times':times})
def realtimestatus(request):
    fileHandle = open ('C:\\Users\\rosha\\person_log.txt',"r" )
=======
    #return HttpResponse(dict[0])
    return render(request,'availDoctrs.html',{'doctrs':doctrs})

def checkdrstatus(request,drid):
    patients = PatientRegstration.objects.filter(DoctorInfo_id = drid,isinqueue=1)
    sum  = 0
    for patient in patients:
        sum+=patient.predictedtime
    return render(request,'checkstatus.html',{'patients':patients,'sum':sum})

def removefromqueue(request,ptid):
    if request.method == "POST":
        actualtime = request.POST['actualtime']
        patient = PatientRegstration.objects.get(patient_id=ptid)
        patient.actualtime = actualtime
        patient.isinqueue = 0
        tokenno=0
        patient.save()
        field_names = [patient.patient_type, patient.age, patient.gender, patient.created_at, patient.actualtime, tokenno]
        with codecs.open("C:/Users/RAJESH/Desktop/dataset(2).csv","a", encoding='utf-8') as logfile:
            logger = csv.DictWriter(logfile, fieldnames=field_names)
            logger.writeheader()
        doctrs = DoctorInfo.objects.all()
        response = redirect('availDoctrs')
        return response
    else:
        patient = PatientRegstration.objects.get(patient_id=ptid)
        return render(request,'enteractualtime.html',{'patient':patient})

def realtimestatus(request):
    fileHandle = open ('C:\\Users\\RAJESH\\person_log.txt',"r" )
>>>>>>> master
    lineList = fileHandle.readlines()
    fileHandle.close()
    l = lineList[-1]
    #return HttpResponse(l)
    return render(request,'realtimestatusreception.html',{'l':l})
<<<<<<< HEAD
def dailyanalysis(request):
    return render(request,'dailyanalysis.html')
    
=======
def history(request):
    current_user=request.user
    times  = PatientRegstration.objects.filter(email=current_user.email)
    return render(request,'history.html',{'current_user':current_user,'times':times})
>>>>>>> master

# def predict(request):
#     pklout =  open("C:\\Users\\abc\\.spyder-py3\\predict queue wait time\\randomforest.pkl","rb")
#     knn_from_joblib = joblib.load(pklout)
#     ini_array = np.array([[2, 29, 1]])
#     str2 = knn_from_joblib.predict(ini_array) 
#     return render(request,'predict.html',{'f':str2})