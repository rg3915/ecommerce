from django.conf import settings
from django.contrib.auth import get_user_model
from django.core import mail
from django.core.urlresolvers import reverse
from django.test import TestCase, Client
from model_mommy import mommy

User = get_user_model()


class IndexViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('index')

    def tearDown(self):
        pass

    def test_status_code(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)

    def test_template_used(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'index.html')


class ContactViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('contact')

    def test_status_code(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)

    def test_template_used(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'contact.html')

    def test_form_error(self):
        data = {'name': '', 'message': '', 'email': ''}
        response = self.client.post(self.url, data)
        self.assertFormError(response, 'form', 'name',
                             'Este campo é obrigatório.')
        self.assertFormError(response, 'form', 'email',
                             'Este campo é obrigatório.')
        self.assertFormError(response, 'form', 'message',
                             'Este campo é obrigatório.')

    def test_form_ok(self):
        data = {'name': 'test', 'message': 'test', 'email': 'test@email.com'}
        response = self.client.post(self.url, data)
        self.assertTrue(response.context['success'])
        self.assertEquals(len(mail.outbox), 1)
        self.assertEquals(mail.outbox[0].subject,
                          'Contato do Django E-Commerce')


class LoginViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('login')
        self.user = mommy.prepare(settings.AUTH_USER_MODEL)
        self.user.set_password('demodemo')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_status_code(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)

    def test_template_used(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'login.html')

    def test_login_ok(self):
        data = {'username': self.user.username, 'password': 'demodemo'}
        response = self.client.post(self.url, data)
        redirect_url = reverse(settings.LOGIN_REDIRECT_URL)
        self.assertRedirects(response, redirect_url)
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_login_error(self):
        data = {'username': self.user.username, 'password': '1234'}
        response = self.client.post(self.url, data)
        error_msg = ('Por favor, entre com um usuário  e senha corretos.'
                     ' Note que ambos os campos diferenciam maiúsculas e minúsculas.')
        self.assertFormError(response, 'form', None, error_msg)


class RegisterViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register')

    def test_register_ok(self):
        data = {
            'username': 'regis',
            'password1': 'demodemo',
            'password2': 'demodemo'
        }
        response = self.client.post(self.register_url, data)
        index_url = reverse('index')
        self.assertRedirects(response, index_url)
        # Verifica se existe o usuário.
        self.assertEquals(User.objects.count(), 1)
