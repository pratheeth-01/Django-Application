from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from django.shortcuts import render, redirect
from .models import Task
from .forms import ContactForm, TaskForm

# Create your views here.
from django.views.generic import RedirectView


def index(request):
    return HttpResponse("Hello, this app is working fine!!!")


tasks = ['Learn python basics', 'Setup up django']


def render_page(request):
    return render(request, 'index.html', context={'cur_date': str(datetime.now()), 'tasks': tasks})


# URL Redirection in django
def redirect_view(request):
    return redirect('https://www.google.com/')


class RedirectPage(RedirectView):
    url = 'https://www.google.com/'


class Redirect(RedirectView):
    urlA = 'https://www.google.com/'
    urlB = 'cars'
    url = '{}{}'.format(urlA, urlB)


def render_tasks(request):
    tasks_list = Task.objects.all()
    return render(request, 'tasks.html', {'tasks': tasks_list})


def add_task(request):
    if request.method == 'POST':
        content = request.POST['content']
        deadline = request.POST['deadline']
        task = Task(content=content, deadline=deadline)
        task.save()
        return redirect('tasks_list')
    else:
        return render(request, 'new_task.html')


def add_task_new(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = form.save()
            return redirect('tasks_list')
    else:
        form = TaskForm()
    return render(request, 'add_task_new.html', {'form': form})


def contact(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message']
        email = request.POST['email']
        # Send an email
        return redirect('tasks_list')
    else:
        return render(request, 'contact_us.html')


def contact_new(request):
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            return redirect('tasks_list')

    else:
        form = ContactForm()
    return render(request, 'contact_us_new.html', {'form': form})
