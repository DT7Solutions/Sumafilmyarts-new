from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail,EmailMessage
from django.conf import settings
from .models import Collaboration,Sponsorship,ContactData,Ideas,Application

# Create your views here.


def home(request):
    return render(request, 'uifiles/home.html')

def about(request):
    return render(request, 'uifiles/about-us.html')

def portfolio(request):
    return render(request, 'uifiles/portfolio.html')

def newsevents(request):
    return render(request, 'uifiles/newsandevents.html')

def blogdetailspage1(request):
    return render(request, 'uifiles/blogdetailspage1.html')

def blogdetailspage2(request):
    return render(request, 'uifiles/blogdetailspage2.html')

def blog(request):
    return render(request, 'uifiles/blogs.html')


def career(request):
    return render(request, 'uifiles/career.html')

#collaboration form
def collaborate(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname',"")
        lastname = request.POST.get('lastname',"")
        email = request.POST.get('email',"")
        phone = request.POST.get('phone',"")
        brand_agency = request.POST.get('brand',"")
        industry = request.POST.get('industry',"")
        collaboration_Type = request.POST.get('Collaboration_Type',"")
        up_file = request.FILES['file']
        upload_file = settings.MEDIA_URL[1:] + "//pdf//" + str(up_file.name)
        
        oApplication = Collaboration(FirstName=firstname,LastName=lastname,Email=email,Phone=phone,Brand_Agency=brand_agency ,Industry=industry ,file=up_file ,Collaboration_Type=collaboration_Type)
        oApplication.save()
 
        subject="sumfilmyart"
        sucess =f'hi {lastname} Your message has been received, We will contact you soon'
        
        message ='''
        Subject:{}
        Message:{}
        From:{}
        '''.format(subject,sucess,email)
        try:
            mail = EmailMessage(subject,message, 'noreplaykajasuresh522@gmail.com', recipient_list=['kajasuresh522@gmail.com'])
            mail.attach_file(upload_file)
            # mail.attach(up_file.name, up_file.read(), up_file.content_type)
            #    mail = EmailMessage(subject,message, settings.EMAIL_HOST_USER , [email])
            mail.send()
        except:
            messages.error(request,'Your message has been failed, Please Try Agian')
    return render (request,"uifiles/collaborations.html",{'navbar':'collaboration'})
    return render(request, 'uifiles/collaborations.html')


#sponsorship form
def sponsorship(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname',"")
        lastname = request.POST.get('lastname',"")
        email = request.POST.get('email',"")
        phone = request.POST.get('phone',"")
        brand_agency = request.POST.get('brand',"")
        industry = request.POST.get('industry',"")
        sponcer_kind = request.POST.get('Kind_Sponcer',"")
        sponcer_type = request.POST.get('Sponcer_Type',"")
        up_file = request.FILES['file']
        upload_file = settings.MEDIA_URL[1:] + "//pdf//" + str(up_file.name)
        oApplication = Sponsorship(FirstName=firstname,LastName=lastname,Email=email,Phone=phone,Brand_Agency=brand_agency ,Industry=industry ,Kind_Sponcer=sponcer_kind,file=up_file ,Sponcer_Type=sponcer_type)
        oApplication.save()
        
        subject="sumfilmyart"
        message =f'hi {firstname} Your Application has been submited Sucessfully'
        
        # try:
        #     # bio_file = io.BytesIO(up_file.read().encode('utf8'))
        #     mail = EmailMessage(subject,message, settings.EMAIL_HOST_USER , [email])
        #     mail.attach_file(upload_file)
        #     mail.send()
           
        # except:
        #     messages.ERROR(request,'sending fail')

    return render (request,"uifiles/sponsorship.html",{'navbar':'sponsorship'})


#Enquiries Form
def enquiries(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname',"")
        lastname =  request.POST.get('lastname',"")
        email = request.POST.get('email',"")
        phone = request.POST.get('phone',"")
        subject = request.POST.get('subject',"")
        message = request.POST.get('message',"")
        
        oContactinfo = ContactData(FirstName=firstname,LastName=lastname,Email=email,Phone=phone,Subject=subject,Message=message)
        oContactinfo.save()
        sucess =f'hi {lastname} Your message has been received, We will contact you soon'
        
        message ='''
        Subject:{}
        Message:{}
        From:{}
        '''.format(subject,message,email)
        try:
            send_mail(subject, message,'noreplaybadugudinesh94@gmail.com',recipient_list=['team@sumaflimyarts.com']) 
            messages.success(request,sucess)
        except:
            messages.error(request,'Your message has been failed, Please Try Agian')
    return render(request, 'uifiles/enquiries.html')
     


# your idea form
def youridea(request):
    if request.method == "POST":
        name = request.POST.get('fname',"")
        email = request.POST.get('email',"")
        phone = request.POST.get('phone',"")
        subject = request.POST.get('subject',"")
        up_file = request.FILES['file']
        upload_file = settings.MEDIA_URL[1:] + "//pdf//" + str(up_file.name)

        oContactinfo = Ideas(Name=name,Email=email,Phone=phone,Subject=subject,file = up_file)
        oContactinfo.save()

        subject="sumfilmyart"
        message =f'hi {name} Your Application has been submited Sucessfully'

        # try:
        #     mail = EmailMessage(subject,message, settings.EMAIL_HOST_USER , ['team@sumaflimyarts.com'])
        #     mail.attach_file(upload_file)
        #     # mail.attach(up_file.name, up_file.read(), up_file.content_type)
        #     mail.send()
           
        # except:
        #     messages.ERROR(request,'sending fail')
    return render(request, 'uifiles/youridea.html')


def careerdetails(request):
    return render(request, 'uifiles/careerdetails.html')


#Apply_job form
def apply_job(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname',"")
        lastname = request.POST.get('lastname',"")
        email = request.POST.get('email',"")
        phone = request.POST.get('phone',"")
        experinces = request.POST.get('work_exp',"")
        up_file = request.FILES['file']
        upload_file = settings.MEDIA_URL[1:] + "//pdf//" + str(up_file.name)
        
        oApplication = Application(FirstName=firstname,LastName=lastname,Email=email,Phone=phone,Experience=exp, file=up_file )
        oApplication.save()
        subject="JobApplication"
        sucess =f'hi {firstname} Your Application has been submited Sucessfully'
        message ='something'
        # try:
        #     mail = EmailMessage(subject,message, settings.EMAIL_HOST_USER , ['team@sumafilmyarts.com'])
        #     mail.attach_file(upload_file)
        #     print('fill attach sucessfully')
        #     mail.send()
        #     messages.success(request,sucess)
        # except:
        #     messages.ERROR(request,'sending fail')
    return render (request, 'uifiles/apply-job.html')