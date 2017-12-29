from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from catalog.models import Category
from core.forms import ContactForm


def index(request):
    return HttpResponse('Hello World')


def index(request):
    texts = ['Lorem ipsum dolor sit amet', 'consectetur adipisicing elit',
             'sed do eiusmod tempor incididunt ut labore et dolore magna.']
    context = {
        'title': 'django e-commerce',
        'texts': texts
    }
    return render(request, 'index.html', context)


def index(request):
    return render(request, 'index.html')


class IndexView(object):

    def __call__(self, request):
        return render(request, 'index.html')

index = IndexView()


def contact(request):
    success = False
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.send_mail()
        success = True
    context = {
        'form': form,
        'success': success
    }
    return render(request, 'contact.html', context)
