from django.shortcuts import redirect, render

# Create your views here.
def register(request):
    """Register user"""
    if request.method == 'POST':
        print('Registered')
        return redirect('accounts:register')
    else:
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