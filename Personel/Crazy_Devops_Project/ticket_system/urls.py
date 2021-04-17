from django.urls import path
from . import views

urlpatterns = [
    path('',views.Register),
    path('Register',views.Register,name='Register'),
    path('Login',views.logIn,name='Login'),
    path('Home',views.Home,name='Home'),
    path('About',views.About,name='About'),
    path('Radhe',views.Radhe,name='Radhe'),
    path('KGF',views.kgf,name='KGF'),
    path('Booking',views.Booking,name='Booking'),

]

