from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request,"home/dashboard.html")
def aboutus(request):
    return render(request,"home/aboutus.html")
def contactus(request):
    return render(request,"home/contactus.html")
def home(request):
    return render(request,"home/home.html")