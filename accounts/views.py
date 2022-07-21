from django.shortcuts import redirect, render

# Create your views here.
def register(request):
    """Register user"""
    return render(request,'accounts/register.html')

def login(request):
    """Login user"""
    return render(request,'accounts/login.html')

def logout(request):
    """Logout user"""
    return redirect(request,'pages/index.html')

def dashboard(request):
    """User dashboard"""
    return render(request,'accounts/dashboard.html')