<<<<<<< Updated upstream
from django.urls import path

from . import views

urlpatterns = [
path('',views.home, name='home')

=======
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns=[
    path('',views.index, name='index')
>>>>>>> Stashed changes
]