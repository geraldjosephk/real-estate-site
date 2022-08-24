from multiprocessing import context
from django.shortcuts import redirect, render
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from contacts.models import Contact

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
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request,'Your are logged in')
            return redirect('accounts:dashboard') 
        else:
            messages.error(request,'Invalid credentials')
            return redirect('accounts:login')
    else:
        return render(request,'accounts/login.html')

@login_required(login_url = 'login')
def logout(request):
    """Logout user"""
    auth.logout(request)
    messages.success(request, 'You are logged out.')
    return redirect('pages:index')

@login_required(login_url = 'login')
def dashboard(request):
    """User dashboard"""
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    context = {
        'contacts': user_contacts
    }
    return render(request,'accounts/dashboard.html', context)