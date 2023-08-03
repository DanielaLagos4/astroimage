import cv2

def adjust_contrast(image, alpha, beta):
    # Ajustar el contraste utilizando la transformación lineal
    adjusted_image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

    return adjusted_image

# Cargar la imagen astronómica
image = cv2.imread("C:/Users/lagos/Downloads/PHOTO-2023-04-20-22-56-58.jpg")

# Ajustar el contraste de la imagen
adjusted_image = adjust_contrast(image, alpha=1.5, beta=0)

# Mostrar la imagen original y la imagen con el contraste ajustado
cv2.imshow("Imagen Original", image)
cv2.imshow("Imagen con Contraste Ajustado", adjusted_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
