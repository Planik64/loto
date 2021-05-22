from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'label': 'Парола', }),
    )


def clean_email(self):
    email = self.cleaned_data.get('email', False)
    if not email:
        raise forms.ValidationError('Email is required')
    return email


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model=User
        fields = ('email','first_name', 'last_name')
        labels = {
            'email': 'Емайл:',
            'first_name': 'Име:',
            'last_name': 'Фамилия:'
        }
