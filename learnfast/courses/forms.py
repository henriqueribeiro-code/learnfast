from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from django.conf import settings
from django.core.mail import send_mail

class ContactCourseForms(forms.Form):
    name = forms.CharField(label='Nome ', max_length=100)
    email = forms.EmailField(label='E-mail ', max_length=200)
    message = forms.CharField(label='Mensagem/Dúvida ', widget=forms.Textarea)

    helper = FormHelper()
    helper.add_input(Submit('submit', 'Enviar Dúvida', css_class='btn-primary'))
    helper.form_method = 'POST'

    def send_email(self, course):
        subject = f"{course} Nome"
        message = f"Nome: {self.cleaned_data['name']} | \n Email: {self.cleaned_data['email']} | \nMessage: {self.cleaned_data['message']}"
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [settings.CONTACT_EMAIL]
        )
