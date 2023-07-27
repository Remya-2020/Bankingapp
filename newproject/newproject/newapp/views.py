from django.contrib import auth, messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import request
from django.shortcuts import render, redirect
from . models import Banking
# Create your views here.
def home(request):
    return render(request,"home.html")


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']

        if username == '' or password == '':
            messages.add_message(request, messages.INFO, "Username and password are required fields")
            return redirect('/register')

        elif password != cpassword:
            messages.add_message(request, messages.INFO, "Passwords do not match")
            return redirect('/register')

        elif User.objects.filter(username=username).exists():
            messages.add_message(request, messages.INFO, "Username Taken")
            return redirect('/register')

        else:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            print("User created")
            return redirect('/login')

    return render(request, "register.html")

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/login')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')

    return render(request,"login.html")




def new(request):
    return render(request,"new.html")


def form(request):
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('dob'):
            banking=Banking()
            banking.name = request.POST['name']
            banking.dob = request.POST['dob']
            banking.age = request.POST['age']
            banking.gender = request.POST['gender']
            banking.phoneno = request.POST['phoneno']
            banking.mailid = request.POST['mailid']
            banking.address = request.POST['address']
            banking.district = request.POST['district']
            banking.branch = request.POST['branch']
            banking.accounttype = request.POST['accounttype']
            banking.materials = request.POST['materials']
            banking.save()
            return render(request,"form.html")
        else:
            return render(request,"form.html")
    return render(request,"form.html")


def new(request):
    return render(request,"new.html")
def logout(request):

    auth.logout(request)
    return redirect('/home')


