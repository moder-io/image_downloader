# Image Downloader Project

Este es un script en Python que permite descargar imágenes desde la web basadas en palabras clave proporcionadas por el usuario. Las imágenes se organizan automáticamente en carpetas.

## Características
- Búsqueda de imágenes en Google basadas en palabras clave.
- Descarga automática de las imágenes.
- Organización de las imágenes en carpetas específicas.
- Capacidad para descargar un maximo de 20 imágenes por búsqueda.

## Requisitos
- Python 3.x
- Bibliotecas listadas en `requirements.txt`

## Instalación
1. Clona este repositorio:
   ```bash
   git clone https://github.com/moder-io/image_downloader.git
   ```

2. Navega al directorio del proyecto:
   ```bash
   cd image_downloader
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Uso
1. Ejecuta el archivo run.bat (en Windows) o ejecuta el script principal directamente:
   ```bash
   python main.py
   ```

2. Sigue las instrucciones en pantalla para ingresar las palabras clave y el número de imágenes que deseas descargar.

3. Las imágenes se guardarán en una carpeta con el nombre de la búsqueda dentro del directorio `images`.