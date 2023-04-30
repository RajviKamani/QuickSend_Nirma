<<<<<<< HEAD
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate

# Create your views here.
def home(request):
    return render(request, 'home.html')
=======
from django.shortcuts import render
from app.models import Email
# Create your views here.
def home(request):
   return render(request,'home.html')

def login(request):
        
        if request.method == "POST":
           email = request.POST.get('email')
           password = request.POST.get('password')
    
           login=Email(email=email, password=password)
           login.save()
           return render(request,"home.html")
		
           

def signup(request):
      if request.method == "POST":
           email = request.POST.get('email')
           password = request.POST.get('password')
    
           signup=Email(email=email, password=password)
           signup.save()
		
           return render(request,"home.html")
    
>>>>>>> 8f085d4e74ea3952e53928203581291de5e9c25c

def about(request):
    return render(request, 'about.html')

<<<<<<< HEAD
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
=======
def upload(request):
    return render(request, 'upload.html')

>>>>>>> 8f085d4e74ea3952e53928203581291de5e9c25c
