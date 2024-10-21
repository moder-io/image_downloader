import argparse
import os
from scraper import scrape_images
from downloader import download_images
from utils import create_folder, compress_folder

def main():
    parser = argparse.ArgumentParser(description='Descargador de imágenes')
    parser.add_argument('--search-term', type=str, required=True, help='Palabras clave para buscar imágenes')
    parser.add_argument('--max-images', type=int, default=20, help='Número máximo de imágenes a descargar (máximo 20)')
    parser.add_argument('--output-folder', type=str, default='images', help='Carpeta de salida para las imágenes')
    parser.add_argument('--compress', action='store_true', help='Comprimir la carpeta de imágenes después de la descarga')
    args = parser.parse_args()

    if args.max_images > 20:
        print("No se pueden descargar más de 20 imágenes. Inténtalo de nuevo.")
        return

    folder_name = os.path.join(args.output_folder, args.search_term)
    create_folder(folder_name)

    print(f"Buscando {args.max_images} imágenes de '{args.search_term}'...")
    image_urls = scrape_images(args.search_term, args.max_images + 1)

    if not image_urls:
        print("No se encontraron imágenes. Saliendo del programa.")
        return

    print(f"Comenzando la descarga de {len(image_urls)} imágenes...")
    download_images(image_urls, folder_name, args.search_term)
    print(f"\n¡Descarga completa! Las imágenes están guardadas en la carpeta: {folder_name}")

    if args.compress:
        compress_folder(folder_name, folder_name)
        print(f"Carpeta '{folder_name}' comprimida como '{folder_name}.zip'.")

if __name__ == "__main__":
    main()