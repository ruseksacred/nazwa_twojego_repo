from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm

def register(reguest):
    form = CustomUserCreationForm()
    
    if reguest.method == 'POST':
        form = CustomUserCreationForm(reguest.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            form = CustomUserCreationForm()

    return render(reguest,'accounts/register.html', {'form': form})

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("admin:index")  # Zmień na nazwę swojej strony głównej
    else:
        form = AuthenticationForm()

    return render(request, "accounts/login.html", {"form": form})
            




