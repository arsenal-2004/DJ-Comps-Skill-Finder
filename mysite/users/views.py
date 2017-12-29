from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.urls import reverse


def login(request):
    if request.user.is_authenticated:
            return render(request, 'users/test.html', {})
    else:
        if request.method == 'POST':
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    auth_login(request, user)
                    return render(request, 'users/test.html', {})
                else:
                    error = 'The account has been disabled.'
                    return render(request, 'users/login.html',
                                  {'error': error})
            else:
                error = 'Invalid Username/Password'
                return render(request, 'users/login.html', {'error': error})
        else:
            return render(request, 'users/login.html', {})


def logout(request):
    auth_logout(request)
    return redirect(reverse('users:login'))
