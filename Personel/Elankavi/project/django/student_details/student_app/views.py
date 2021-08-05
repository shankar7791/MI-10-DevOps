from student_app.models import stu_details
from django.shortcuts import redirect, render
from student_app.form import  login_form, register_form, stu_detail_form
from django.contrib import auth
from django.contrib.auth import logout
# Create your views here.
def add(request):
    form=stu_detail_form()
    if request.method=="POST":
        form=stu_detail_form(data=request.POST,files=request.FILES)
        
        if form.is_valid():
            form.save()
            #obj=form.instance
            #return redirect("/students")
            #return render(request,"stu_list.html",{"obj":obj})
            return redirect("/students")
    return render(request,"student_app/add.html",{"form":form})

def stu_list(request):
    student=stu_details.objects.all
    return render(request,"student_app/stu_list.html",{'student':student})

def details(request,id):
    student=stu_details.objects.get(id=id)
    img=stu_details.objects.all()
    return render(request,"student_app/details.html",{'img':img,'student':student})

def update(request,id):
    form=stu_details.objects.get(id=id)
    if request.method== "POST":
        
        stu=stu_detail_form(request.POST ,files=request.FILES, instance=form)
        if stu.is_valid():
            stu.save()
            
            return redirect("/students/")
    return render(request,"student_app/update.html",{'form':form})



def delete(request,id):
    form=stu_details.objects.get(id=id)
    form.delete()
    return redirect("/students/")

def home(request):
  
    return render(request,"student_app/home.html")

def login_view(request):
    form = login_form()
    if request.method == "POST":
        form=login_form(request.POST)
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username = username , password=password)

        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            return redirect("/login/")
    return render(request,"student_app/login.html",{'form':form})


def register_view(request):
    form=register_form()
    if request.POST:
        form=register_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/login/")
        else:
            return redirect ("/register/")
    return render(request,"student_app/register.html",{'form':form})

def logoutpage(request):
    logout(request)
    return redirect("/")
