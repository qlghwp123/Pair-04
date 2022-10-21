from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup(req):
    if req.method == 'POST':
        form = CustomUserCreationForm(req.POST)

        if form.is_valid():
            user = form.save()
            auth_login(req, user)

            return redirect('reviews:index')

    else:
        form = CustomUserCreationForm()

    context = {
        'form': form
    }

    return render(req, 'accounts/signup.html', context)


def login(req):
    if req.method == 'POST':
        form = AuthenticationForm(req, data=req.POST)

        if form.is_valid():
            auth_login(req, form.get_user())

            return redirect('reviews:index')

    else:
        form = AuthenticationForm(req)

    context = {
        'form': form
    }

    return render(req, 'accounts/login.html', context)


@login_required
def logout(req):
    auth_logout(req)

    return redirect('accounts:login')