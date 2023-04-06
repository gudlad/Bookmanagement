from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required

# @login_required(login_url='login')
# def index(request):
#     return render(request,"index.html")

# Create your views here.
def register(request):
    if request.method=='POST':
        print(request.user)
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        password_repeat=request.POST.get('password_repeat')
        if password==password_repeat:
            if User.objects.filter(username=username).exists():
                messages.warning(request,"User name already exists!!")
                return render(request,"main/register.html")
            elif User.objects.filter(email=email).exists():
                messages.warning(request,"Email already exists!!")
                return render(request,"main/register.html")
            else:    
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()
                return render(request,"main/login.html")
        else:
            messages.warning(request,"Password Not Matching!!")
            return render(request,"main/register.html")
    else:
        return render(request,"main/register.html")

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        passw = request.POST['pass']
        user = auth.authenticate(username=username, password=passw)
        if user is not None:
            auth.login(request, user)
            return redirect('main/list_of_books')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')
    else:
        return render(request,"main/login.html")

def logout(request):
    auth.logout(request)
    return redirect('/login')