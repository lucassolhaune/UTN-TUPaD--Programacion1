#ej1

entrada = input("Ingrese su edad por favor:")

if entrada.isdigit():
    edad = int(entrada)
    if edad >= 18:
        print("Es mayor de edad")
    else:
        print("Es menor de edad")
else:
    print("Ingrese un valor entero")



#ej2

entrada = input("Ingrese una nota numerica: ")

if entrada.isdigit():
    nota = int(entrada)
    if nota >= 6:
        print("APROBADO")
    else:
        print("DESAPROBADO")

else:
    print("ERROR: Ingrese una nota numerica.")



#ej3
num_pares = int(input("Ingrese numeros pares: "))

if num_pares % 2 == 0:
    print("Ha ingresado un numero par.")
else:
    print("Por favor, ingrese un numero par.")





#ej4
edad = int(input("Ingrese su edad: "))


if edad < 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto")






#ej5
password = input("Ingrese su contraseña: ")

if len(password) >= 8 and len(password) <= 14:
    print("Ha ingresado uan contraseña correcta.")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")








#ej6
consumo = float(input("Ingrese su consumo mensual de energía eléctrica en kWh: "))

if consumo < 150:
    print("Consumo bajo")
elif consumo <= 300:
    print("Consumo medio")
else:
    print("Consumo alto")

if consumo > 500:
    print("Considere medidas de ahorro energético")





#ej7
texto = input("Ingrese una palabra o frase: ")

if texto[-1].lower() in "aeiou":
    print(texto + "!")
else:
    print(texto)






#ej8
nombre = input("Ingrese su nombre: ")
opcion = input("Elija una opción (1: MAYÚSCULAS, 2: minúsculas, 3: Primera letra mayúscula): ")

if opcion == "1":
    print(nombre.upper())
elif opcion == "2":
    print(nombre.lower())
elif opcion == "3":
    print(nombre.title())
else:
    print("Opción no válida.")







#ej9
magnitud = float(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve")
elif magnitud < 4:
    print("Leve")
elif magnitud < 5:
    print("Moderado")
elif magnitud < 6:
    print("Fuerte")
elif magnitud < 7:
    print("Muy Fuerte")
else:
    print("Extremo")








#ej10
hemisferio = input("Ingrese hemisferio (N/S): ").upper()
mes = int(input("Ingrese el número del mes (1-12): "))
dia = int(input("Ingrese el día (1-31): "))

# Validación de datos correctos
if (hemisferio != "N" and hemisferio != "S") or mes < 1 or mes > 12 or dia < 1 or dia > 31:
    print("Datos ingresados no válidos.")
else:
    # Evaluación de estaciones según la tabla
    if (mes == 12 and dia >= 21) or mes == 1 or mes == 2 or (mes == 3 and dia <= 20):
        if hemisferio == "N":
            print("Invierno")
        else:
            print("Verano")

    elif (mes == 3 and dia >= 21) or mes == 4 or mes == 5 or (mes == 6 and dia <= 20):
        if hemisferio == "N":
            print("Primavera")
        else:
            print("Otoño")

    elif (mes == 6 and dia >= 21) or mes == 7 or mes == 8 or (mes == 9 and dia <= 20):
        if hemisferio == "N":
            print("Verano")
        else:
            print("Invierno")

    else:
        if hemisferio == "N":
            print("Otoño")
        else:
            print("Primavera")
