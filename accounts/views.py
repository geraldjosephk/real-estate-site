from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def register(request):
    """Register user"""
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,'Username already used')
                return redirect('accounts:register')
            elif User.objects.filter(email=email).exists():
                messages.error(request,'Email already used')
                return redirect('accounts:register')
            else:
                user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
                user.save()
                messages.success(request,'Registration successful. You can login')
                return redirect('accounts:login')

        else:
            messages.error(request,'Passwords do not match')
            return redirect('accounts:register')
        
    return render(request,'accounts/register.html')

def login(request):
    """Login user"""
    if request.method == 'POST':
        print('Logged in')
        return redirect('accounts:login')
    else:
        return render(request,'accounts/login.html')

def logout(request):
    """Logout user"""
    return redirect(request,'pages/index.html')

def dashboard(request):
    """User dashboard"""
    return render(request,'accounts/dashboard.html')