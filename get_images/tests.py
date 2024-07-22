import pytest
from .models import Image
import os
from django.conf import settings
from .views import (
    get_image_url,
    download_image,
    download_image_thread,
    start_download,
    )


@pytest.mark.django_db
def test_add_image():
    imagen = Image.objects.create(url='https://example.com/image.jpg',
                                  name='test_image')
    assert imagen.url == 'https://example.com/image.jpg'
    assert imagen.name == 'test_image'


@pytest.mark.django_db
def test_get_image_url():
    api_url = 'https://dog.ceo/api/breeds/image/random'
    result = get_image_url(api_url)
    assert result['message']
    assert result['status']


@pytest.mark.django_db
def test_download_image():
    api_url = 'https://dog.ceo/api/breeds/image/random'
    image_data = get_image_url(api_url)
    assert image_data
    path = os.path.join(settings.MEDIA_ROOT, 'images')
    if not os.path.exists(path):
        os.makedirs(path)
    download_image(image_data, "test_image.jpg", path)
    image = Image.objects.first()
    assert image_data
    assert image.url == image_data['message']
    assert image.status == image_data['status']


@pytest.mark.django_db
def test_download_image_thread():
    api_url = 'https://dog.ceo/api/breeds/image/random'
    path = os.path.join(settings.MEDIA_ROOT, 'images')
    if not os.path.exists(path):
        os.makedirs(path)
    downloaded_images = download_image_thread(api_url, path, 20)
    assert len(downloaded_images) == 20
    assert len(Image.objects.all()) == 20


@pytest.mark.django_db
def test_start_download():
    response = start_download(20)
    assert len(response) == 2
    assert len(response['dowloaded_images']) == 20
    assert response['execution_time']
