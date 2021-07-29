import datetime

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from student_mgmt_app.EmailBackEnd import EmailBackEnd
from student_mgmt_app.models import CustomUser, Courses, SessionYearModel


def showDemoPage(request):
    return render(request, "demo.html")


def ShowLoginPage(request):
    return render(request, "login_page.html")


def doLogin(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user = EmailBackEnd.authenticate(request, username=request.POST.get("email"),
                                         password=request.POST.get("password"))
        if user != None:
            login(request, user)
            if user.user_type == "1":
                return HttpResponseRedirect('/admin_home')
            elif user.user_type == "2":
                return HttpResponseRedirect(reverse("staff_home"))
            else:
                return HttpResponseRedirect(reverse("student_home"))
        else:
            messages.error(request, "Invalid Login Details")
            return HttpResponseRedirect("/")


def GetUserDetails(request):
    if request.user != None:
        return HttpResponse("User : " + request.user.email + " usertype : " + str(request.user.user_type))
    else:
        return HttpResponse("Please Login First")


def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")


def signup_admin(request):
    return render(request, "registration/admin_signup.html")


def do_admin_signup(request):
    username = request.POST.get("username")
    email = request.POST.get("email")
    password = request.POST.get("password")

    try:
        user = CustomUser.objects.create_user(username=username, password=password, email=email, user_type=1)
        user.save()
        messages.success(request, "Admin Created Successfully!")
        return HttpResponseRedirect(reverse('show_login'))
    except:
        messages.error(request, "Failed to Create Admin!")
        return HttpResponseRedirect(reverse('show_login'))


def signup_staff(request):
    return render(request, "registration/staff_signup.html")


def do_staff_signup(request):
    username = request.POST.get("username")
    email = request.POST.get("email")
    password = request.POST.get("password")
    address = request.POST.get("address")

    try:
        user = CustomUser.objects.create_user(username=username, password=password, email=email, user_type=2)
        user.staffs.address = address
        user.save()
        messages.success(request, "Staff Created Successfully!")
        return HttpResponseRedirect(reverse('show_login'))
    except:
        messages.error(request, "Failed to Create Staff!")
        return HttpResponseRedirect(reverse('show_login'))


def signup_student(request):
    courses = Courses.objects.all()
    session_years = SessionYearModel.objects.all()
    context = {
        "courses": courses,
        "session_years": session_years
    }
    return render(request, "registration/student_signup.html", context)


def do_student_signup(request):
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    address = request.POST.get('address')
    session_year_id = request.POST.get('sessions')
    course_id = request.POST.get('course')
    gender = request.POST.get('gender')

    # Getting Profile Pic first
    # First Check whether the file is selected or not
    # Upload only if file is selected
    if len(request.FILES) != 0:
        profile_pic = request.FILES['profile_pic']
        fs = FileSystemStorage()
        filename = fs.save(profile_pic.name, profile_pic)
        profile_pic_url = fs.url(filename)
    else:
        profile_pic_url = None

    # try:
    user = CustomUser.objects.create_user(username=username, password=password, email=email,
                                          first_name=first_name, last_name=last_name, user_type=3)
    user.students.address = address

    course_obj = Courses.objects.get(id=course_id)
    user.students.course_id = course_obj

    session_year_obj = SessionYearModel.objects.get(id=session_year_id)
    user.students.session_year_id = session_year_obj

    user.students.gender = gender
    user.students.profile_pic = profile_pic_url
    user.save()
    messages.success(request, "Student Created Successfully!")
    return HttpResponseRedirect(reverse('show_login'))
    # except:
    #     messages.error(request, "Failed to Create Student!")
    #     return HttpResponseRedirect(reverse('show_login'))

