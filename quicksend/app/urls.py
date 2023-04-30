from django.urls import path
from app import views

urlpatterns = [
    path('', views.home, name='home'),
<<<<<<< HEAD
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('upload', views.upload, name='upload'),
]
=======
     path('home', views.home, name='home'),
    path('upload', views.upload, name='upload'),
    path('about', views.about, name='about'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),

]
>>>>>>> 8f085d4e74ea3952e53928203581291de5e9c25c
