import rasterio
from rasterio.io import MemoryFile
import numpy as np
from PIL import Image

def georeference_png_from_tif(tif_path, png_path, output_path):
    """
    Georreferencia un archivo PNG utilizando un archivo TIFF como referencia.

    Args:
        tif_path (str): Ruta al archivo TIFF georreferenciado.
        png_path (str): Ruta al archivo PNG no georreferenciado.
        output_path (str): Ruta donde se guardará el archivo TIFF georreferenciado generado.

    Returns:
        None
    """
    # Leer la geoinformación del TIFF
    with rasterio.open(tif_path) as src:
        profile = src.profile
        transform = src.transform
        crs = src.crs

    # Leer el archivo PNG y convertirlo a un array NumPy
    img = Image.open(png_path)
    img_array = np.array(img)

    # Asegurarse de que la imagen tenga solo un canal (si es necesario)
    if img_array.ndim == 3 and img_array.shape[2] in [3, 4]:  # RGB o RGBA
        img_array = img_array[:, :, 0]  # Usar solo un canal (modificar según necesidad)

    # Actualizar el perfil para el nuevo archivo
    profile.update(
        dtype=rasterio.uint8,
        count=1,
        compress='lzw',
        nodata=None,
        transform=transform,
        crs=crs,
        height=img_array.shape[0],
        width=img_array.shape[1]
    )

    # Escribir el archivo georreferenciado
    with rasterio.open(output_path, 'w', **profile) as dst:
        dst.write(img_array, 1)  # Escribir el array en el primer canal

    print(f"Archivo georreferenciado guardado en: {output_path}")

tif_path = r"C:\Users\Facu\Downloads\Sentinel2_Annual_Median_2022.tif"  # Ruta al archivo TIFF
png_path = r"C:\Users\Facu\Desktop\Deep learning pruebas\Label_1_Sentinel2_Annual_Median_2022.png"      # Ruta al archivo PNG
output_path = r"C:\Users\Facu\Desktop\georeferenciada2.tiff"  # Ruta para guardar el archivo TIFF georreferenciado

georeference_png_from_tif(tif_path, png_path, output_path)
