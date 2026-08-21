#ej1
lista_de_notas = []

#cargo las notas
for n in range(10):
    nota_ingresada = float(input("Ingrese las notas de los estudiantes: "))
    lista_de_notas.append(nota_ingresada)

#Muestro la lista
print("Todas las notas: ", lista_de_notas)

#Calculo el promedio
suma_total_notas = sum(lista_de_notas)
promedio = suma_total_notas / len(lista_de_notas)
print("El promedio es: ", promedio)

#Nota mas alta y mas baja
nota_ingresada_mas_alta = max(lista_de_notas)
nota_ingresada_mas_baja = min(lista_de_notas)
print(f"La nota mas alta es: {nota_ingresada_mas_alta}")
print(f"La nota mas baja es: {nota_ingresada_mas_baja}")

#ej2
lista_producto = []

#Ingresar un producto
for numero_producto in range(5):
    producto_ingresado = input("Ingrese productos: ")
    lista_producto.append(producto_ingresado)
    print("Los productos que cargo el usuario son: ", lista_producto)

#Ordenar alfabeticamente
lista_producto_ordenada = sorted(lista_producto)
print("Los productos orednados alfabeicamente son: ", lista_producto_ordenada)

#Eliminar un producto de la lista
producto_a_eliminar = input("Que producto desea eliminar?: ")
lista_producto.remove(producto_a_eliminar)

#Lista actualizada
print("La lista aztualizada es: ", lista_producto)

#ej3
import random

lista_numeros_generados = []
lista_numeros_generados_pares = []
lista_numeros_generados_impares = []

#Generar nuemeros random del 1 al 100
for primer_intento in range(15):
    numeros_generados_random = random.randint(1, 100) #Numeros random del 1 al 100
    lista_numeros_generados.append(numeros_generados_random)


    #Ver si son pares o impares
    if numeros_generados_random % 2 == 0:
        lista_numeros_generados_pares.append(numeros_generados_random)
    else:
        lista_numeros_generados_impares.append(numeros_generados_random)

#Mostrar numeros generados aleatoriamente
print("La lista de numeros generados aleatoriamente son: ", lista_numeros_generados)

#Mostrar numeros pares
print(f"Los numeros pares son: {lista_numeros_generados_pares}")

#Mostrar numeros impares
print(f"Los numeros impares son: {lista_numeros_generados_impares}")

#ej4
datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
datos_sin_repetidos = []

for numeros in datos: 
    if numeros not in datos_sin_repetidos:
        datos_sin_repetidos.append(numeros)

print("La lista de numeros repetidos son: ", datos)
print("La lista de numeros no repetidos son: ", datos_sin_repetidos)

#ej5
estudiantes_presentes = ["Lucas","Oscar","Fransico","Emanuel","Pepe"] 
print("Lista actual de los estudiantes: ", estudiantes_presentes)

print("Presione un numero si desea....")
opcion_usuario = int(input("1) AGREGAR     2)ELIMINAR: "))

#Agrega un estudiante si pone 1
if opcion_usuario == 1:
    estudiantes_a_agregar = input("Ingrese el nombre del estudiante que desea agregar: ")
    estudiantes_presentes.append(estudiantes_a_agregar)
#Elimina un estudiante si pone 2
elif opcion_usuario == 2:
    estudiantes_a_eliminar = input ("Ingrese el nombre del estudiante que desea eliminar: ")
    estudiantes_presentes.remove(estudiantes_a_eliminar)
else:
    print("Ingrese una opción válida")

print(f"La lista de estudiantes actualizada es: {estudiantes_presentes}")

#ej6
lista_numero = [1, 2, 3, 4, 5, 6, 7]
lista_con_numeros_rotados = []

for numero in reversed(lista_numero):   #reversed() invierte todo el orden de la lista
    lista_con_numeros_rotados.append(numero)

print("La nueva lista con los numeros rotados es: ", lista_con_numeros_rotados)

#ej7
#Temperaturas minimas y maximas
matriz_temperaturas = [
    [12, 22],  # Día 1
    [10, 25],  # Día 2
    [15, 21],  # Día 3
    [8, 20],   # Día 4
    [11, 24],  # Día 5
    [14, 28],  # Día 6
    [13, 22]   # Día 7
]
print("Temperatura de la semana: ", matriz_temperaturas)

suma_temperaturas_minimas = 0
suma_temperaturas_maximas = 0

for registro_temperatura_diario in matriz_temperaturas:
    suma_temperaturas_maximas = suma_temperaturas_maximas + registro_temperatura_diario[1] #Posicion 1 en el primer array (maxima)
    suma_temperaturas_minimas = suma_temperaturas_minimas + registro_temperatura_diario[0] #Posicion 0 en el primer array (minima)

#Me devuelve lso 7 dias de la semana que los uso para el promedio
cantidad_dias_totales = len(matriz_temperaturas)

promdio_temperaturas_maximas = suma_temperaturas_maximas / cantidad_dias_totales
promdio_temperaturas_minimas = suma_temperaturas_minimas / cantidad_dias_totales

print(f"El promedio de las temperaturas maximas es: {promdio_temperaturas_maximas:.2f}")
print(f"El promedio de las temperaturas mainimas es: {promdio_temperaturas_minimas:.2f}")

#ej8
matriz_notas_estudiantes = [
    [8, 4, 7],
    [2, 5, 1],
    [9, 6, 8],
    [3, 1, 4],
    [10, 8, 6]
]

#Primer estudiante
numero_estudiante = 1

for notas in matriz_notas_estudiantes:
    #Sumo las 3 notas de este estudiante
    suma_notas_estudiante = 0
    for nota_individual in notas:
        suma_notas_estudiante = suma_notas_estudiante + nota_individual

    #Promedio
    promedio_del_estudiante = suma_notas_estudiante / 3

    print(f"Estudiante {numero_estudiante}: {promedio_del_estudiante}")

#ej9 
tablero_de_juego = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

jugador_actual = "X"
juego_en_curso = True

print("Bienvenido al Ta-Te-Ti!")

# Mostramos el tablero inicial (recorriendo fila por fila)
for fila_del_tablero in tablero_de_juego:
    print(fila_del_tablero[0], fila_del_tablero[1], fila_del_tablero[2])
print("")

while juego_en_curso:
    print(f"Es el turno del jugador: {jugador_actual}")
    
    fila_elegida = int(input("Elige una fila (1, 2 o 3): "))
    columna_elegida = int(input("Elige una columna (1, 2 o 3): "))
    
    indice_de_fila = fila_elegida - 1
    indice_de_columna = columna_elegida - 1
    
    if tablero_de_juego[indice_de_fila][indice_de_columna] == "-":
        tablero_de_juego[indice_de_fila][indice_de_columna] = jugador_actual
        
        # Mostramos el tablero actualizado sin usar funciones
        for fila_del_tablero in tablero_de_juego:
            print(fila_del_tablero[0], fila_del_tablero[1], fila_del_tablero[2])
        print("")
        
        # Cambiamos de jugador
        if jugador_actual == "X":
            jugador_actual = "O"
        else:
            jugador_actual = "X"
            
    else:
        print("Esa casilla ya está ocupada! Intente de nuevo.\n")

#ej10
ventas = [
    [10, 12, 8, 15, 20, 5, 9],    # producto 1
    [7, 9, 14, 10, 11, 6, 8],     # producto 2
    [20, 18, 22, 19, 25, 30, 28], # producto 3
    [3, 5, 4, 6, 2, 7, 5]         # producto 4
]

# total por producto 
for indice_producto, fila_producto in enumerate(ventas):
    total_producto = sum(fila_producto)
    print("Producto", indice_producto + 1, ":", total_producto)

# día con más ventas 
mejor_total_dia = 0   # el total más alto que encontramos hasta ahora
mejor_dia = 0          # en qué día ocurrió ese total más alto

for numero_dia in range(7):
    total_de_este_dia = 0

    for fila_producto in ventas:
        total_de_este_dia = total_de_este_dia + fila_producto[numero_dia]

    print("Día", numero_dia + 1, ":", total_de_este_dia)

    # ¿este día superó al mejor que teníamos guardado?
    if total_de_este_dia > mejor_total_dia:
        mejor_total_dia = total_de_este_dia
        mejor_dia = numero_dia

print("El día con más ventas fue el día", mejor_dia + 1, "con", mejor_total_dia, "unidades")

#ej11
nombres = [
    "Lucas", "Sofía", "Mateo", "Valentina", "Nicolás",
    "Martina", "Agustín", "Camila", "Tomás", "Renata"
]

usuario_ingresa_nombre = input("Ingrese un nombre por favor: ")

if usuario_ingresa_nombre in nombres:
    posicion = nombres.index(usuario_ingresa_nombre) #Si encontró el nombre, me da la posicion
    print(f"El nombre se encuentra en la lista y esta en la posicion: {posicion}")
    
else:
    print("El nombre no se encuentra en la lista. Intente nuevamente.")

#ej12
lista_numeros = []

for n in range(8):
    num_ingresar = int(input("Ingrese numeros por favor: "))
    lista_numeros.append(num_ingresar)
print("Lista original: ", lista_numeros)

lista_ordenada_menor_a_mayor = sorted(lista_numeros)
print("Lista ordenada de menor a mayor: ", lista_ordenada_menor_a_mayor)

lista_ordenada_mayora_a_menor = sorted(lista_numeros, reverse=True)
print("Lista ordenada de mayor a menor: ", lista_ordenada_mayora_a_menor)


#ej13 
puntajes = [450, 1200, 875, 990, 300, 1500, 640]

mayor = 0

#Me devuelve el mayor de la lista
for n in puntajes:
    if n > mayor:
        mayor = n
print('El mayor es: ', mayor)

ranking = sorted(puntajes, reverse=True)  #Devuelve la lista de mayor a menor
print(ranking)

posicion = ranking.index(990)
print('La posicion del numero 990 es:', posicion) #Dos
