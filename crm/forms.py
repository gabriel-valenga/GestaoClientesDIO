from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        label='Nome',
        error_messages={'max_length': 'Nome não ´pode ter mais de 150 caracteres.'}
    )
    email = forms.EmailField(label='Email')
    username = forms.CharField(
        label='Usuario',
        error_messages={'max_length': 'Nome não ´pode ter mais de 150 caracteres.'}
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput,
        label='Senha'
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput,
        label='Confirme a senha'
    )

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'email',
            'password1',
            'password2'
        ]

    def form_valid(self, form):
        return super().form_valid(form)