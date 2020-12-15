from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field

class ContactCourseForms(forms.Form):
    name = forms.CharField(label='Nome ', max_length=100)
    email = forms.EmailField(label='E-mail ', max_length=200)
    message = forms.CharField(label='Mensagem/Dúvida ', widget=forms.Textarea)



    helper = FormHelper()
    helper.add_input(Submit('submit', 'Enviar Dúvida', css_class='btn-primary'))
    helper.form_method = 'POST'