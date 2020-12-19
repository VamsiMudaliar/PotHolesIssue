from django.shortcuts import render, redirect
from django.http import request
from django.contrib import messages
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib.auth.models import User
from .models import AddIssue
from django.contrib.sessions.models import Session
from .models import AddIssue
from django.contrib.auth.decorators import login_required


def home(request):
    if request.session.has_key('email'):
        return render(request, 'index.html', {'sess': request.session['email'], 'items': AddIssue.objects.all()})
    return redirect('login')


def signup(request):
    #    messages.error(request, 'Create your account')
    if request.method == "POST":
        uname = request.POST["uname"]
        email = request.POST["email"]
        password = request.POST["password"]
        user = User(username=uname, email=email, password=password)
        user.save()
        messages.success(request, 'Account Created, Login to Continue')
        return redirect('login')
    else:
        return render(request, 'signup.html')


def login(request):
    #    messages.success(request, 'Account Created Successfully')
    if request.session.has_key('email'):
        return redirect('home')
    if request.method == 'POST':
        uname = request.POST["uname"]
        password = request.POST["password"]

        user = authenticate(username=uname, password=password)
        if user:
            request.session['email'] = uname
            # print(request.session['email'])
            print(user, request.session.get("email"))
            auth_login(request, user)
            messages.success(request, "Successfully Logged in")
            return redirect('home')
        else:
            messages.error(request, "Couldn't Login , Try Again")
            return redirect('login')
    else:
        return render(request, 'login.html')


@login_required
def addIssue(request):
    if request.method == 'POST':
        title = request.POST["issueTitle"]
        location = request.POST["location"]
        file_img = request.FILES["IssueImage"]
        user = User.objects.filter(username=request.session['email']).first()
        obj = AddIssue(issue_title=title, author=user, location=location,
                       issue_img=file_img)
        obj.save()
        messages.success(request, 'Issue Raised Successfully')
        return redirect('home')

    return render(request, 'AddIssue.html', {'sess': request.session['email']})


@login_required
def profile(request):
    return render(request, 'profile.html', {'sess': request.session['email']})


@login_required
def myIssues(request):
    user = User.objects.filter(username=request.session['email']).first()
    print(user)
    issues_by_him = AddIssue.objects.filter(author=user).all()
    return render(request, 'myIssues.html', {'sess': request.session['email'], 'my_issues': issues_by_him})


def deleteIssue(request, issueid):
    obj = AddIssue.objects.filter(issue_id=issueid).delete()
    return redirect('myIssues')


def logout(request):
    # print(request.session['email'])
    try:
        del request.session['email']
    except:
        pass
    auth_logout(request)
    messages.success(request, "Successfully Logged out")
    return redirect('home')
