from django.shortcuts import render
from student_management_app.models import CustomUser, Staffs, Courses, Subjects, Students
from django.http import HttpResponse, HttpResponseRedirect, request
from django.contrib import admin, messages

def student_home(request):
    user=CustomUser.objects.get(id=request.user.id)
    students=Students.objects.get(admin=user)

    courses=Courses.objects.all()
    #student=Students.objects.get(admin=student_id)

    
    return render(request,"student_template/student_home_template.html",{"student":students,"user":user,"course":courses})








def student_profile(request) :
    user=CustomUser.objects.get(id=request.user.id)
    students=Students.objects.get(admin=user)

    courses=Courses.objects.all()
    
    
    return render(request,"student_template/edit_student_template.html",{"student":students,"user":user,"courses":courses})  

def student_profile_save(request):
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

            student.save()
            messages.success(request,"Successfully eddit student")
            return HttpResponseRedirect("/student_profile")
        except:
            messages.success(request,"Failded eddit student")
            return HttpResponseRedirect("/student_profile")
 