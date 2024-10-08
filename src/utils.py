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