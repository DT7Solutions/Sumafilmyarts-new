from django.urls import path
from app import views
from app.views import apply_job,enquiries

urlpatterns = [
   
    path('', views.home, name='home'),
    path('about/',views.about, name='about'),
    path('portfolio/',views.portfolio, name='portfolio'),
    path('newsevents/',views.newsevents, name='newsevents'),
    path('blog/', views.blog, name='blog'),
    path('blogdetailspage1/', views.blogdetailspage1,name='blogdetailspage1'),
    path('blogdetailspage2/', views.blogdetailspage2,name='blogdetailspage2'),
    path('career/', views.career, name='career'),
    path('collaborate/', views.collaborate, name='collaborate'),
    path('sponsorship/',views.sponsorship, name='sponsorship'),
    path('enquiries/',enquiries, name='enquiries'),
    path('youridea/', views.youridea, name='youridea'),
    path('careerdetails/', views.careerdetails, name='careerdetails'),
    path('applyjobform/', apply_job, name='applyjobform'),
]
