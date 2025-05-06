# Programa para tomar notas de clase y guardarlas en un archivo

# Solicitar al usuario que escriba una nota
nota = input("Escribe tu nota de clase: ")

# Guardar la nota en un archivo de texto
with open("notas_clase.txt", "a") as archivo:
    archivo.write(nota + "\n")

print("Nota guardada exitosamente en 'notas_clase.txt'.")