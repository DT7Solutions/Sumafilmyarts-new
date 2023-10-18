from django.urls import path
from app import views


urlpatterns = [
   
    path('', views.home, name='home'),
    path('about/',views.about, name='about'),
    path('portfolio/',views.portfolio, name='portfolio'),
    path('collaborate/', views.collaborate, name='collaborate'),
    path('sponsorship/',views.sponsorship, name='sponsorship'),
    path('newsevents/',views.newsevents, name='newsevents'),
    path('blog/', views.blog, name='blog'),
    path('career/', views.career, name='career'),
    path('enquiries/',views.enquiries, name='enquiries'),
    path('youridea/', views.youridea, name='youridea'),
    path('formapply/', views.formapply, name='formapply'),
]
