from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "Account was created for " + user)
            return redirect('login')


    context = {'form': form}
    return render(request, 'regestration_and_authentication/register.html', context)


def loginPage(request):
    context = {}
    return render(request, 'regestration_and_authentication/login.html', context)


def homePage(request):
    context = {}
    return render(request, 'regestration_and_authentication/home.html', context)
