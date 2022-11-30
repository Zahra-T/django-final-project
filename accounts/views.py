from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required

def signup(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            form=CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                #message
                return redirect('/')
            else:
                #message
                return redirect('accounts:signup')   
        return render(request, 'accounts/signup_login.html')
    return redirect('/')
# Create your views here.

@login_required
def logout(request):
    auth.logout(request)
    return redirect('/')
