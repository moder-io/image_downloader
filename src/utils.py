import os
import shutil

def create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        print(f"Carpeta '{folder_name}' creada.")
    else:
        print(f"Carpeta '{folder_name}' ya existe.")

def compress_folder(folder_name, output_zip):
    """Comprime la carpeta en un archivo .zip."""
    if os.path.exists(folder_name):
        shutil.make_archive(output_zip, 'zip', folder_name)
        print(f"Carpeta '{folder_name}' comprimida como '{output_zip}.zip'.")
    else:
        print(f"Carpeta '{folder_name}' no existe.")

def list_images(folder_name):
    """Lista las imágenes en la carpeta especificada."""
    if os.path.exists(folder_name):
        image_files = [f for f in os.listdir(folder_name) if f.endswith(('.jpg', '.png', '.gif', '.bmp'))]
        for image_file in image_files:
            print(image_file)
    else:
        print(f"La carpeta '{folder_name}' no existe.")