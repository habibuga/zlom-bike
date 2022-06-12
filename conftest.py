import pytest
from django.test import Client

from bike_app.models import Offer, Category, User


@pytest.fixture
def client():
    django_client = Client()
    return django_client


@pytest.fixture
def offer():
    return Offer.objects.create(name="dummy czesc", description="jakis opis", price=99.9,
                                category=Category.objects.get(pk=1), user=User.objects.get(pk=1))
