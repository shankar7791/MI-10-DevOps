from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from quiz_app.models import login_model
from quiz_app.forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib import auth
from quiz_app.models import *
from .models import CreateUserform
from django.contrib.auth import logout

# Create your views here.
def register(request):
    form =RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("/login/")
        else:
            messages.info("Enter the valid username and password")
            return redirect("/register")

    context ={'form':form}
    return render(request,"quiz_app/register.html",context)

    

def login(request):
    form = login_form()
    if request.method =="POST":
        form =login_form(request.POST)
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = auth.authenticate(username = username , password =password)
        
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"invalid credentials")
            return redirect("/login/")
    return render(request,"quiz_app/login.html",{'form':form})


def home(request):
    
   
    return render(request,"quiz_app/home.html")

def python_view(request):
    if request.method == 'POST':
        
        questions=python.objects.all()
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            if q.ans ==  request.POST.get(q.question):
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100
        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }
        return render(request,'quiz_app/result.html',context)
    else:
        questions=python.objects.all()
        context = {
            'questions':questions
        }
        return render(request,'quiz_app/python.html',context)


def linux_view(request):
    if request.method == 'POST':
        questions=linux.objects.all()
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            if q.ans ==  request.POST.get(q.question):
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100
        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }
        return render(request,'quiz_app/result.html',context)
    else:
        questions=linux.objects.all()
        context = {
            'questions':questions
        }
        return render(request,'quiz_app/linux.html',context)

def git_view(request):
    if request.method == 'POST':
        questions=git.objects.all()
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            if q.ans ==  request.POST.get(q.question):
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100
        context = {
            'score':score,
            'click':request.POST.get(q.question),
            'ans' : q.ans,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }
        return render(request,'quiz_app/result.html',context)
    else:
        questions=git.objects.all()
        context = {
            'questions':questions
        }
        return render(request,'quiz_app/git.html',context)


def addQuestionPython(request):    
    if request.user.is_staff:
        form=pythonform()
        if(request.method=='POST'):
            form=pythonform(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('/')
        context={'form':form}
        return render(request,'quiz_app/AddQuestionpython.html',context)
    else: 
        return redirect('/')
def addQuestionLinux(request):    
    if request.user.is_staff:
        form=linuxform()
        if(request.method=='POST'):
            form=linuxform(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('/')
        context={'form':form}
        return render(request,'quiz_app/AddQuestionlinux.html',context)
    else: 
        return redirect('/')
def addQuestiongit(request):    
    if request.user.is_staff:
        form=gitform()
        if(request.method=='POST'):
            form=gitform(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('/')
        context={'form':form}
        return render(request,'quiz_app/AddQuestiongit.html',context)
    else: 
        return redirect('/')

def logoutpage(request):
    logout(request)
    return redirect('/')



def deleteGit(request,id):
    form=git.objects.get(id=id)
    form.delete()
    return redirect("/")
def deleteLinux(request,id):
    form=linux.objects.get(id=id)
    form.delete()
    return redirect("/")
def deletePython(request,id):
    form=python.objects.get(id=id)
    form.delete()
    return redirect("/")

def gitQuestion_view(request):
    questions=git.objects.all()
    context = {
            'questions':questions
        }
    return render(request,"quiz_app/git_view.html",context)

def pythonQuestion_view(request):
    questions=python.objects.all()
    context = {
            'questions':questions
        }
    return render(request,"quiz_app/python_view.html",context)

def linuxQuestion_view(request):
    questions=linux.objects.all()
    context = {
            'questions':questions
        }
    return render(request,"quiz_app/linux_view.html",context)