import requests
import os

def download_image(url, folder_name, image_name):
    try:
        img_data = requests.get(url, timeout=10).content
        file_path = os.path.join(folder_name, image_name)
        os.makedirs(folder_name, exist_ok=True)
        with open(file_path, 'wb') as handler:
            handler.write(img_data)
        print(f'Imagen {image_name} descargada con éxito')
    except requests.exceptions.Timeout:
        print(f'Error: Tiempo de espera agotado al descargar {url}')
    except requests.exceptions.RequestException as e:
        print(f'Error al descargar {url}: {e}')
    except OSError as e:
        print(f'Error al crear la carpeta o escribir el archivo: {e}')
    except Exception as e:
        print(f'Error inesperado al descargar {url}: {e}')

def download_images(image_urls, folder_name, search_term):
    for idx, url in enumerate(image_urls):
        image_name = f"{search_term}_{idx}.jpg"
        download_image(url, folder_name, image_name) 