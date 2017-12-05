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