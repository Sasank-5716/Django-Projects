from django.shortcuts import render

def home(request):
    return render(request, 'home.html',{})

def login_user(request):
    if request.Method == 'POST':
        
    return render(request, 'login.html', {}) 

def logout_user(request):
    pass


