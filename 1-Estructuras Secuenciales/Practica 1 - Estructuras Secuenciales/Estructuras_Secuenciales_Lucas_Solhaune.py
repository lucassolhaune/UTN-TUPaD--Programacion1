#ej1
print('Hola mundo')



#ej2
nombre = input( 'Ingrese un nombre por favor: ')

print(f'Hola {nombre}!!')



#ej3
nombre = input('Ingrese su nombre por favor: ')
apellido = input('Ingrese su apllido por favor: ')
edad = int(input('ingrese su edad por favor: '))
lugar_residencia = input('Ingrese su lugar de residencia: ')

print (f'Mi nombre y apellido es {nombre} {apellido}, tengo {edad} años y vivo en {lugar_residencia}')



#ej4
import math

radio = float(input("Ingresa el radio del círculo: "))

area = math.pi * (radio ** 2)
perimetro = 2 * math.pi * radio

print(f"Área: {area:.2f}")
print(f"Perímetro: {perimetro:.2f}")




#ej5
cantidad_segundos = float(input("Ingrese la cantidad de segundos: \n"))
cantidad_de_horas = cantidad_segundos / 3600

print(f"Equivale a {cantidad_de_horas:.2f} horas.")




#ej6
numero = int(input("Ingrese un numero para ver su tabla: "))

print(f"La tabla del {numero} es: ")

#Recorre del 1 al 10 y te muestra la tabla de cada numero.
for multiplicador in range(1, 11):
    resultado_multiplicacion = numero * multiplicador
    print(f"{numero} x {multiplicador} = {resultado_multiplicacion}")




#ej7
numero1 = int(input("Ingrese el primero numero: "))
numero2 = int(input("Ingrese el segundo numero: "))

while numero1 == 0 or numero2 == 0:
    print("ERROR, los numeros deben ser distintos de cero.")
    numero1 = int(input("Ingrese el numero otra vez: "))
    numero2 = int(input("Ingrese el numero otra vez: "))

resultado_suma = numero1 + numero2
resultado_resta = numero1 - numero2
resultado_division = numero1 / numero2
resultado_multiplicacion = numero1 * numero2

print(f"El resultado de la suma es {resultado_suma}")
print(f"El resultado de la resta es {resultado_resta}")
print(f"El resultado de la division es {resultado_division:.2f}")
print(f"El resultado de la multiplicacion es {resultado_multiplicacion}")





#ej8
altura = float(input("Ingrese su altura en metros (ej. 1.75): "))
peso = float(input("Ingrese su peso en kg: "))

# Elevamos la altura al cuadrado (** 2)
indice_masa_corporal = peso / (altura ** 2)

if indice_masa_corporal < 18.5:
    print("Índice de peso bajo")
elif 18.5 <= indice_masa_corporal <= 24.9:
    print("Índice de peso normal")
elif 25 <= indice_masa_corporal <= 29.9:
    print("Sobrepeso")
else:
    print("Obesidad")

print(f"El índice de masa corporal es: {indice_masa_corporal:.2f}")






#ej9
temperatura_celcius = int(input("Ingrese la temperatura en celcius: "))

conversion_temperatura_fahrenheit = (9/5 * temperatura_celcius) + 32

print(f"La conversion de celcius a fahrenheit es: {conversion_temperatura_fahrenheit} º")



#ej10
num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese un numero: "))
num3 = int(input("Ingrese un numero: "))

suma = num1 + num2 + num3

promedio = suma / 3

print(f"El promedio de la suma de los 3 numeros es: {promedio}")







