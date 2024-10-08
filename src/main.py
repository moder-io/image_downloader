from scraper import *
from downloader import *
from utils import *

def main():
    search_term = input("Ingresa las palabras clave para buscar imágenes: ")
    max_images = int(input("¿Cuántas imágenes deseas descargar? (máximo 20): "))
    
    if max_images > 20:
        print("No se pueden descargar más de 20 imágenes. Inténtalo de nuevo.")
        return
    
    folder_name = f"images/{search_term}"
    create_folder(folder_name)

    print(f"Buscando {max_images} imágenes de '{search_term}'...")
    image_urls = scrape_images(search_term, max_images+1)

    if not image_urls:
        print("No se encontraron imágenes. Saliendo del programa.")
        return
    
    print(f"Comenzando la descarga de {len(image_urls)} imágenes...")
    download_images(image_urls, folder_name, search_term)
    
    print(f"\n¡Descarga completa! Las imágenes están guardadas en la carpeta: {folder_name}")

    # Pregunta si se desea comprimir las imágenes descargadas
    respuesta = input("¿Quieres comprimir las imágenes? (escribe 'y' para aceptar): ")
    if respuesta.lower() == 'y':
        compress_folder(folder_name, folder_name)
        print(f"Carpeta '{folder_name}' comprimida como '{folder_name}.zip'.")
    else:
        print("No se comprimieron las imágenes.")

    input("Pulsa enter para cerrar el programa.")

if __name__ == "__main__":
    main()
