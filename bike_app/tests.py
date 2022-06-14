import pytest

from django.contrib.auth.models import User

@pytest.mark.django_db
def test_category_view(client, categories, db):
    response = client.get("/")
    assert response.status_code == 200
    cat_list = []
    for category in response.context['categories']:
        cat_list.append(category)
    assert len(cat_list) == 3


@pytest.mark.django_db
def test_user_detail_view(client, test_user, db):
    response = client.get('/moj_profil/')
    assert response.status_code == 200 or response.status_code == 302


@pytest.mark.django_db
def test_user_detail_update(client, test_user, db):
    response = client.post('/zmien_dane/', {"first_name": "first_tester", "last_name": "last_tester",
                                            "email": "tester@tester.com"})
    assert response.status_code == 200 or response.status_code == 302
    # user_tester = User.objects.get(username="Tester")
    # assert user_tester.first_name == "first_tester" and user_tester.last_name == "last_tester" \
    #        and user_tester.email == "tester@tester.com"
