from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.core import mail
from django.contrib.auth import get_user_model
from django.conf import settings

# from model_mommy import mommy


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
