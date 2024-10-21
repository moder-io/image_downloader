import requests
from bs4 import BeautifulSoup
from urllib.parse import quote

def scrape_images(search_term, max_images, start_page=1, search_engine='google', user_agent=None):
    if search_engine.lower() == 'google':
        search_url = f"https://www.google.com/search?hl=en&q={quote(search_term)}&tbm=isch&start={start_page}"
    else:
        raise ValueError("Solo se admite Google como motor de búsqueda por ahora.")

    headers = {
        "User-Agent": user_agent or "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    try:
        response = requests.get(search_url, headers=headers, timeout=30)
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