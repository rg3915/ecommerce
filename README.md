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
mixer.cycle(5).blend(User)
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

