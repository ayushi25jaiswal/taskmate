from django.shortcuts import render, redirect
from todolist_app.models import TaskList
from todolist_app.forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


@login_required
def todolist(request):
    if request.method == 'POST':
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save(commit=False).manage = request.user
            form.save()
        messages.success(request, ('New Task Added!'))
        return redirect('todolist')
    else:
        all_task = TaskList.objects.filter(manage=request.user)
        paginator = Paginator(all_task, 7)
        page = request.GET.get('pg')
        all_task = paginator.get_page(page)
        return render(request, 'todolist.html', {'all_task': all_task})

def delete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.delete()

    return redirect('todolist')

def edit_task(request, task_id):
    if request.method == "POST":
        task = TaskList.objects.get(pk=task_id)
        form = TaskForm(request.POST or None, instance= task)
        if form.is_valid():
            form.save()
        messages.success(request, ("Task Edited"))
        return redirect('todolist')

    else:
        task_obj = TaskList.objects.get(pk=task_id)
        return render(request, 'edit.html', {'task_obj': task_obj})

def complete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.done = True
    task.save()

    return redirect('todolist')

def pending_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.done = False
    task.save()

    return redirect('todolist')

def contact(request):
    return render(request, 'contact.html', {'contact_text': "Welcome to contact"})

def about(request):
    return render(request, 'about.html', {'about_text': "Welcome to about"})

def index(request):
    return render(request, 'index.html', {'index_text': "Welcome to HOME"})