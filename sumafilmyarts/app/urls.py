from django.urls import path
from app import views
from app.views import apply_job,enquiries

urlpatterns = [
   
    path('', views.home, name='home'),
    path('about/',views.about, name='about'),
    path('portfolio/',views.portfolio, name='portfolio'),
    path('newsevents/',views.newsevents, name='newsevents'),
    path('blog/', views.blog, name='blog'),
    path('blogdetailspage/<str:slug>', views.blogdetailspage,name='blogdetailspage'),
    # path('blogdetailspage2/', views.blogdetailspage2,name='blogdetailspage2'),
    path('career/', views.career, name='career'),
    path('careerdetails/<str:slug>', views.careerdetails, name='careerdetails'),
    path('collaborate/', views.collaborate, name='collaborate'),
    path('sponsorship/',views.sponsorship, name='sponsorship'),
    path('enquiries/',enquiries, name='enquiries'),
    path('youridea/', views.youridea, name='youridea'),
    path('applyjobform/', apply_job, name='applyjobform'),
]
