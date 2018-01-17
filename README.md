# ecommerce
Django E-Commerce Trainning


## Shell

```
python manage.py shell

from core.forms import ContactForm
form = ContactForm()
form.as_p()
data = {'name': 'Seu Nome', 'email': 'contact@'}
form = ContactForm(data)
form.is_valid()
form.errors
```

### Populando o banco com [mixer](https://github.com/klen/mixer)

```
./manage.py shell_plus
from mixer.backend.django import mixer
from django.utils.text import slugify
mixer.cycle(5).blend(User)
categories = ['Cursos', 'Livros', 'Videos']
for category in categories:
    cat = Category.objects.create(name=category, slug=slugify(category))
    mixer.cycle(5).blend(Product, category=cat)
```

### Paginação

```
from django.core.paginator import Paginator
from catalog.models import Product
paginator = Paginator(Product.objects.all(), 3)
paginator.num_pages
page_obj = paginator.page(2)
page_obj.object_list
```


### Formset Factory

```
from checkout.models import CartItem
from django.forms import modelformset_factory
CartItemFormSet = modelformset_factory(CartItem, fields=['quantity'], extra=0, can_delete=True)
formset = CartItemFormSet(queryset=CartItem.objects.all())
form = formset[0]
print(formset)
```