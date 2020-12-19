from django.shortcuts import render, redirect
from django.http import request
from django.contrib import messages
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib.auth.models import User
from .models import AddIssue
from django.contrib.sessions.models import Session
from .models import AddIssue


def home(request):
    if request.session.has_key('email'):
        return render(request, 'index.html')
    return redirect('login')


def signup(request):
    #    messages.error(request, 'Create your account')
    if request.method == "POST":
        uname = request.POST["uname"]
        email = request.POST["email"]
        password = request.POST["password"]
        print(uname, email, password)
        messages.success(request, 'Account Created, Login to Continue')
        return redirect('login')
    else:
        return render(request, 'signup.html')


def login(request):
    #    messages.success(request, 'Account Created Successfully')
    if request.session.has_key('email'):
        return render(request, 'index.html', {'sess': request.session['email']})
    if request.method == 'POST':
        username = request.POST["email"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)

        if user:

            request.session['email'] = username
            # print(request.session['email'])
            auth_login(request, user)
            messages.success(request, "Successfully Logged in")
            return render(request, 'index.html', {'sess': request.session['email']})
        else:
            messages.error(request, "Couldn't Login , Try Again")
            return redirect('login')
    else:
        return render(request, 'login.html')


def addIssue(request):
    return render(request, 'AddIssue.html', {'sess': request.session['email']})


def profile(request):
    return render(request, 'profile.html', {'sess': request.session['email']})


def logout(request):
    # print(request.session['email'])
    try:
        del request.session['email']
    except:
        pass
    auth_logout(request)
    messages.success(request, "Successfully Logged out")
    return redirect('home')
