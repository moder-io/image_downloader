import requests

def download_image(url, folder_name, image_name):
    try:
        img_data = requests.get(url).content
        with open(f'{folder_name}/{image_name}', 'wb') as handler:
            handler.write(img_data)
        print(f'Imagen {image_name} descargada con éxito')
    except Exception as e:
        print(f'Error al descargar {url}: {e}')

def download_images(image_urls, folder_name, search_term):
    for idx, url in enumerate(image_urls):
        image_name = f"{search_term}_{idx}.jpg"
        download_image(url, folder_name, image_name) 
