from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login')
def index(request):
    return render(request,'index.html')

def auth_login(request):
    if request.method == "POST":
        usuario = request.POST['usuario']
        password = request.POST['password']
        
        user_auth = authenticate(request,username=usuario,password=password)
        print(user_auth)
        if user_auth is not None:
            login(request,user_auth)
            return redirect('/')
        else:
            context = {
                'error':'datos invalidos'
            }
            return render(request,'login.html',context)
    
    return render(request,'login.html')

def auth_logout(request):
    logout(request)
    return redirect('/')