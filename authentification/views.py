from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.contrib.auth import login, authenticate
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.profile_picture = form.cleaned_data.get('profile_picture')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            messages.success(request, f'Hello {user.username}, Your account has been created successfully!')
            return redirect('accounts')
    else:
        form = SignUpForm()
    return render(request, 'registration/register.html', {'form': form})