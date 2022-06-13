import pytest
from django.test import Client

from bike_app.models import Offer, Category


@pytest.fixture
def client():
    django_client = Client()
    return django_client


@pytest.fixture
def categories():
    Category.objects.create(name="kategoria testowa", slug="kategoria-testowa")
    Category.objects.create(name="kategoria random", slug="kategoria-random")
    Category.objects.create(name="kategoria dummy", slug="kategoria-dummy")

