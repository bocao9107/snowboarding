from django.shortcuts import render
# Create your views here.
def homepage(request):
    return render(request,"index.html",)

def snowboarding(request):
    return render(request,"snowboarding.html")

def sking(request):
    return render(request,"sking.html")

def about(request):
    return render(request,"about.html")

def discussion(request):
    return render(request,"discussion.html")

def sell(request):
    return render(request,"sell.html")
