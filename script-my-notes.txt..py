# Tarea de manipulación de archivos de texto

#1: Escribir contenido en un archivo

# Usamos 'with open' para manejar el archivo de forma segura.
# El modo 'w' (write) se usa para escribir. Creará el archivo si no existe.
print("Iniciando la escritura del archivo my_notes.txt.")
with open('my_notes.txt', 'w', encoding='utf-8') as notes_file:
    # Agregamos al menos tres líneas de texto.
    # Usamos '\n' para asegurar que cada nota ocupe una nueva línea.
    notes_file.write("Idea 1: Investigar sobre la historia de la programación.\n")
    notes_file.write("Idea 2: Planificar el proyecto final de la asignatura.\n")
    notes_file.write("Idea 3: Terminar de leer el capítulo 5 del libro.\n")
print("Contenido escrito correctamente en el archivo.")
print("=" * 25) # Separador visual

# Paso 2: Leer el contenido del archivo

# El modo 'r' (read) se usa para leer el archivo.
print("Leyendo el contenido de my_notes.txt:")
try:
    with open('my_notes.txt', 'r', encoding='utf-8') as notes_file:
        while True:
            # El método readline() lee una sola línea del archivo.
            current_line = notes_file.readline()


            if not current_line:
                break

            # Imprimimos la línea que acabamos de leer.
            # Usamos .strip() para quitar el salto de línea final y tener una salida limpia.
            print(f"Contenido: {current_line.strip()}")

except IOError:
    print("Ocurrió un error al intentar leer el archivo.")


print("=" * 25)
print("Proceso finalizado. El archivo se ha cerrado de forma segura.")