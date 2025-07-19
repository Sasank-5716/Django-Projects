from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from todo import models
from todo.models import TodoItem
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

def signup(request):
    if request.method == 'POST':
        fnm = request.POST.get('fnm')
        emailid = request.POST.get('emailid')
        pwd = request.POST.get('pwd')
        print(fnm, emailid, pwd)
        myuser = User.objects.create_user(username=fnm, email=emailid, password=pwd)
        myuser.save()
        return redirect('/login')
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('/todo')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        print(title)
        obj = models.TodoItem(title)
        obj.save()
    return render(request, 'todo.html')