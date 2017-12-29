from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View, TemplateView, CreateView
from catalog.models import Category
from core.forms import ContactForm

User = get_user_model()


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


class IndexView(View):

    def get(self, request):
        return render(request, 'index.html')


class IndexView(TemplateView):
    template_name = 'index.html'


# index = IndexView()
index = IndexView.as_view()


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


class RegisterView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('index')

register = RegisterView.as_view()
