<<<<<<< Updated upstream
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("hello world")
=======
from django.shortcuts import render

# Create your views here.
def home(request):
    return render('index.html')
>>>>>>> Stashed changes
