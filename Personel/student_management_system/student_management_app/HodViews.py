

from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect, request
#from django import forms
#from student_management_app.forms import AddStudentForm
from student_management_app.models import CustomUser, Staffs, Courses, Subjects, Students
from django.core.files.storage import FileSystemStorage
from django.contrib import admin, messages
from django.urls import reverse
import datetime

def admin_home(request):
    students=Students.objects.all()
    return render(request,"hod_template/home_content.html",{"students":students})

def add_staff(request):
    return render(request,"hod_template/add_staff.html")

def add_staff_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        address=request.POST.get("address")
        try:
            user=CustomUser.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name,user_type=2)
            user.staffs.address=address
            user.save()
            messages.success(request,"Successfully added staff")
            return HttpResponseRedirect("/add_staff")
        except:    
            messages.error(request,"Faild added staff")
            return HttpResponseRedirect("/add_staff")


def add_course(request):
    return render(request,"hod_template/add_course_template.html")

def add_course_save(request):
    if request.method!="POST":
        return HttpResponseRedirect("Method Not Allowed")
    else :
        course=request.POST.get("course")
        try:
            course_model=Courses(course_name=course)
            course_model.save()
            messages.success(request,"Successfully Added Course")
            return HttpResponseRedirect("/add_course")    
        except:
            messages.error(request,"Failed To Add Course")
            return HttpResponseRedirect("/add_course")      

def add_student(request):
    courses=Courses.objects.all()
    return render(request,"hod_template/add_student_template.html",{"courses":courses})            
def add_student_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        address=request.POST.get("address")
        course_id=request.POST.get("course")
        sex=request.POST.get("sex")

        profile_pic=request.FILES['profile_pic']
        fs=FileSystemStorage()
        filename=fs.save(profile_pic.name,profile_pic)
        profile_pic_url=fs.url(filename)

        try:
            user=CustomUser.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name,user_type=3)
            user.students.address=address
            course_obj=Courses.objects.get(id=course_id)
            user.students.course_id=course_obj

            
            user.students.gender=sex
            user.students.profile_pic=profile_pic_url

            user.save()
            messages.success(request,"Successfully added student")
            return HttpResponseRedirect("/add_student")
        except:    
            messages.error(request,"Faild added student")
            return HttpResponseRedirect("/add_student")

def manage_student(request) :
    students=Students.objects.all()
    return render(request,"hod_template/manage_student_template.html",{"students":students})      

def manage_course(request) :
    courses=Courses.objects.all()
    return render(request,"hod_template/manage_course_template.html",{"courses":courses})              

def edit_student(request,student_id):
    courses=Courses.objects.all()
    student=Students.objects.get(admin=student_id)
    return render(request,"hod_template/edit_student_template.html",{"student":student,"courses":courses,"id":student_id})  

def edit_student_save(request):
    if request.method!="POST":
        return HttpResponse("<h2>method Not Allowed</h2>")
    else:
        student_id=request.POST.get("student_id")
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        username=request.POST.get("username")
        email=request.POST.get("email")
        address=request.POST.get("address")
        course_id=request.POST.get("course")
        sex=request.POST.get("sex")  


        if request.FILES.get('profile_pic',False) :
            profile_pic=request.FILES['profile_pic']
            fs=FileSystemStorage()
            filename=fs.save(profile_pic.name,profile_pic)
            profile_pic_url=fs.url(filename)
        
        else:
            profile_pic_url=None



        try:
            user=CustomUser.objects.get(id=student_id)
            user.first_name=first_name
            user.last_name=last_name
            user.username=username
            user.email=email
            user.save()

            student=Students.objects.get(admin=student_id)
            student.address=address
            student.gender=sex

            course=Courses.objects.get(id=course_id)
            student.course_id=course
            if profile_pic_url!=None:
                student.profile_pic=profile_pic_url

            student.save()
            messages.success(request,"Successfully eddit student")
            return HttpResponseRedirect("/edit_student/"+student_id)
        except:
            messages.success(request,"Failded eddit student")
            return HttpResponseRedirect("/edit_student/"+student_id)






def view_profile(request,student_id):
    courses=Courses.objects.all()
    student=Students.objects.get(admin=student_id)
    return render(request,"hod_template/view_profile.html",{"student":student,"courses":courses})


def edit_student_profile(request,student_id) :
    courses=Courses.objects.all()
    student=Students.objects.get(admin=student_id)
    return render(request,"hod_template/edit_student_template.html",{"student":student,"courses":courses})  

def edit_student_save_profile(request):
    if request.method!="POST":
        return HttpResponse("<h2>method Not Allowed</h2>")
    else:
        student_id=request.POST.get("student_id")
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        username=request.POST.get("username")
        email=request.POST.get("email")
        address=request.POST.get("address")
        session_start=request.POST.get("session_start")
        session_end=request.POST.get("session_end")
        course_id=request.POST.get("course")
        sex=request.POST.get("sex")    


        try:
            user=CustomUser.objects.get(id=student_id)
            user.first_name=first_name
            user.last_name=last_name
            user.username=username
            user.email=email
            user.save()

            student=Students.objects.get(admin=student_id)
            student.address=address
            student.session_start_year=session_start
            student.session_end_year=session_end
            student.gender=sex

            course=Courses.objects.get(id=course_id)
            student.course_id=course

            student.save()
            messages.success(request,"Successfully eddit student")
            return HttpResponseRedirect("/edit_student/"+student_id)
        except:
            messages.success(request,"Failded eddit student")
            return HttpResponseRedirect("/edit_student/"+student_id)

def edit_course(request,course_id):
    course=Courses.objects.get(id=course_id)
    return render(request,"hod_template/edit_course_template.html",{"course":course,"id":course_id})

def edit_course_save(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        course_id=request.POST.get("course_id")
        course_name=request.POST.get("course")

        try:
            course=Courses.objects.get(id=course_id) 
            course.course_name=course_name
            course.save()   
            messages.success(request,"Successfully Edited Course")
            return HttpResponseRedirect("/edit_course/"+course_id)
        except:

            messages.error(request,"Failed to Edit Cousre")
            return HttpResponseRedirect("/edit_course/"+course_id)  




def delete_student(request, student_id):
    student = Students.objects.get(admin=student_id)
    try:
        student.delete()
        messages.success(request, "Student Deleted Successfully.")
        return redirect('manage_student')
    except:
        messages.error(request, "Failed to Delete Student.")
        return redirect('manage_student')


