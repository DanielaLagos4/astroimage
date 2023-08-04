# Importar las funciones necesarias del paquete AstroImage
from astroimage.align import align_images
from astroimage.stack import stack_images
from astroimage.detection import detect_objects

# Cargar las imágenes astronómicas (suponiendo que están en formato numpy arrays)
image1 = load_image("C:/Users/lagos/Downloads/space-331.jpg")
image2 = load_image("C:/Users/lagos/Downloads/space-331.jpg")
image3 = load_image("C:/Users/lagos/Downloads/space-331.jpg")

# Alinear las imágenes utilizando la función register_translation
aligned_images = align_images([image1, image2, image3])

# Apilar las imágenes alineadas utilizando la función stack_images
stacked_image = stack_images(aligned_images, method='mean')

# Detectar objetos en la imagen apilada utilizando la función detect_objects
detected_objects = detect_objects(stacked_image, threshold=0.5)

# Imprimir las coordenadas de los objetos detectados
for obj in detected_objects:
    print(f"Objeto detectado en coordenadas (x, y): ({obj[0]}, {obj[1]})")
