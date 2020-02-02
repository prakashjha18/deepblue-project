from django.urls import path

from . import views

urlpatterns = [
path("signup",views.signup,name="signup"),
path("login",views.login, name="login"),
path("register",views.register, name="register"),
path("logout",views.logout, name="logout"),
path("availDoctrs",views.availDoctrs,name="availDoctrs"),
path("checkstatus/<int:drid>",views.checkdrstatus,name="checkdrstatus"),
path("removefromqueue/patient/<int:ptid>",views.removefromqueue,name="removefromqueue"),
path("dashboard",views.dashboard, name="dashboard"),
path("history",views.history, name="history"),

#path('predicttime',views.predict,name='predictp'),
path("realtimestatus",views.realtimestatus,name="realtimestatus"),
path('',views.home,name='home')
]