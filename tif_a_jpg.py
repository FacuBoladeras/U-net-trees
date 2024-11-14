import rasterio
from PIL import Image
import numpy as np

# Ruta del archivo TIFF
tiff_path = r"C:\Users\Facu\Downloads\Sentinel2_Annual_Median_2022.tif"
png_path = r"C:\Users\Facu\Downloads\Sentinel2_Annual_Median_2022.png"

# Abrir el archivo TIFF con rasterio
with rasterio.open(tiff_path) as src:
    # Leer los datos de la primera banda como un array de numpy
    array = src.read(1)

# Calcular los percentiles 2 y 98 para mejorar el contraste
p2, p98 = np.percentile(array, (2, 98))

# Escalar los valores al rango 0-255 usando estos percentiles
array = np.clip(array, p2, p98)  # Limitar al rango percentil
array = (255 * (array - p2) / (p98 - p2)).astype(np.uint8)  # Normalizar

# Crear una imagen usando Pillow y guardar en PNG
image = Image.fromarray(array)
image.save(png_path, format="PNG")

print("Imagen convertida y guardada como PNG con ajuste de contraste.")
