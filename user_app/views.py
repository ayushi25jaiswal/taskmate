from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
    if request == 'POST':
        register_form = UserCreationForm(request.POST)
        if register_form.is_valid():
            # register_form.save()
            messages.success(request, ('NEw User Created'))
            return redirect(request, 'todolist')
    else:
        register_form = UserCreationForm()
    return render(request, 'register.html', {'register_form': register_form})