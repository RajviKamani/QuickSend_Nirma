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
    

def about(request):
    return render(request, 'about.html')

def upload(request):
    return render(request, 'upload.html')

