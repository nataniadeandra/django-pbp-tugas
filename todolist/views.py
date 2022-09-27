from datetime import date
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from todolist.forms import TaskForm
from todolist.models import Task
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_todolist = Task.objects.filter(user=request.user)

    context = {
        "username": request.user,
        "todolist": data_todolist,
    }

    return render(request, "todolist.html", context)
    

def create_task(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TaskForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            instance = form.save(commit=False)
            instance.user = request.user
            instance.date = date.today()
            instance.save()
            # redirect to a new URL:
            return redirect('todolist:show_todolist')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TaskForm()

    context = {
        'form': form,
    }

    return render(request, 'create_task.html', context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todolist:show_todolist')
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('todolist:login')

def display_finished(request, id):
    task = Task.objects.get(user=request.user, id=id)
    task.is_finished = not task.is_finished
    task.save(update_fields = ['is_finished'])
    return HttpResponseRedirect(reverse("todolist:show_todolist"))

def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return HttpResponseRedirect(reverse("todolist:show_todolist"))
