from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm
from django.http import HttpRequest, HttpResponse


# 🔐 REGISTER VIEW
def register_view(request: HttpRequest) -> HttpResponse:
    """
    Handle user registration. Auto-login after successful registration.
    """
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto login after register
            # Redirect to home or posts list after registration
            return redirect('posts:list')
    else:
        form = RegisterForm()

    context = {'form': form}
    return render(request, 'users/register.html', context)


# 🔐 LOGIN VIEW
def login_view(request: HttpRequest) -> HttpResponse:
    """
    Handle user login with next redirect support.
    """
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to next page if exists, otherwise to posts list
                next_url = request.POST.get('next')
                return redirect(next_url or 'posts:list')
    else:
        form = AuthenticationForm()

    context = {'form': form}
    return render(request, 'users/login.html', context)


# 🔒 LOGOUT VIEW
def logout_view(request: HttpRequest) -> HttpResponse:
    """
    Logout the user and redirect to login page.
    """
    logout(request)
    return redirect('users:login')
