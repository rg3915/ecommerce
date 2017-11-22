from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello World')


def index(request):
    texts = ['Lorem ipsum dolor sit amet', 'consectetur adipisicing elit',
             'sed do eiusmod tempor incididunt ut labore et dolore magna aliqua']
    context = {
        'title': 'django e-commerce',
        'texts': texts
    }
    return render(request, 'index.html', context)
