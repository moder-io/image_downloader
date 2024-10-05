from scraper import scrape_images
from downloader import download_images
from utils import create_folder

def main():
    search_term = input("Ingresa las palabras clave para buscar imágenes: ")
    max_images = int(input("¿Cuántas imágenes deseas descargar? "))
    folder_name = f"images/{search_term}"
    create_folder(folder_name)
    image_urls = scrape_images(search_term, max_images+1)
    download_images(image_urls, folder_name, search_term)
    print(f"\n¡Descarga completa! Las imágenes están guardadas en la carpeta: {folder_name}")

if __name__ == "__main__":
    main()