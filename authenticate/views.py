# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from  django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .forms import SignUpForm, EditProfileForm



def home(request):
    return render (request, 'authenticate/home.html', {})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, ('Login Successful!'))
            return redirect('home')

        else:
            messages.success(request, ('Login Failed! please enter the correct Credentials!'))
            return redirect ('login')

    else:
        return render(request, 'authenticate/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request,('You have loged out!'))
    return redirect ('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, ('Regisraion Successful!'))
            return redirect('home')
    else:
        form = SignUpForm()

    conext = {'form': form}
    return render(request, 'authenticate/register.html', conext)


def edit_profile(request):
        if request.method == 'POST':
            form = EditProfileForm(request.POST, instance = request.user)
            if form.is_valid():
                form.save()
                messages.success(request, ('You have Updated your profile Successfully!'))
                return redirect('home')
        else:
            form = EditProfileForm(instance = request.user)

        conext = {'form': form}
        return render(request, 'authenticate/edit_profile.html', conext)


def change_password(request):
        if request.method == 'POST':
            form = PasswordChangeForm(data = request.POST, user = request.user)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                messages.success(request, ('You have Changed Your Password!'))
                return redirect('home')
        else:
            form = PasswordChangeForm(user = request.user)

        conext = {'form': form}
        return render(request, 'authenticate/change_password.html', conext)
