from django.shortcuts import render,redirect
from .form import TaskForm
from .models import Task
from django.contrib.auth.decorators import login_required
from django.http import Http404,HttpResponse
# Create your views here.

def index(request):
    return render(request, 'to_do_list/index.html')

@login_required
def task_list(request):
    tasks = Task.objects.filter(owner=request.user).order_by('created_at')
    context = {'tasks':tasks}
    return render(request, 'to_do_list/task_list.html', context)

@login_required
def create_task(request):
    if request.method != 'POST':
        form = TaskForm()
    else:
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.owner = request.user
            new_task.save()
        return redirect('to_do_list:task_list')
    context = {'form':form}
    return render(request, 'to_do_list/create_task.html', context)

@login_required
def update_task(request,task_id):
    tasks = Task.objects.get(id=task_id)
    if tasks.owner != request.user:
        raise Http404
    if request.method != 'POST':
        form = TaskForm(instance=tasks)
    else:
        form = TaskForm(request.POST,instance=tasks)
        if form.is_valid():
            form.save()
        return redirect('to_do_list:task_list')
    context = {'tasks':tasks,'form':form}
    return render(request, 'to_do_list/update_task.html', context)

@login_required
def delete_task(request,task_id):
    tasks = Task.objects.get(id=task_id)
    if tasks.owner != request.user:
        raise Http404
    if request.method == 'POST':
        tasks.delete()
        return redirect('to_do_list:task_list')
    context = {'tasks':tasks}
    return render(request, 'to_do_list/delete_task.html', context)
