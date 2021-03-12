from .forms import *
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import DetailView, ListView, TemplateView
from .models import *
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from .forms import UserSignUpForm

def index(request):
    return render(request,'index.html')

def UserSignup(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            role = form.cleaned_data.get('role')
            print(role)
            login(request, user)
            return redirect('index')
    else:
        form = UserSignUpForm()
    return render(request, 'donor/donor_signup.html', {'form': form})


