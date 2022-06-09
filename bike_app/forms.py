from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from .models import Offer, Message, Profile

User = get_user_model()

DEACTIVATION_CHOICES = (
    (1, "Tak"),
    (2, "Nie"),
)


class SearchOffer(forms.Form):
    search_word = forms.CharField(label="", max_length=50,
                                  widget=forms.TextInput(attrs={'placeholder': 'Wpisz coś...'}))


class NewUserForm(UserCreationForm):
    password1 = forms.CharField(label="Hasło", strip=False, widget=forms.PasswordInput, help_text=None)
    password2 = forms.CharField(label="Potwierdź hasło", strip=False, widget=forms.PasswordInput, help_text=None)
    location = forms.CharField(label="Lokalizacja")
    tel_num = forms.IntegerField(label="Numer telefonu")

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")
        labels = {
            "username": "Login",
            "first_name": "Imie",
            "last_name": "Nazwisko",
            "email": "Email",
        }
        help_texts = {
            "username": None
        }


class LoginForm(forms.Form):
    username = forms.CharField(label='Login')
    password = forms.CharField(label='Hasło', widget=forms.PasswordInput)


class ResetPasswordForm(forms.ModelForm):
    password2 = forms.CharField(label='Powtórz hasło', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('password',)
        widgets = {
            'password': forms.PasswordInput
        }
        labels = {
            "password": "Hasło"
        }

    def clean(self):
        cd = super().clean()

        password1 = cd['password']
        password2 = cd['password2']

        if password1 != password2:
            raise ValidationError("Hasła są różne!")


class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")
        labels = {
            "first_name": "Imie",
            "last_name": "Nazwisko",
            "email": "Email",
        }


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("location", "tel_num")
        labels = {
            "location": "Lokalizacja",
            "tel_num": "Numer telefonu"
        }


class OfferDeactivationForm(forms.Form):
    answer = forms.ChoiceField(label="", choices=DEACTIVATION_CHOICES, widget=forms.RadioSelect)
