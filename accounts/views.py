from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login as auth_login


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