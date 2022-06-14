import pytest
from django.test import Client

from bike_app.models import Offer, Category
from django.contrib.auth.models import User


@pytest.fixture
def client():
    django_client = Client()
    return django_client


@pytest.fixture
def categories():
    Category.objects.create(name="kategoria testowa", slug="kategoria-testowa")
    Category.objects.create(name="kategoria random", slug="kategoria-random")
    Category.objects.create(name="kategoria dummy", slug="kategoria-dummy")


@pytest.fixture
def test_user():
    user_tester = User.objects.create(username="Tester")


# @pytest.fixture
# def offer():
#     Offer.objects.create(name="jakaś oferta", description="jakiś opis", price=99.9,
#                          category=Category.objects.get(slug="kategoria-testowa"),
#                          user=User.objects.get(username="Tester")
