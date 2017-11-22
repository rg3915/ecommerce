from django.conf.urls import url
from catalog import views as cat


urlpatterns = [
    url(r'^$', cat.product_list, name='product_list'),
    url(r'^(?P<slug>[\w_-]+)/$', cat.category, name='category'),
    # url(r'^produto/$', cat.product, name='product'),
]
