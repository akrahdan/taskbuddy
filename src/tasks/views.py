from django.urls import reverse
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import Task
from .forms import TaskForm
def taskview(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        print("User:", request.user)
        if form.is_valid():
           form.instance.owner = request.user
           form.save()
          
           
    else:
        form = TaskForm()
    return render(request, "tasks/task.html",{ "form": form} )

def task_update(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        raise Http404
        
    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('task_all'))
    return render(request, "tasks/edit.html", { "form": form} )
        
def listview(request):
    tasks = Task.objects.all()

    return render(request, "tasks/list.html", {"tasks": tasks})



