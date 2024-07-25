from django.shortcuts import render, redirect
from .forms import CustomerForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from django.contrib import messages


def home_view(request):
    return render(request, 'base/index.html')


def order_view(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_success')
    else:
        form = CustomerForm()
    return render(request, 'base/order_form.html', {'form': form})

def order_success(request):
    return render(request, 'base/order_success.html')


@staff_member_required
def login_view(request):
    if request.user.is_authenticated and request.user.is_staff:
        return redirect('admin:index')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('admin:index')
        else:
            messages.error(request, 'Invalid credentials or you are not authorized to access the admin site.')
    
    return render(request, 'base/login.html')


# Create your views here.
