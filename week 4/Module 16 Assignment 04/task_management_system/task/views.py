from django.shortcuts import render, redirect, get_object_or_404
from .forms import taskForm
from .models import task

# Create your views here.
def add_task(request):
    form = taskForm()
    
    if request.method == 'POST':
        form = taskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show_tasks")
        
    return render(request, './task/add.html', {"form": form})



def delete_task(request, pk):
    task_instance = get_object_or_404(task, pk=pk)
    task_instance.delete()
    return redirect("show_tasks")

def show_tasks(request):
    tasks = task.objects.all()
    return render(request, './task/show.html', {"tasks": tasks})

def edit_task(request, pk):
    task_instance = get_object_or_404(task, pk=pk)
    form = taskForm(instance=task_instance)
    
    if request.method == 'POST':
        form = taskForm(request.POST, instance=task_instance)
        if form.is_valid():
            form.save()
            return redirect("show_tasks")
        
    return render(request, './task/add.html', {"form": form})
