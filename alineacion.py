import cv2
import numpy as np
def align_images(image1, image2):
    # Convertir las imágenes a escala de grises
    gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    # Crear el objeto ORB para la detección de puntos clave y descriptores
    orb = cv2.ORB_create()

    # Encontrar puntos clave y descriptores en ambas imágenes
    keypoints1, descriptors1 = orb.detectAndCompute(gray1, None)
    keypoints2, descriptors2 = orb.detectAndCompute(gray2, None)

    # Realizar la correspondencia de puntos clave entre las dos imágenes
    matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = matcher.match(descriptors1, descriptors2)

    # Ordenar las correspondencias por distancia
    matches = sorted(matches, key=lambda x: x.distance)

    # Extraer las coordenadas de los puntos clave coincidentes
    src_points = np.float32([keypoints1[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
    dst_points = np.float32([keypoints2[m.trainIdx].pt for m in matches]).reshape(-1, 1, 2)

    # Calcular la matriz de transformación homográfica
    transformation_matrix, _ = cv2.findHomography(src_points, dst_points, cv2.RANSAC, 5.0)

    # Aplicar la transformación a la segunda imagen
    aligned_image = cv2.warpPerspective(image2, transformation_matrix, (image2.shape[1], image2.shape[0]))

    return aligned_image

# Cargar las imágenes
image1 = cv2.imread("ruta/a/la/imagen1.jpg")
image2 = cv2.imread("ruta/a/la/imagen2.jpg")

# Alinear las imágenes
aligned_image = align_images(image1, image2)

# Mostrar las imágenes originales y la imagen alineada
cv2.imshow("Imagen 1", image1)
cv2.imshow("Imagen 2", image2)
cv2.imshow("Imagen Alineada", aligned_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
