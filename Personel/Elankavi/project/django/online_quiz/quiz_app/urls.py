from django.contrib import admin
from django.urls import path,include
from quiz_app import views
urlpatterns = [
    path("",views.home),
    path("login/",views.login),
    path('logout/', views.logoutpage),
    path("python/",views.python_view),
    path("linux/",views.linux_view),
    path("git/",views.git_view),
    path("register/",views.register),
    path('AddQuestionPython/', views.addQuestionPython),
    path('AddQuestionLinux/', views.addQuestionLinux),
    path('AddQuestionGit/', views.addQuestiongit),
    path("gitQuestion/",views.gitQuestion_view),
    path("pythonQuestion/",views.pythonQuestion_view),
    path("linuxQuestion/",views.linuxQuestion_view),
   
    path("gitdelete/<id>",views.deleteGit),
    path("linuxdelete/<id>",views.deleteLinux),
    path("pythondelete/<id>",views.deletePython),
]