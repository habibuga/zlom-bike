import pytest
from .models import Offer


@pytest.mark.django_db
def test_offer_view(client, offer, db):
    offer_id = offer.pk
    response = client.get("offer_detail", pk=offer_id)

