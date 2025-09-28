# Objetivo: Utilizar diccionarios en Python para representar información estructurada
# y realizar operaciones comunes

# 1. Crear un Diccionario:
# Crea un diccionario llamado 'informacion_personal' con datos ficticios.
# Debe incluir al menos las claves 'nombre', 'edad', 'ciudad' y 'profesion'.
informacion_personal = {
    "Nombre": "TAYLOR SAMUEL PONCE",
    "Edad": 20,
    "Ciudad": "LOJA",
    "Profesion": "FARMACEUTICO"
}

print("--- Paso 1: Diccionario Inicial ---")
print(informacion_personal)
print("-" * 30)

# 2. Acceder y Modificar Valores:
# Accede al valor asociado con la clave 'ciudad' y modifícalo con una ciudad diferente.
# Vamos a cambiar la ciudad de "LOJA" a "QUITO".
print("--- Paso 2: Modificar Valores ---")
informacion_personal["Ciudad"] = "QUITO"
print(f"Ciudad modificada a: {informacion_personal['Ciudad']}")


print("-" * 30)


# 3. Verificar Existencia de Claves:
# Verifica si la clave "telefono" existe en el diccionario.
print("--- Paso 3: Verificar y Agregar Clave ---")
if "Telefono" not in informacion_personal:
    # Si no existe, agrégala con un número de teléfono ficticio.
    informacion_personal["Telefono"] = "0991234567"
    print("La clave 'Telefono' no existía y fue agregada.")
else:
    print("La clave 'Telefono' ya existía.")

print("-" * 30)


# 4. Eliminar una Clave:
# Elimina la clave "edad" del diccionario.
print("--- Paso 4: Eliminar Clave ---")
# Usamos 'del' para eliminar la clave "edad".
del informacion_personal["Edad"]
print("La clave 'Edad' ha sido eliminada.")
print("-" * 30)


# 5. Imprimir el Diccionario Final:
# Imprime el diccionario resultante después de realizar todas las operaciones.
print("--- Paso 5: Imprimir Diccionario Final ---")
print("El diccionario final es:")
print(informacion_personal)
print("-" * 30)