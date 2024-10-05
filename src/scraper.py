import requests
from bs4 import BeautifulSoup

def scrape_images(search_term, max_images=10):
    search_url = f"https://www.google.com/search?hl=en&tbm=isch&q={search_term}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(search_url, headers=headers)
    
    soup = BeautifulSoup(response.text, 'html.parser')
    images = soup.find_all('img', limit=max_images)
    
    image_urls = []
    for img in images:
        image_urls.append(img['src'])
    
    return image_urls
