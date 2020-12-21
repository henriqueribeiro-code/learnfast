from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ObjectDoesNotExist


class RegisterForm(UserCreationForm):

    email = forms.EmailField(label='E-mail')
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Nome de usuário'
        self.fields['email'].widget.attrs['placeholder'] = 'example@example.com'
        self.fields['email'].widget.attrs['class'] = 'formInput'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Primeiro nome'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Segundo nome'
        self.fields['password1'].widget.attrs['placeholder'] = 'Senha'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirme sua senha'

    class Meta:
        model = User

        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2'            
        )    


    def clean_email(self):
        email = self.cleaned_data.get('email')
        
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email já cadastrado')
        return email

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
