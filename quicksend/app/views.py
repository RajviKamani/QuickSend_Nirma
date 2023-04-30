from django.shortcuts import render,redirect
from app.models import Email
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
# Create your views here.
def home(request):
   return render(request,'home.html')


def about(request):
    return render(request, 'about.html')

def login(request):
    if request.method=="POST":
        uname = request.POST['username']
        pass1 = request.POST['password']

        user = authenticate(username=uname, password=pass1)
        
        if user is not None:
            login(request,user)
            return render(request, 'home.html')
        
        else:
            messages.error(request, "Bad Credentials")
            return redirect('home')
        
    return render(request, 'login.html')

def signup(request):
    if request.method=="POST":
        uname = request.POST['username']
        pass1 = request.POST['password']

        my_user = User.objects.create_user(uname,pass1)
        my_user.uname = uname
        my_user.pass1 = pass1

        my_user.save()
        messages.success(request, "User has been created successfully")

        return redirect('login')

    return render(request, 'signup.html')

def upload(request):
    return render(request, 'upload.html')
