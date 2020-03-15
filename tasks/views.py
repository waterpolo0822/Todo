from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.utils import timezone
from django.views.decorators.http import require_POST

from tasks import forms
from tasks.forms import TaskForm, TaskEdit
from .models import Task


def task_list(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        tasks = Task.objects.all()
        if form.is_valid():
            task = form.save(commit=False)
            task.create_date = timezone.now()
            task.due_date = timezone.now()
            task.save()
            render(request, 'tasks/task_list.html', {'tasks': tasks, 'form': form})
    else:
        form = TaskForm()
        tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks, 'form': form})


def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskEdit(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskEdit(instance=task)
    return render(request, 'tasks/task_detail.html', {'task': task, 'form': form})


@require_POST
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('task_list')






