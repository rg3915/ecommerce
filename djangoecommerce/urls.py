from django.conf.urls import url
from django.contrib import admin
from core import views as core
from catalog import views as cat


urlpatterns = [
    url(r'^$', core.index, name='index'),
    url(r'^contato/$', core.contact, name='contact'),
    url(r'^produto/$', cat.product, name='product'),
    url(r'^produtos/$', cat.product_list, name='product_list'),
    url(r'^admin/', admin.site.urls),
]
