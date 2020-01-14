from django.urls import path

from . import views

urlpatterns = [
path("signup",views.signup,name="signup"),
path("login",views.login, name="login"),
path("register",views.register, name="register"),
path('predicttime',views.predict,name='predictp'),
path('',views.home,name='home')
]