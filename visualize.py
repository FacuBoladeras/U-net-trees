from PIL import Image
import matplotlib.pyplot as plt

# Ruta de la imagen PNG
image_path = r"C:\Users\Facu\Documents\MATLAB\PixelLabelData\pixelLabelData\Label_1_Sentinel2_Annual_Median_2022.png"

# Abrir la imagen con Pillow
image = Image.open(image_path)

# Mostrar la imagen con matplotlib
plt.imshow(image)
plt.axis('off')  # Ocultar los ejes para una visualización más limpia
plt.title('Imagen PNG')
plt.show()
