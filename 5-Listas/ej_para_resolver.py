# """
# # Crea una lista de tus cinco frutas favoritas.
# # Luego utiliza append() para añadir una sexta fruta y remove () para eliminar
# # la segunda fruta de la lista. Imprime la lista resuelta
# """
# frutas = ["manzana", "banana", "naranja", "limon", "frutilla"]
# frutas.append("mandarina")
# print("Lista actualizada:", frutas)
# frutas.remove("naranja")
# print("La lista con la segunda fruta eliminada:", frutas)


# """
# Dada la lista = [10, 20, 30, 40, 50, 50, 60, 70, 80, 90] utiliza 
# slicing para obtener: los primeros tres elementos los
# últimos dos elementos y los elementos en posiciones pares
# """
# lista = [10, 20, 30, 40, 50, 50, 60, 70, 80, 90]
# print("Lista sin slice: ", lista)
# lista_slice = lista[1:3]
# print("Lista con slice: ",lista_slice)

"""
Genera una lista con los numeros impares de 1 al 20 utilizando range(). 
Luego, crea otra lista que contenga solo los numeros de la primera lista que son divisibles por 3
"""
impares = []
"""
Genera una lista con los numeros impares de 1 al 20 utilizando range(). 
Luego, crea otra lista que contenga solo los numeros de la primera lista que son divisibles por 3
"""

# Paso 1: generar los impares y guardarlos en una lista
impares = []
for n in range(1, 21, 2):
    impares.append(n)

print("Los números impares son:", impares)

# Paso 2: recorrer ESA lista (no un número suelto) y filtrar los divisibles por 3
numeros_divisibles_por_3 = []
for numero in impares:          # recorremos elemento por elemento
    if numero % 3 == 0:         # el % se aplica a CADA número, no a la lista entera
        numeros_divisibles_por_3.append(numero)

print("Los divisibles por 3 son:", numeros_divisibles_por_3)
"""
Conversión con split()
Convierte la cadena "PythonJava,C++JavaScript,PHP"
en una lista de lenguajes de programación utilizando
split(). Luego añade "Ruby" a la lista e imprime los
lenguajes por consola
"""

# cadena = "Python,Java,C++,JavaScript,PHP".split(",")
# print(cadena)


















# impares = list(range(1, 21, 2)) #Me genera una lista de 1 a 20
# divisibles_por_3 = []
# print("La lista original de los numeros: ", impares)

# for n in impares:
#     if n % 3 == 0:
#         divisibles_por_3.append(n)

# print("Los numeros divisibles por 3 son: ", divisibles_por_3)
