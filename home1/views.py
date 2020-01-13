from django.shortcuts import render
from django.http import HttpResponse
from sklearn.externals import joblib
import numpy as np
# Create your views here.

def home(request):
    return  render(request,'index.html')

def predict(request):
    pklout =  open("C:\\Users\\abc\\.spyder-py3\\predict queue wait time\\randomforest.pkl","rb")
    knn_from_joblib = joblib.load(pklout)
    ini_array = np.array([[2, 19, 1]])
    str2 = knn_from_joblib.predict(ini_array) 
    return render(request,'predict.html',{'f':str2})
