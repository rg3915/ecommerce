from django.conf.urls import url
from catalog import views as cat


urlpatterns = [
    # url(r'^produto/$', cat.product, name='product'),
    url(r'^$', cat.product_list, name='product_list'),
]
