from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='nome')
    email = forms.EmailField(label='e-mail')
    message = forms.CharField(label='mensagem', widget=forms.Textarea())
