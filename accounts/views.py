from django.shortcuts import render, redirect
from . forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login


# Create your views here.

def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('post_list')
    return render(request, 'accounts/login.html', {'form': form})


def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username,password=password)
        login(request, new_user)
        return redirect('post_list')
    return render(request, 'accounts/register.html', {'form': form})