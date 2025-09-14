import numpy as np
import random


def calcular_promedio_temperatura_detallado(datos_temperatura, nombres_ciudades):
    """
    Calcula y muestra la temperatura promedio para cada ciudad, detallada por semana.

    Args:
        datos_temperatura (np.array): La matriz 3D con las temperaturas.
        nombres_ciudades (list): Una lista con los nombres de las ciudades.
    """
    print("Calculando y mostrando los promedios de temperatura detallados:")
    print("=" * 50)

    # Bucle principal para iterar sobre cada ciudad
    for idx_ciudad, nombre_ciudad in enumerate(nombres_ciudades):
        print(f"--- Promedios para {nombre_ciudad} ---")

        # Bucle anidado para iterar sobre cada semana de la ciudad actual
        for idx_semana in range(datos_temperatura.shape[0]):
            # Seleccionamos todos los datos de los 7 días para la semana y ciudad actuales
            temperaturas_semanales = datos_temperatura[idx_semana, idx_ciudad, :]

            # Calculamos el promedio de esa semana
            promedio_semana = np.mean(temperaturas_semanales)

            # Mostramos el resultado
            print(f"> El promedio de la semana {idx_semana + 1} es: {promedio_semana:.2f}°C")

        print("\n")



# Definimos las dimensiones de la matriz 3D
ciudades = ['Quito']
num_ciudades = len(ciudades)
dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
num_dias_semana = len(dias_semana)
num_semanas = 4

#  Crear una matriz 3D para representar los datos y llenarla con valores aleatorios
matriz_temperaturas = np.zeros((num_semanas, num_ciudades, num_dias_semana))

for semana in range(num_semanas):
    for ciudad in range(num_ciudades):
        for dia in range(num_dias_semana):
            matriz_temperaturas[semana, ciudad, dia] = random.randint(15, 30)


# Llamamos a la nueva función con la matriz y la lista de ciudades
calcular_promedio_temperatura_detallado(matriz_temperaturas, ciudades)