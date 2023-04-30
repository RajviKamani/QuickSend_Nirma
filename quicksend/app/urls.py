from django.urls import path
from app import views

urlpatterns = [
    path('', views.home, name='home'),
     path('home', views.home, name='home'),
    path('upload', views.upload, name='upload'),
    path('about', views.about, name='about'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),

]
