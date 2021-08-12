from django.shortcuts import render

# Create your views here.

def showDemopage(request):
    return render(request,"demo.html")

def showLoginpage(request):
    return render(request,"login_page.html")

def doLoginpage(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user=EmailBackend=authenticate(request,username=request.POST.get("email"),password=request.POST.get("password"))
        if user!= None:
            login(user)
            return HttpResponse("Email :" +request.POST.get("email")+" Password :" +request.POST.get("password"))
        else:
            return HttpResponse("Invalid Login")
    
def GetUserDetails(request):
    if request.user! = None:
        return HttpResponse(" User :"+request.user.email+" usertype : " +request.user.user_type)
    else:
        return HttpResponse("Please Login First")

def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")