from django.contrib.auth import authenticate, login
from django.core.checks import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from django.http import HttpResponse
from .forms import ImageForm
from .forms import  CreateUserForm
from .models import *


def welcome(request):
    #return HttpResponse("<h1>welcome to the page</h1>")
    return render(request,"welcome.html")


def loginpage(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'login.html', context)


def register(request):
    if request.user.is_authenticated:
        return redirect('login')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')

        context = {'form': form}
        return render(request, 'register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def dashboard(request):
    return render(request,"dashboard.html")

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,"contact.html")

def feedback(request):
    return render(request,"feedback.html")

def homepage(request):
    return render(request,"homepage.html")

def help(request):
    return render(request,"help.html")

def transaction(request):
    return render(request,"transaction.html")

def land(request):
    return render(request,"land.html")

def commercial(request):
    return render(request, "commercial.html")

def development(request):
    return render(request, "development.html")

def property_management(request):
    return render(request, "property_management.html")

def industrial(request):
    return render(request, "industrial.html")

def villa(request):
    return render(request, "villa.html")

def details(request):
    return render(request,"details.html")

def new(request):
    email=request.POST.get("email")
    fname=request.POST.get("fname")
    lname=request.POST.get("lname")
    num=request.POST.get("num")
    add=request.POST.get("add")
    pin=request.POST.get("pin")
    state=request.POST.get("state")

    o_ref =Details(email=email,fname=fname,lname=lname,num=num,add=add,pin=pin,state=state)
    o_ref.save()

    return render(request,"details.html",{"message": "registered!"})

def new1(request):
    fname=request.POST.get("fname")
    lname=request.POST.get("lname")
    country=request.POST.get("country")

    o_ref =Feedback(fname=fname,lname=lname,country=country)
    o_ref.save()

    return render(request,"feedback.html",{"message":"succesfully stored your feedback!"})


def index(request):
    if request.method == "POST":
        form = ImageForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            obj = form.instance
            return render(request, 'property.html', {"obj": obj})
    else:
        form = ImageForm()
    img = Image.objects.all()
    return render(request, 'property.html', {"img": img, "form": form})


def new2(request):
    fname=request.POST.get('fname')
    email=request.POST.get('email')
    add=request.POST.get('add')
    city=request.POST.get('city')
    state=request.POST.get('state')
    zip=request.POST.get('zip')
    cname=request.POST.get('cname')
    cnum=request.POST.get('cnum')
    expmonth=request.POST.get('expmonth')
    expyear=request.POST.get('expyear')
    cvv=request.POST.get('cvv')

    o_ref = Tran(fname=fname,email=email,add=add,city=city,state=state,zip=zip, cname=cname,cnum=cnum,expmonth=expmonth,expyear=expyear,cvv=cvv)
    o_ref.save()

    return render(request, "transaction.html", {"message":"succesfully stored your transaction details!"})