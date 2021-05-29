from django import urls
from django.contrib.auth import get_user_model
import pytest


@pytest.mark.parametrize('param',[
    ('welcome'),
    ('dashboard'),
    ('login'),
    ('register')
])
def test_render_views(client,param):
    temp_url = urls.reverse(param)
    resp = client.get(temp_url)
    assert resp.status_code == 200

@pytest.mark.django_db
def test_register(client,user_data):
    user_model =get_user_model()
    assert user_model.objects.count()==0
    register_url = urls.reverse('register')
    resp =client.post(register_url,user_data)
    assert user_model.objects.count()==1
    assert resp.status_code==302


@pytest.mark.django_db
def test_login(client,create_test_user,user_data):
    user_model = get_user_model()
    assert user_model.objects.count()==1
    login_urls =urls.reverse('login')
    resp=client.post(login_urls,data=user_data)
    assert resp.status_code == 302
    assert resp.url == urls.reverse('dashboard')

@pytest.mark.django_db
def test_user_logout(client,authenticated_user):
    logout_url =urls.reverse('user_logout')
    resp =client.get(logout_url)
    assert resp.status_code == 302
    assert resp.url == urls.reverse('welcome')