from django.urls import path

from . import views

urlpatterns = [
path('',views.home, name='home'),
path('predicttime',views.predict,name='predictp')

]