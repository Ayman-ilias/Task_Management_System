from django.shortcuts import render, redirect
from .import forms,models

def add_task(request):
    if request.method == 'POST':
        task_form = forms.TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect('show')
    else:
        task_form = forms.TaskForm
    return render(request, 'task.html', {'form': task_form})

def edit_task(request,id):
    t=models.Task.objects.get(pk=id)
    task_form = forms.TaskForm(instance=t)
    if request.method == 'POST':
        task_form = forms.TaskForm(request.POST,instance=t)
        if task_form.is_valid():
            task_form.save()
            return redirect('show')
    return render(request, 'task.html', {'form': task_form})

def delete_task(request,id):
    p=models.Task.objects.get(pk=id)
    p.delete()
    return redirect('show')


