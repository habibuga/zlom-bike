import pytest
from .models import Category


@pytest.mark.django_db
def test_category_view(client, categories, db):
    response = client.get("/")
    assert response.status_code == 200
    cat_list = []
    for category in response.context['categories']:
        cat_list.append(category)
    assert len(cat_list) == 3
