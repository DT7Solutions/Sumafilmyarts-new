from django.db import models
from datetime import datetime
from .app import ContentTypeRestrictedFileField
# Create your models here.

class Collaboration(models.Model):
        FirstName = models.CharField(max_length=100)
        LastName = models.CharField(max_length=100)
        Email = models.EmailField(max_length=50)
        Phone = models.CharField(max_length=10)
        Brand_Agency = models.CharField(max_length=100)
        Industry = models.CharField(max_length=100)
        Collaboration_Type = models.CharField(max_length=25)
        file = ContentTypeRestrictedFileField(
            upload_to='pdf',
            content_types=['application/pdf', 'application/msword','application/vnd.openxmlformats-officedocument.wordprocessingml.document'],
            max_upload_size=2621440
        ) 
        Date = models.DateTimeField(default = datetime.now())
        def __str__(self):
                return self.FirstName



class Sponsorship(models.Model):
            FirstName = models.CharField(max_length=100)
            LastName = models.CharField(max_length=100)
            Email = models.EmailField(max_length=50)
            Phone = models.CharField(max_length=10)
            Brand_Agency = models.CharField(max_length=35)
            Industry = models.CharField(max_length=30)
            Kind_Sponcer = models.CharField(max_length=30)
            Sponcer_Type = models.CharField(max_length=30)
            file = ContentTypeRestrictedFileField(
                upload_to='pdf',
                content_types=['application/pdf', 'application/msword','application/vnd.openxmlformats-officedocument.wordprocessingml.document'],
                max_upload_size=2621440
            ) 
            Date = models.DateTimeField(default=datetime.now())
            def __str__(self):
                return self.FirstName


# enquiries form
class ContactData(models.Model):
            FirstName = models.CharField(max_length=100)
            LastName = models.CharField(max_length=100)
            Email = models.EmailField(max_length=254)
            Phone = models.CharField(max_length=10)
            Subject = models.CharField(max_length=100)
            Message = models.CharField(max_length=500)
            Date = models.DateTimeField(default=datetime.now())

            def __str__(self):
                return self.FirstName


#Your Idea form
class Ideas(models.Model):
            Name = models.CharField(max_length=100)
            Email = models.EmailField(max_length=254)
            Phone = models.CharField(max_length=10)
            Subject = models.CharField(max_length=400)
            file = ContentTypeRestrictedFileField(
                upload_to='pdf',
                content_types=['application/pdf', 'application/msword','application/vnd.openxmlformats-officedocument.wordprocessingml.document'],
                max_upload_size=2621440
            ) 
            Date = models.DateTimeField(default=datetime.now())
            def __str__(self):
                return self.Name
            

#Apply Form
class Application(models.Model):
    FirstName = models.CharField(max_length=50,blank=True)
    LastName = models.CharField(max_length=50,blank=True)
    Email = models.EmailField(max_length=254)
    Phone = models.CharField(max_length=10)
    Experience = models.CharField(max_length=20)
    # field_name = models.FileField(upload_to=None, max_length=254) 
    file = ContentTypeRestrictedFileField(
        upload_to='pdf',
        content_types=['application/pdf', 'application/msword','application/vnd.openxmlformats-officedocument.wordprocessingml.document'],
        max_upload_size=2621440
    ) 
    # Term_check = models.BooleanField()
    Date = models.DateTimeField(default=datetime.now())
    
    def __str__(self):
                return self.FirstName



class Category(models.Model):
    Name = models.CharField(max_length=30,default='heading')
    Created = models.DateTimeField(default=datetime.now())

    def __str__(self):
            return self.Name
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

STATUS = (
       (0,"Draft"),
       (1,"Publish")
)

    
class BlogPost(models.Model):
    Id = models.AutoField(primary_key=True)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='Categories')
    Title = models.CharField(max_length=225, default="title")
    Description = models.CharField(max_length=2000, blank=True, null=True)
    Image1 = models.ImageField(upload_to='uploads/')
    Body = models.TextField(blank=True, null=True)
    Sluglink = models.CharField(max_length=200, blank=True, null=True)
    CreatedName = models.CharField(max_length=100)
    Created_at = models.DateTimeField(default=datetime.now())
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering : ['-Created_at']

    def __str__(self):
           return self.Title


        
    
class Career(models.Model):
    title = models.CharField(max_length=255)
    Image1 = models.ImageField(upload_to='uploads/')
    Image2 = models.ImageField(upload_to='uploads/', blank=True, null=True)
    location = models.CharField(max_length=100)
    posted_date = models.DateField(auto_now_add=True)
    Sluglink = models.CharField(max_length=150, blank=True, null=True)
    full_time = models.CharField(max_length=50)
    description = models.TextField()
    Body = models.TextField(blank=True,null=True) 
    job_title = models.CharField(max_length=50, blank=True, null=True)
    experience = models.CharField(max_length=50, null=True,blank=True)
    gender = models.CharField(max_length=50,null=True, blank=True)
    workingtime = models.CharField(max_length=50, null=True, blank=True)
    age = models.IntegerField(default=0,blank=True, null=True)
    dead_line = models.CharField(max_length=50, blank=True, null=True)
    



    def __str__(self):
        return self.title
    
