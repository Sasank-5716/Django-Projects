from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from todo import models
from todo.models import TodoItem

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
    return render(request, 'login.html')