from django.conf.urls import include, url
from django.contrib import admin
from core import views as c

urlpatterns = [
    url(r'^$', c.index, name='index'),
    url(r'^contato/$', c.contact, name='contact'),
    url(r'^produtos/', include('catalog.urls', namespace='catalog')),
    url(r'^admin/', admin.site.urls),
]
