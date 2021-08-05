from django.conf.urls import url
from django.contrib import admin
from django.urls import path,include
from django.views.static import serve
from student_app import views
from django.conf import settings 
from django.conf.urls.static import static


urlpatterns = [
    path("",views.home),
    path("add/",views.add),
    path("details/<id>",views.details),
    path('delete/<id>',views.delete),
    path('update/<id>',views.update),
    path('students/',views.stu_list),
    path('login/',views.login_view),
    path('register/',views.register_view),
   

]

