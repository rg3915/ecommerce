from django.db import models
from django.core.urlresolvers import reverse


class Category(models.Model):
    name = models.CharField('nome', max_length=100)
    slug = models.SlugField('identificador', max_length=100)
    created = models.DateTimeField('criado em', auto_now_add=True)
    modified = models.DateTimeField('modificado em', auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog:category', kwargs={'slug': self.slug})


class Product(models.Model):
    name = models.CharField('nome', max_length=100)
    slug = models.SlugField('identificador', max_length=100)
    category = models.ForeignKey('catalog.Category', verbose_name='categoria')
    description = models.TextField('descrição', blank=True)
    price = models.DecimalField('preço', decimal_places=2, max_digits=10)
    created = models.DateTimeField('criado em', auto_now_add=True)
    modified = models.DateTimeField('modificado em', auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'produto'
        verbose_name_plural = 'produtos'

    def __str__(self):
        return self.name
