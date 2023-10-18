from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'uifiles/home.html')

def about(request):
    return render(request, 'uifiles/about-us.html')

def portfolio(request):
    return render(request, 'uifiles/portfolio.html')

def collaborate(request):
    return render(request, 'uifiles/Collaborations.html')

def sponsorship(request):
    return render(request, 'uifiles/sponsorship.html')

def newsevents(request):
    return render(request, 'uifiles/newsandevents.html')

def blog(request):
    return render(request, 'uifiles/blogs.html')

def career(request):
    return render(request, 'uifiles/career.html')

def enquiries(request):
    return render(request, 'uifiles/enquiries.html')

def youridea(request):
    return render(request, 'uifiles/youridea.html')

def formapply(request):
    return render(request, 'uifiles/applyforjobform.html')