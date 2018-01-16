from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from core import views as c

urlpatterns = [
    url(r'^$', c.index, name='index'),
    url(r'^contato/$', c.contact, name='contact'),
    url(
        r'^entrar/$',
        login,
        {'template_name': 'login.html'},
        name='login'
    ),
    url(r'^sair/$', logout, {'next_page': 'index'}, name='logout'),
    # url(r'^registro/$', c.register, name='register'),
    url(r'^catalogo/', include('catalog.urls', namespace='catalog')),
    url(r'^conta/', include('accounts.urls', namespace='accounts')),
    url(r'^compras/', include('checkout.urls', namespace='checkout')),
    url(r'^admin/', admin.site.urls),
]
