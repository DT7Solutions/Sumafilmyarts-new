from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'uifiles/home.html')

def portfolio(request):
    return render(request, 'uifiles/portfolio.html')