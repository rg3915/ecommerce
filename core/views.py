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


def contact(request):
    success = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            message = 'Nome: {0}\nE-mail:{1}\n{2}'.format(name, email, message)
            send_mail(
                'Contato do Django E-Commerce',
                message,
                settings.DEFAULT_FROM_EMAIL,
                [settings.DEFAULT_FROM_EMAIL]
            )
            success = True
    else:
        form = ContactForm()
    context = {
        'form': form,
        'success': success
    }
    return render(request, 'contact.html', context)
