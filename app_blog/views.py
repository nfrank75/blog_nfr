from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'app_blog/home.html')

def about(request):
    return render(request, 'app_blog/about.html')
