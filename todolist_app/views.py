from django.shortcuts import render, redirect
from todolist_app.models import TaskList
from todolist_app.forms import TaskForm
from django.contrib import messages

def todolist(request):
    if request.method == 'POST':
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request, ('New Task Added!'))
        return redirect('todolist')
    else:
        all_task = TaskList.objects.all
        return render(request, 'todolist.html', {'all_task': all_task})

def contact(request):
    return render(request, 'contact.html', {'contact_text': "Welcome to contact"})

def about(request):
    return render(request, 'about.html', {'about_text': "Welcome to about"})