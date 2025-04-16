from django.shortcuts import render, redirect
from .forms import UserRegistration, UserLoginForm
from django.contrib.auth import messages


def user_registration(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('login')
    else:
        form = UserRegistration()
    return render(request, 'user_accounts/register.html', {'form': form})