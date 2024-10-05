import os

def create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        print(f"Carpeta '{folder_name}' creada.")
    else:
        print(f"Carpeta '{folder_name}' ya existe.")
