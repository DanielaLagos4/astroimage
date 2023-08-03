# astroimage
El paquete AstroImage es una herramienta de procesamiento de imágenes astronómicas desarrollada en Python. Este paquete proporciona una serie de funciones y módulos diseñados para facilitar tareas comunes en el procesamiento y análisis de imágenes astronómicas.

astroimage.align
register_translation
Esta función utiliza el algoritmo de correlación cruzada para calcular el desplazamiento (traslación) entre dos imágenes. Es útil para alinear imágenes que pueden haber sufrido pequeños movimientos o desplazamientos entre ellas. La función toma como entrada dos imágenes image1 y image2 y devuelve las coordenadas shift que representan el desplazamiento requerido para alinear image2 con respecto a image1.

align_images
Esta función toma una lista de imágenes y utiliza la función register_translation para alinear todas las imágenes de la lista con respecto a una imagen de referencia (generalmente la primera imagen de la lista). Devuelve una nueva lista de imágenes alineadas.

astroimage.stack
stack_images
Esta función permite apilar imágenes astronómicas para mejorar la calidad y aumentar la señal. Toma una lista de imágenes y, mediante un método especificado (method='mean' para promedio o method='sum' para suma), combina los valores de píxeles de las imágenes para formar una imagen apilada. Es útil para resaltar características astronómicas débiles y mejorar la detección de objetos celestiales.

astroimage.noise
subtract_background
Esta función toma una imagen y realiza una sustracción de fondo para eliminar la contribución del fondo o el ruido de lectura. Se utiliza para reducir el ruido en las imágenes astronómicas y resaltar objetos celestiales de interés.

astroimage.contrast
adjust_contrast
Esta función ajusta el contraste de una imagen astronómica utilizando la técnica de estiramiento lineal del histograma. Esto resalta los detalles importantes y facilita la visualización y el análisis de características astronómicas.

astroimage.detection
detect_objects
Esta función detecta objetos astronómicos en una imagen utilizando el algoritmo de umbralización adaptativa y técnicas de segmentación. Devuelve una lista de coordenadas que representan la posición de los objetos detectados.

astroimage.measurement
measure_properties
Esta función mide las propiedades de los objetos astronómicos detectados en una imagen, como la posición, el brillo y el tamaño. Utiliza las coordenadas de los objetos obtenidas con la función detect_objects y devuelve una lista de propiedades medidas para cada objeto.
