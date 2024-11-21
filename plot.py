from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

def plot_three_pngs_with_titles(png_paths, titles, colormaps=None):
    """
    Plotea hasta 3 archivos PNG, cada uno con su propio colormap y título personalizado.

    Args:
        png_paths (list): Lista con rutas a los archivos PNG (máximo 3).
        titles (list): Lista con los títulos para cada imagen.
        colormaps (list or None): Lista con los nombres de los colormaps para cada PNG.
                                  Si es None, se usa 'viridis' por defecto.

    Returns:
        None
    """
    if len(png_paths) > 3:
        raise ValueError("La función admite un máximo de 3 archivos PNG.")
    
    if colormaps is None:
        colormaps = ['viridis'] * len(png_paths)  # Usar 'viridis' por defecto

    if len(colormaps) != len(png_paths) or len(titles) != len(png_paths):
        raise ValueError("El número de colormaps y títulos debe coincidir con el número de imágenes.")

    # Leer los archivos PNG
    png_arrays = [np.array(Image.open(png_path)) for png_path in png_paths]

    # Configurar el plot
    plt.figure(figsize=(15, 5))
    
    for i, png_array in enumerate(png_arrays):
        plt.subplot(1, 3, i + 1)
        plt.imshow(png_array, cmap=colormaps[i])
        plt.title(titles[i])  # Títulos personalizados
        plt.axis("on")
    
    # Mostrar el plot
    plt.tight_layout()
    plt.show()

# Rutas a los PNGs
png_paths = [
    r"C:\Users\Facu\Desktop\img_google.png",
    r"C:\Users\Facu\Desktop\realmask.png",
    r"C:\Users\Facu\Desktop\img_predict.png"
]

# Títulos personalizados
titles = ["Image", "Real mask", "Prediction"]

# Opcional: Define colormaps diferentes para cada PNG
colormaps = ['gray', 'plasma', 'viridis']

# Llamar a la función
plot_three_pngs_with_titles(png_paths, titles, colormaps)

