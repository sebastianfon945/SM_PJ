import os
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from django.conf import settings
from .models import Image
import time
from retrying import retry


@retry(stop_max_attempt_number=2, wait_fixed=2000)
def get_image_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except Exception:
        raise ValueError("Image can't be downloaded")


def download_image(image_data, image_name, path):
    try:
        url = image_data["message"]
        response = requests.get(url)
        response.raise_for_status()
        with open(os.path.join(path, image_name), 'wb') as file:
            file.write(response.content)
        print(f"Downloading {image_name}")
        Image.objects.create(url=url,
                             name=image_name,
                             status=image_data["status"])
        return {"name": image_name,
                "url": url}

    except requests.exceptions.RequestException as e:
        raise ValueError(f"Error while downloading {image_name}: {e}")


def download_image_thread(api_url, path, n_downloads):
    if not os.path.exists(path):
        os.makedirs(path)

    future_results = []
    downloaded_images = []

    with ThreadPoolExecutor(max_workers=20) as executor:
        for i in range(n_downloads):
            image_data = get_image_url(api_url)
            if image_data:
                image_name = f"imagen_{i}.jpg"
                future_image = executor.submit(download_image, image_data,
                                               image_name, path)
                future_results.append(future_image)

        for future_image in as_completed(future_results):
            result = future_image.result()
            if result:
                downloaded_images.append(result)

    return downloaded_images


def start_download(n_downloads=15):
    api_url = 'https://dog.ceo/api/breeds/image/random'
    path = os.path.join(settings.MEDIA_ROOT,
                        'images')
    start_time = time.time()
    downloaded_images = download_image_thread(api_url, path, n_downloads)
    end_time = time.time()
    execution_time = end_time - start_time
    response = {
        'dowloaded_images': downloaded_images,
        'execution_time': execution_time
    }
    return response
