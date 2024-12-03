from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import get_user_model

User = get_user_model()
from .forms import LoginForm, SignUpForm
from django.shortcuts import render, redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def sign_in(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'
    return render(request, "homepage/login.html", {"form": form, "msg": msg})

def sign_up(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created - please <a href="/login">login</a>.'
            success = True
            return redirect("/login/")
        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "homepage/register.html", {"form": form, "msg": msg, "success": success})


def page_user(request):
  template = loader.get_template('homepage/page_user.html')
  return HttpResponse(template.render())


def logout_view(request):
  """Logs out the user and redirects to login page."""
  # Logout the user using Django's logout function
  logout(request)
  # Optionally, clear any session data related to login
  # del request.session['user_data']  # Example removing user data
  return redirect('/')  # Redirect to login page after logout