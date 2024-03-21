from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home/index.html')

def about(request):
    return render(request,'home/about.html')

def feature(request):
    return render(request,'home/feature.html')

def team(request):
    return render(request,'home/team.html')

def menu(request):
    return render(request,'home/menu.html')

def booking(request):
    return render(request,'home/booking.html')

def contact(request):
    return render(request,'home/contact.html')

def blog(request):
      return render(request,'home/blog.html')

def blogDetail(request):
      return render(request,'home/blogdetail.html')