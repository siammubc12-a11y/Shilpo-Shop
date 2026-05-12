from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect

from django.contrib.auth import login, logout, authenticate

from django.contrib.auth.decorators import login_required

from .forms import RegisterForm, LoginForm, UserProfileForm

from .models import UserProfile


# Register

def register_view(request):

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save()

            UserProfile.objects.create(user=user)

            login(request, user)

            return redirect('home')

    else:

        form = RegisterForm()

    return render(request, 'users_app/register.html', {
        'form': form
    })


# Login

def login_view(request):

    if request.method == 'POST':

        form = LoginForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']

            password = form.cleaned_data['password']

            user = authenticate(
                request,
                username=username,
                password=password
            )

            if user:

                login(request, user)

                return redirect('home')

    else:

        form = LoginForm()

    return render(request, 'users_app/login.html', {
        'form': form
    })


# Logout

def logout_view(request):

    logout(request)

    return redirect('login')


# Profile

@login_required
def profile_view(request):

    profile = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':

        form = UserProfileForm(
            request.POST,
            instance=profile
        )

        if form.is_valid():

            form.save()

            return redirect('profile')

    else:

        form = UserProfileForm(instance=profile)

    return render(request, 'users_app/profile.html', {
        'form': form
    })