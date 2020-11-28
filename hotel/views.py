from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .models import Contact,Order, Product, Pune, Bengaluru, Mumbai, Goa
from math import ceil

# Create your views here.


def index(request):
    products = Product.objects.all()
    pune = Pune.objects.all()
    benglore = Bengaluru.objects.all()
    mumbai = Mumbai.objects.all()
    goa = Goa.objects.all()
    print(pune)
    print(products)
    n = 9
    print(n)
    nslide = n//4+ceil((n/4)-(n//4))
    params = {'no_of_slide': nslide, 'range': range(
        1, nslide), 'product': products, 'pune': pune, 'benglore': benglore, 'mumbai': mumbai, 'goa': goa}
    return render(request, 'index.html', params)

def about(request):
    return render(request,'about.html')







def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
             messages.info(request, 'Your username or password is incorrect')
             return redirect('signin')
    return  render(request,'signIn.html')


def register(request):
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username is alerady in used')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email is alerady in used')
                return redirect('register')
            else:
                user=User.objects.create_user(first_name=first_name, last_name=last_name , username=username, password=password, email=email)
                user.save()
                return redirect('signin')
        else:
            messages.info(request, 'Confirm password not matching')
            return redirect('register')
           
    return render(request,'signup.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        desc=request.POST.get('desc','')
        contact=Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
    return render(request, 'contact.html')

def order(request):
    if request.method=="POST":
        username=request.POST.get('username','')
        name=request.POST.get('name','')
        price=request.POST.get('price','')
        uname=request.POST.get('uname','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        room=request.POST.get('room','')
        day1=request.POST.get('day1','')  
        month1=request.POST.get('month1','')
        year1=request.POST.get('year1','')
        day2=request.POST.get('day2','')  
        month2=request.POST.get('month2','')
        year2=request.POST.get('year2','')
        cal=request.POST.get('cal','')
        order=Order(username=username,name=name,price=price,uname=uname,email=email,phone=phone,room=room,day1=day1,month1=month1,year1=year1,day2=day2,month2=month2,year2=year2,cal=cal)
        order.save()
        return redirect('thankyou')

    return render(request, 'order.html')
def thankyou(request):
    return render(request,'thankyou.html')

# product view
def productView(request,  myid):
     product=Product.objects.filter(id=myid)
     return render(request,'productView.html',{'product':product[0]})

def benglore(request,  myid):
     benglore = Bengaluru.objects.filter(id=myid)
     return render(request,'productView.html',{'benglore':benglore[0]})

def goa(request,  myid):
     goa = Goa.objects.filter(id=myid)
     return render(request,'productView.html',{'goa':goa[0]})

def pune(request,  myid):
     pune = Pune.objects.filter(id=myid)
     return render(request,'productView.html',{'pune':pune[0]})

def mumbai(request,  myid):
     mumbai = Mumbai.objects.filter(id=myid)
     return render(request,'productView.html',{'mumbai':mumbai[0]})


