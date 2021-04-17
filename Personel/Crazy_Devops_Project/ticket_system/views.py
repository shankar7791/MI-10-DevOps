from django.http import HttpResponse
from django.shortcuts import render
from ticket_system.models import Customer
from ticket_system.models import LogIn


def Register(request):

    if(request.method == 'GET'):
        return render(request,'Register.html')
    else:
        postData = request.POST
        username = postData.get('username')
        Email = postData.get('email')
        Password = postData.get('password')
        print(username)
        print(Email)
        print(Password)
        customer = Customer(Username=username,
                            Email=Email,
                            Password=Password)
        customer.register()
        return render(request,'Register.html') 
    
def logIn(request):
    if(request.method == "GET"):
        return render(request,'Register.html')
    else:
        postData = request.POST
        Username = postData.get('username')
        Password = postData.get('password')
      
        customer = LogIn(Username = Username,
                         Password = Password )
        
        return render(request,'home.html')


def Home(request):
    return render(request,'home.html')



def About(request):
    return render(request,'About.html')
    
def Booking(request):
    return render(request,'booking.html')
#------------------------------------------------------- MOVIES -----------------------------------------------------------------------------------------------

def Radhe(request):
    return render(request,'Radhe.html')

def kgf(request):
    return render(request,'KGF.html')