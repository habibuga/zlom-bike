from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator

from .models import Offer, Message

User = get_user_model()


class SearchOffer(forms.Form):
    search_word = forms.CharField(label="", max_length=50,
                                  widget=forms.TextInput(attrs={'placeholder': 'Wpisz coś...'}))
