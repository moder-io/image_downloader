import requests
from bs4 import BeautifulSoup

def scrape_images(search_term, max_images):    
    search_url = f"https://www.google.com/search?hl=en&q={search_term}&tbm=isch" 
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    
    try:
        response = requests.get(search_url, headers=headers)
        response.raise_for_status() 
    except requests.exceptions.RequestException as e:
        print(f"Error al hacer la solicitud HTTP: {e}")
        return []
    
    soup = BeautifulSoup(response.text, 'html.parser')
    image_tags = soup.find_all('img', limit=max_images)
    
    image_urls = []
    for img in image_tags:
        img_url = img.get('src')
        if img_url:
            image_urls.append(img_url)
    
    if not image_urls:
        print("No se encontraron imágenes.")
    else:
        print(f"Se encontraron {len(image_urls)} imágenes.")
    
    return image_urls
