from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

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
            




