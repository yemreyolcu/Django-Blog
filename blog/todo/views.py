from django.shortcuts import render, redirect, get_object_or_404,reverse
from .models import todoForm
from .forms import todoform
from django.contrib import messages

# Create your views here.

def showtodo(request):
    todolist = todoForm.objects.all()
    context = {
        "todolist":todolist
    }
    return render(request,"todos/todo.html",context)

def createtodo(request):
    form = todoform(request.POST or None)
    if form.is_valid():
        todo = form.save()
        messages.success(request,"TODO has created!")
        return redirect("showtodo")
    context = {
        "form":form
    }
    return render(request,"todos/create.html",context)
def updatetodo(request,id):
    update_todo = get_object_or_404(todoForm,id=id)
    form = todoform(request.POST or None, instance=update_todo)
    if form.is_valid():
        update_todo.save()
        messages.success(request,"TO-DO has upgraded successfully!")
        return redirect("showtodo")
    context = {
        "form":form
    }
    return render(request,"todos/update.html",context)
def deltodo(request,id):
    remove_todo = get_object_or_404(todoForm,id=id)
    remove_todo.delete()
    messages.success(request,"Well done!")
    return redirect("showtodo")

