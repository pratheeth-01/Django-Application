from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime


# Create your views here.
def index(request):
    return HttpResponse("Hello, this app is working fine!!!")


tasks = ['Learn python basics', 'Setup up django']


def render_page(request):
    return render(request, 'index.html', context={'cur_date': str(datetime.now()), 'tasks': tasks})
