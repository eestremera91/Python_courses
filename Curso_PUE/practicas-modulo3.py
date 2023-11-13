######################
# Sección 3.1.1.1
######################

# Pregunta #1: ¿Cuál es el resultado de la siguiente comparación?

# 2 == 2 # True

# Pregunta #2: ¿Cuál es el resultado de la siguiente comparación?

# 2 == 2. # True

# Pregunta #3: ¿Cuál es el resultado de la siguiente comparación?

# 1 == 2 # false

######################
# Sección 3.1.1.2
######################

# var == 0

# black_sheep == 2 * white_sheep
# black_sheep == (2 * white_sheep) # equivalente y mejora la legibilidad del código

# ¿Puedes adivinar la salida del código a continuación?

# var = 0   # asignando 0 a var
# print(var == 0)

# var = 1  # asignando 1 a var
# print(var == 0)

# ¿Puedes adivinar la salida del código a continuación?

# var = 0 # asignando 0 a var
# print(var != 0)

# var = 1 # asignando 1 a var
# print(var != 0)

######################
# Sección 3.1.1.3
######################

# Precedencia de operadores actualizada

# Prioridad	
# 1	+, -                       operadores unarios
# 2	**	
# 3	*, /, //, %
# 4	+, -                       operadores binarios
# 5 +=, -=, *=, /=, //=, %=    operadores abreviados
# 6	<, <=, >, >=	               
# 7	==, !=	

# numero1 = 12
# numero2 = 14
# print(numero1 >= numero2)

# !!!!
# print(2==2.000000000000001)

# print(2==2.00000000000000001)

######################
# Sección 3.1.1.5
######################

# Usando uno de los operadores de comparación en Python, 
# escribe un programa simple de dos líneas que tome el parámetro n 
# como entrada, que es un entero, e imprime False si n es menor que 100, 
# y True si n es mayor o igual que 100.

# n = int(input("Introduce un valor numérico: "))

# print("¿", n, "es menor que 100 ? -->", n < 100)
# print("¿", n, "es mayor o igual que 100 ? --> ", n >= 100)

# No debes crear ningún bloque if (hablaremos de ellos muy pronto). Prueba tu código usando los datos que te proporcionamos.

# Alternativa 1

# print("¿n es mayor o igual que 100?", int(input('Valor N ')) >= 100)

######################
# Sección 3.1.1.6
######################

# pseudocódigo
# if the_weather_is_good:
#     go_for_a_walk()
# have_lunch()

# tiempo = input("¿Qué tiempo hace hoy? ")

# if tiempo == "bueno":
#     print("salgo a pasear y después") 
# print("me voy a comer")

# # alternativa

# tiempo = input("¿Qué tiempo hace hoy? ")

# respuesta = (tiempo == "bueno")

# if respuesta:
#     print("salgo a pasear y después")  
# print("me voy a comer")

######################
# Sección 3.1.1.7
######################

# numero = int(input("Introduce un valor numérico: "))

# if numero < 100:
#     print(numero,"es menor que 100")
# else:
#     print(numero,"es mayor o igual que 100")

# #####################
# numero = int(input("Introduce un valor numérico: "))

# if numero < 100:
#     print(numero,"es menor que 100")
# else:
#     if numero == 100:    
#         print(numero,"es igual a 100")
#     else:
#         print(numero,"es mayor 100")

# # IF-ELSE NORMAL
# valor = 6

# if (valor % 2 == 0):
#   msg = "Par"
# else:
#   msg = "Impar"
  
# print(msg)

# # IF-ELSE NORMAL - variante
# valor = int(input("Introduce un valor numérico: "))

# if (valor % 2):
#   msg = "Impar"
# else:
#   msg = "Par"
  
# print(msg)


# # IF-ELSE - en una sola línea, válido solo para una única instrucción

# valor = 8

# if (valor % 2 == 0): msg = "Par"
# else: msg = "Impar"

# print(msg)

# # OPERADOR TERNARIO EN PYTHON - válido para asignar un valor u otro 

# valor = 8

# msg = "Par" if valor % 2 == 0 else "Impar"
# print(msg) 

######################
# Sección 3.1.1.8
######################

# tiempo = input("¿Qué tiempo hace hoy? ")

# if tiempo == "bueno":
#     print("iré a caminar")
#     print("me divertiré")
#     print("y después")
# else:
#     print("iré al teatro")
#     print("disfrutaré de la función")
#     print("y después")
# print("saldré a cenar")

# sentencias if anidadas

# the_weather_is_good = True
# nice_restaurant_is_found = False
# tickets_are_available = False

# if the_weather_is_good:
#     if nice_restaurant_is_found:
#         print("saldré a cenar")
#     else:
#         print("me comeré un sandwich")
# else:
#     if tickets_are_available:
#         print("nos vamos al cine")
#     else:
#         print("ir de compras")

# sentencia elif

# the_weather_is_good = False
# tickets_are_available = True
# table_is_available = True

# if the_weather_is_good:
#     print("saldré a caminar")
# elif tickets_are_available:
#     print("iré al cine")
# elif table_is_available:
#     print("saldré a cenar")
# else:
#     print("me quedaré en casa jugando al ajedrez")

######################
# Sección 3.1.1.8
######################

#  Ejemplo 1

# # Se leen dos números
# number1 = int(input("Ingresa el primer número: "))
# number2 = int(input("Ingresa el segundo número: "))

# # Elige el número más grande
# if number1 > number2:
#     larger_number = number1
# else:
#     larger_number = number2

# # Imprime el resultado
# print("El número más grande es:", larger_number)

# # Ejemplo 1
# # con operador ternario

# # Se leen dos números
# number1 = int(input("Ingresa el primer número: "))
# number2 = int(input("Ingresa el segundo número: "))

# # Elige el número más grande
# larger_number = number1 if number1 > number2 else number2 

# # Imprime el resultado
# print("El número más grande es:", larger_number)

# Ejemplo 2

## Se leen dos números
# number1 = int(input("Ingresa el primer número: "))
# number2 = int(input("Ingresa el segundo número: "))

## Elige el número más grande
# if number1 > number2: larger_number = number1
# else: larger_number = number2

## Imprime el resultado
# print("El número más grande es:", larger_number)

# Ejemplo 3

## Se leen tres números
# number1 = int(input("Ingresa el primer número: "))
# number2 = int(input("Ingresa el segundo número: "))
# number3 = int(input("Ingresa el tercer número: "))

# # Asumimos temporalmente que el primer número
# # es el más grande.
# # Lo verificaremos pronto.
# largest_number = number1

# # Comprobamos si el segundo número es más grande que el mayor número actual
# # y actualiza el número más grande si es necesario.
# if number2 > largest_number:
#     largest_number = number2

# # Comprobamos si el tercer número es más grande que el mayor número actual
# # y actualiza el número más grande si es necesario.
# if number3 > largest_number:
#     largest_number = number3

# # Imprime el resultado.
# print("El número más grande es:", largest_number)

######################
# Sección 3.1.1.9
######################

## Se leen tres números.

# number1 = int(input("Ingresa el primer número: "))
# number2 = int(input("Ingresa el segundo número: "))
# number3 = int(input("Ingresa el tercer número: "))

# # Verifica cuál de los números es el mayor
# # y pásalo a la variable largest_number
    
# largest_number = max(number1, number2, number3)

# # Imprime el resultado.
# print("El número más grande es:", largest_number)

######################
# Sección 3.1.1.10
######################

# numeroMayor = -999999999
# numero = 0

# while (numero != -1):
    
#     numero = int(input("Introduzca un número: "))
    
#     if numero > numeroMayor:
#         print("\tEl número",numero, "es mayor que el actual", numeroMayor)
#         numeroMayor = numero
#     else:
#         print("\tEl número",numero, "NO es mayor que el actual", numeroMayor, "y por lo tanto lo descartamos")
    
#     print("\tNueva iteración del bucle")
    
#####################################################
# print("El mayor número introducido es ", numeroMayor)


# import sys

# numeroMayor = -999999999

# while (True):
    
#     numero = int(input("Introduzca un valor numérico: "))
        
#     if numero == -1:
#             print("Este mensaje está dentro del bucle:",numeroMayor)
#             # sys.exit()
#             break
#     if numero > numeroMayor:
#         numeroMayor = numero
     
# #####################################################
# print("Este mensaje está fuera del bucle:", numeroMayor)


###################################
# Sección 3.1.1.11 - Laboratorio
###################################

# planta = input("Dime el nombre de una planta: \n")

# if planta == 'ESPATIFILIO':
#     print('Si, ¡El ESPATIFILIO! es la mejor planta de todos los tiempos!')
# elif planta == 'espatifilo':
#     print('No, ¡quiero un gran ESPATIFILIO!')
# else: 
#     print('¡ESPATIFILIO!, ¡No ' + planta + '!')

# Alternativa en la misma línea

# planta = input("Dime el nombre de una planta: \n")

# if planta == 'ESPATIFILIO': print('Si, ¡El ESPATIFILIO! es la mejor planta de todos los tiempos!')
# elif planta == 'espatifilo': print('No, ¡quiero un gran ESPATIFILIO!')
# else: print('¡ESPATIFILIO!, ¡No ' + planta + '!')

# Alternativa en una sola instrucción mediante operador ternario

# planta = input("Dime el nombre de una planta: \n")

# print("Si, ¡El ESPATIFILIO! es la mejor planta de todos los tiempos!" 
#       if planta == "ESPATIFILIO" 
#       else ("No, ¡quiero un gran ESPATIFILIO" 
#             if planta == "espatifilo" 
#             else "¡ESPATIFILIO!, ¡No " + planta ))

###################################
# Sección 3.1.1.12 - Laboratorio
###################################

# ingreso = float(input("Introduce el ingreso anual: "))

# if ingreso < 85528:
#     impuesto = ingreso * .18 - 556.2
# else:
#     impuesto = 14839.2 + (ingreso - 85528) * .32

# impuesto = round(impuesto, 0)

# print("El impuesto es:", max(impuesto, 0.0), "pesos")

# #en una misma línea

# ingreso = float(input("Introduce el ingreso anual: "))

# if ingreso < 85528: 
#     impuesto = (ingreso * .18) - 556.2
# else:               
#     impuesto = 14839.2 + ((ingreso - 85528) * .32)

# impuesto = round(impuesto, 0)
# print("El impuesto es:", max(impuesto, 0.0), "pesos")

# # #con operador ternario

# ingreso = float(input("Introduce el ingreso anual: "))

# impuesto = (ingreso * .18 - 556.2) if ingreso < 85528 else (14839.2 + (ingreso - 85528) * .32)

# impuesto = round(impuesto, 0)
# print("El impuesto es:", max(impuesto, 0.0), "pesos")

###################################
# Sección 3.1.1.13 - Laboratorio
###################################

# año = int(input("Introduzca un año: ")) # el año que queremos comprobar

# if año < 1582:
#     print("El año", año, "no está dentro del calendario Gregoriano")
    
# elif año % 4 != 0:                          # no divisible entre 4
#  	print("Año común")
# else:
#     if año % 100 != 0:                      # divisible entre 4 y no entre 100 o 400
#         print("Año bisiesto")
#     elif año % 100 == 0 and año % 400 != 0: # divisible entre 4 y 10 y no entre 400
#         print("Año común")
#     elif año % 100 == 0 and año % 400 == 0: # divisible entre 4, 100 y 400
#         print("Año bisiesto")


## ejemplo calculando el resto sin comparar el resultado
## para Python cualquier valor numérico por encima de 0 se considera True!!!!!

# year = int(input("Introduce un año:"))

# if year <= 1580:
#     result = "No esta dentro del período del calendario Gregoriano"
# else:
#     if year % 4:
#         result = "Común"
#     elif year % 100:
#         result = "bisiesto en elif"
#     elif year % 400:
#         result = "común"
#     else:
#         result = "bisiesto"        
# print(result)

########################
# Sección 3.1.1.14
########################

# x = 5 ;  y = 10 ; z = 8

# x, y, z = 5, 10, 8

## Una sentencia de if-else, por ejemplo:

# x = 10

# if x < 10:  # Condición
#     print("x es menor que 10")  # Ejecutado si la condición es Verdadera.

# else:
#     print("x es mayor o igual a 10")  # Ejecutado si la condición es Falsa.


## Una serie de sentencias if seguidas de un else, por ejemplo:

# x = 10

# if x > 5:  # True
#     print("x > 5")

# if x > 8:  # True
#     print("x > 8")

# if x > 10:  # False
#     print("x > 10")

# else:
#     print("se ejecutará el else")


## Cada if se prueba por separado. El cuerpo de else se ejecuta si el último if es False.

## La sentencia if-elif-else, por ejemplo:

# x = 10

# if x == 10:  # True
#     print("x == 10")

# if x > 15:  # False
#     print("x > 15")

# elif x > 10:  # False
#     print("x > 10")

# elif x > 5:  # True
#     print("x > 5")

# else:
#     print("else no será ejecutado")


## Si la condición para if es False, el programa verifica las condiciones de los bloques elif posteriores: el primer elif que sea True es el que se ejecuta. Si todas las condiciones son False, se ejecutará el bloque else.

## Sentencias condicionales anidadas, ejemplo:

# x = 10

# if x > 5:  # True
#     if x == 6:  # False
#         print("anidado: x == 6")
#     elif x == 10:  # True
#         print("anidado: x == 10")
#     else:
#         print("anidado: else")
# else:
#     print("else")

######################
# Sección 3.1.1.15
######################

# Posibles declaraciones de variables en la misma línea

# x, y, z = 5, 10, 8

# x = 5; y = 10;  z = 8

## Ejercicio 1

## ¿Cuál es la salida del siguiente fragmento de código?

# x = 5
# y = 10
# z = 8

# print(x > y) # False
# print(y > z) # True

## Ejercicio 2

## ¿Cuál es la salida del siguiente fragmento de código?

# x, y, z = 5, 10, 8  # declaración de múltiplrs variables separadas por comas

# print(x > z)        # False
# print((y - 5) == x) # True

## Ejercicio 3

## ¿Cuál es la salida del siguiente fragmento de código?

# x, y, z = 5, 10, 8
# x, y, z = z, y, x

# print(x > z)        # True
# print((y - 5) == x) # False

## Ejercicio 4

## ¿Cuál es la salida del siguiente fragmento de código?

# x = 10

# if x == 10:
#     print(x == 10)  # True
# if x > 5:
#     print(x > 5)    # True
# if x < 10:
#     print(x < 10)   # False, no se ejecuta
# else:
#     print("else")   # Se ejec uta e imprime "else"

## Ejercicio 5

## ¿Cuál es la salida del siguiente fragmento de código?

# x = "1"

# if x == 1:
#     print("uno")
# elif x == "1":
#     if int(x) > 1:
#         print("dos")
#     elif int(x) < 1:
#         print("tres")
#     else:
#         print("cuatro") # se imprime
# if int(x) == 1:
#     print("cinco")      # se imprime
# else:
#     print("seis")

## Ejercicio 6

## ¿Cuál es la salida del siguiente fragmento de código?

# x = 1
# y = 1.0
# z = "1"

# if x == y:
#     print("uno")    # True, se imprime
# if y == int(z):
#     print("dos")    # True, se imprime
# elif x == y:
#     print("tres")
# else:
#     print("cuatro")

######################
# Sección 3.1.2.1
######################

# Bucle infinito

# while True:
#     print("Estoy atrapado dentro de un bucle.")
    

# # Almacena el actual número más grande aquí.
# largest_number = -999999999

# # Ingresa el primer valor.
# number = int(input("Introduce un número o escribe -1 para detener: "))

# # Si el número no es igual a -1, continuaremos
# while number != -1:
#     # ¿Es el número más grande que el valor de largest_number?
#     if number > largest_number:
#         # Sí si, se actualiza largest_number.
#         largest_number = number
#     # Ingresa el siguiente número.
#     number = int(input("Introduce un número o escribe -1 para detener: "))

# # Imprime el número más grande
# print("El número más grande es:", largest_number)

######################
# Sección 3.1.2.2
######################

# # Un programa que lee una secuencia de números
# # y cuenta cuántos números son pares y cuántos son impares.
# # El programa termina cuando se ingresa un cero.

# numeros_pares = 0
# numeros_impares = 0

# # Lee el primer número.
# numero = int(input("Introduce un número o escribe 0 para detener: "))

# # 0 termina la ejecución.
# while numero != 0:
#     # Verificar si el número es impar.
#     if numero % 2 == 1:
#         # Incrementar el contador de números impares odd_numbers.
#         numeros_pares += 1
#     else:
#         # Incrementar el contador de números pares even_numbers.
#         numeros_impares += 1
#     # Leer el siguiente número.
#     numero = int(input("Introduce un número o escribe 0 para detener: "))

# # Imprimir resultados.
# print("Cuenta de números impares:", numeros_pares)
# print("Cuenta de números pares:", numeros_impares)


# counter = 5

# while counter != 0:
#     print("Dentro del bucle.", counter)
#     counter -= 1
# print("Fuera del bucle.", counter)


# counter = 5

# while counter:
#     print("Dentro del bucle.", counter)
#     print("Antes de evaluar la condición de salida", counter)
#     counter -= 1
# print("Fuera del bucle.", counter)

###################################
# Sección 3.1.2.3 - Laboratorio
###################################

# secret_number = 777

# print(
# """
# +==================================+
# | ¡Bienvenido a mi juego, muggle!  |
# | Introduce un número entero       |
# | y adivina qué número he          |
# | elegido para ti.                 |
# | Entonces,                        |
# | ¿Cuál es el número secreto?      |
# +==================================+
# """)

# numero_secreto = 777
# condicion = True

# while condicion:
#     numero = int(input("Intenta adivinar el número secreto: "))
#     if numero == numero_secreto:
#         print("\tBien hecho muggle!.", "Eres libre ahora!")
#         condicion = False
#     else:
#         print("\t¡Ja, ja! ¡Estás atrapado en mi bucle!")

# Alternativa 1 - sin variable booleana

# numero_secreto = 777

# # Lee el primer número.
# number = int(input("Introduce un número: "))

# # 777 termina la ejecución.
# while number != numero_secreto:
#     # Leer el siguiente número.
#     number = int(input("Incorrecto. Inténtalo de nuevo: "))


# print("Exacto. Es 777")

#  Alternativa 2 - con break

# secret_number = 777

# print(
# """
# +==================================+
# | ¡Bienvenido a mi juego, muggle!  |
# | Introduce un número entero       |
# | y adivina qué número he          |
# | elegido para ti.                 |
# | Entonces,                        |
# | ¿Cuál es el número secreto?      |
# +==================================+
# """)

# numero_secreto = 777

# while True:
#     numero = int(input("Intenta adivinar el número secreto: "))
#     if numero == numero_secreto:
#         print("\tBien hecho muggle!.", "Eres libre ahora!")
#         break
#     else:
#         print("\t¡Ja, ja! ¡Estás atrapado en mi bucle!")

###############################################
#  Solución con un número secreto aleatorio
###############################################

# import random

# numero_secreto = random.randint(1,10)

# condicion = True

# while condicion:
#     numero = int(input("Intenta adivinar el número secreto: "))
#     if numero == numero_secreto:
#         print("\tBien hecho muggle!.", "Eres libre ahora!")
#         condicion = False
#     else:
#         print("\t¡Ja, ja! ¡Estás atrapado en mi bucle!")

######################
# Sección 3.1.5.4
######################

# for contador in range(10):
#     print("El valor de contador es actualmente", contador)

# for contador in range(2, 8):
#     print("El valor de contador es actualmente", contador)

######################
# Sección 3.1.2.5
######################

# controlar número de iteraciones con bucle while
# contador = 0

# while contador < 100:
#     print(contador)    
#     contador += 1

# for contador in range(100):
#     print(contador)

# for contador in range(10):
#     print("El valor de contador es actualmente", contador)

# for contador in range(2, 8):
#     print("El valor de contador es actualmente", contador)


# palabra = input("Introduce una palabra: ")

# for letra in palabra:
#     print(letra)

# for contador in range(2, 8, 3):
#     print("El valor de contador es actualmente", contador)

# for i in range(2, 1):
#     print("El valor de i es actualmente", i)

## Nota: si el conjunto generado por la función range() está vacío, 
## el bucle no ejecutará su cuerpo en absoluto.

# for i in range(1, 1):
#     print("El valor de i es actualmente", i)

## Nota: el conjunto generado por range() debe ordenarse en un orden ascendente. 
## No hay forma de forzar el range() para crear un conjunto en una forma diferente. 
## Esto significa que el segundo argumento de range() debe ser mayor que el primero.

## Por lo tanto, tampoco habrá salida aquí:

# for i in range(2, 1):
#     print("El valor de i es actualmente", i)

## Echemos un vistazo a un programa corto cuya tarea es escribir 
## algunas de las primeras potencias de dos:

# power = 1
# for expo in range(16):
#     print("2 a la potencia de", expo, "es", power)
#     power *= 2

# palabra = input("Introduzca una palabra: ")

# for letra in palabra:
#     print(letra)
    
###################################
# Sección 3.1.2.6 - Laboratorio
###################################

# import time

# # Escribe un bucle for que cuente hasta cinco.
    
# for contador in range(1,6):
    
#     # Cuerpo del bucle: imprime el número de iteración del bucle y la palabra "Mississippi".
#     print(contador, "Mississippi.")

#     # Cuerpo del bucle - usar: time.sleep (1)
#     time.sleep(1)

# # Escribe una función de impresión con el mensaje final.
# print("¡Listos o no, ahí voy!")

######################
# Sección 3.1.2.7
######################

# break - ejemplo

# print("La instrucción break:")
# for i in range(1, 6):
#     if i == 3:
#         break                         # finaliza el bucle
#     print("Dentro del bucle.", i)
# print("Fuera del bucle.")


# # continue - ejemplo

# print("\nLa instrucción continue:")
# for i in range(1, 6):
#     if i == 3:
#         continue                        # continúa en la siguiente iteración del bucle
#     print("Dentro del bucle.", i)
# print("Fuera del bucle.")

# # imprimir solo números pares
# print("\nLa instrucción continue:")
# for i in range(1, 100):
#     if i >=10:
#         break
#     if i % 2:
#         continue                        # continúa en la siguiente iteración del bucle
#     print("Dentro del bucle.", i)
# print("Fuera del bucle.")


######################
# Sección 3.1.2.8
######################

# # Ejemplo con break

# largest_number = -99999999
# counter = 0

# while True:
#     number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))
#     if number == -1:
#         break
#     counter += 1
#     if number > largest_number:
#         largest_number = number

# if counter != 0:
#     print("El número más grande es", largest_number)
# else:
#     print("No has ingresado ningún número.")

# # Ejemplo con continue

# largest_number = -99999999
# counter = 0

# number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))

# while number != -1:
    
#     if number == -1:
#         continue
#     counter += 1

#     if number > largest_number:
#         largest_number = number
#     number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))

# if counter:
#     print("El número más grande es", largest_number)
# else:
#     print("No has ingresado ningún número.")

###################################
# Sección 3.1.2.9- Laboratorio
###################################

# Diseña un programa que use un bucle while y le pida continuamente al usuario 
# que ingrese una palabra a menos que ingrese "chupacabra" como la palabra de salida secreta, 
# en cuyo caso el mensaje "¡Has dejado el bucle con éxito". debe imprimirse en la pantalla 
# y el bucle debe terminar.

# No imprimas ninguna de las palabras ingresadas por el usuario. 
# Utiliza el concepto de ejecución condicional y la sentencia break.

# while True:
#     palabra = input("Introduce una palabra: ")
    
#     if palabra == "chupacabra":
#         break
# print("¡Has dejado el bucle con éxito!")

###################################
# Sección 3.1.2.10 - Laboratorio
###################################

# Pedir al usuario que ingrese una palabra.
# Utiliza user_word = user_word.upper() para convertir la palabra ingresada por el usuario a mayúsculas; 
# hablaremos sobre los llamados métodos de cadena y el upper() muy pronto, no te preocupes.

# Utiliza la ejecución condicional y la instrucción continue para "comer" 
# las siguientes vocales A , E , I , O , U de la palabra ingresada.

# Imprime las letras no consumidas en la pantalla, cada una de ellas en una línea separada.

# palabra = input("Ingresa tu palabra: ")
# palabra = palabra.upper()

# for letra in palabra:
    
#     if letra == "A":
#         continue
#     elif letra == "E":
#         continue
#     elif letra == "I":
#         continue
#     elif letra == "O":  
#         continue
#     elif letra == "U":
#         continue

#     print(letra)

# # Alternativa

# user_word = input("Write a word:").upper()

# # user_word = user_word.upper()

# # Indicar al usuario que ingrese una palabra
# # y asignarlo a la variable user_word.

# for letter in user_word:
#     # Completa el cuerpo del bucle for.
#     if letter in "AEIOU":
#         continue
#     print(letter)

###################################
# Sección 3.1.2.11 - Laboratorio
###################################

palabra_sin_vocales = ""

# palabra = input("Ingresa tu palabra: ")
# palabra = palabra.upper()

# for letra in palabra:
#     if letra == "A":
#         continue
#         # pass
#     elif letra == "E":
#         continue
#         # pass
#     elif letra == "I":
#         continue
#         # pass
#     elif letra == "O":
#         continue
#         # pass
#     elif letra == "U":
#         continue
#         # pass
    
#     # Escribe tu código aquí.
#     palabra_sin_vocales += letra
# 		
# # Imprimir la palabra asignada a word_without_vowels.
# print(palabra_sin_vocales)

# Alternativa

# palabra=input("Write a word:")
# palabra = palabra.upper()
# palabra_sin_vocales = ""

# # Indicar al usuario que ingrese una palabra
# # y asignarla a la variable user_word.

# for letra in palabra:
#     # Completa el cuerpo del bucle for.
#     if letra in "AEIOU":
#         continue
#     palabra_sin_vocales += letra

# # Imprimir la palabra asignada a word_without_vowels.
# print(palabra_sin_vocales)

######################
# Sección 3.1.2.12
######################

# Rama else

# i = 10

# while i < 5:
#     print(i)
#     i += 1
# else:
#     print("else:", i)

######################
# Sección 3.1.2.13
######################

# Rama else

# for i in range(5):
#     print(i)
# else:
#     print("else:", i)

# print(i) # La variable i sigue existiendo fuera del bucle!!

# i = 111

# for i in range(2, 1):
#     print(i)
# else:
#     print("else:", i)

###################################
# Sección 3.1.2.14 - Laboratorio
###################################

# Escucha esta historia: Un niño y su padre, un programador de computadoras, 
# juegan con bloques de madera. Están construyendo una pirámide.

# Su pirámide es un poco rara, ya que en realidad es una pared en forma de pirámide, es plana. 
# La pirámide se apila de acuerdo con un principio simple: cada capa inferior contiene 
# un bloque más que la capa superior.

# Tu tarea es escribir un programa que lea la cantidad de bloques que tienen los constructores, 
# y generar la altura de la pirámide que se puede construir utilizando estos bloques.

# Nota: La altura se mide por el número de capas completas: si los constructores no tienen 
# la cantidad suficiente de bloques y no pueden completar la siguiente capa, 
# terminan su trabajo inmediatamente.

# numero_bloques = int(input("Ingresa el número de bloques: "))

# print()

# capa = 0
# bloques_en_capa = 1

# while bloques_en_capa <= numero_bloques:
        
#     print("Número de bloques restantes: ", numero_bloques, 
#           "\t- capa:", capa + 1, 
#           "\t- Bloques en capa actual:", bloques_en_capa)
    
#     capa += 1
#     numero_bloques -= bloques_en_capa       
#     bloques_en_capa += 1

# print("\nLa altura de la pirámide es de", capa, "niveles" if capa !=1 else "nivel")


# # Alternativa

# numero_bloques = int(input("Ingresa el número de bloques: "))

# nivel = 1

# while (numero_bloques//nivel >= nivel):
    
#     nivel+= 1
    
# print(nivel)

###################################
# Sección 3.1.2.15 - Laboratorio
###################################

# c0 = int(input("Introduce un número: "))

# pasos=0

# while c0 > 1:

#     if c0 % 2 == 0:
#         c0 = int(c0 / 2)
#     else:
#         c0 = 3 * c0 + 1
        
#     pasos+=1
#     print(c0)
    
# print("pasos = ",pasos)

###################################
# Sección 3.1.2.17
###################################

# Ejercicio 1

# Crea un bucle for que cuente de 0 a 10, e imprima números impares en la pantalla. 
# Usa el esqueleto de abajo:

# for i in range(1, 11):
#     # Línea de código.
#     if i % 2 != 0:
#         # Línea de código.
#         print(i)

# Ejercicio 2

# Crea un bucle while que cuente de 0 a 10, e imprima números impares en la pantalla. 
# Usa el esqueleto de abajo:

# x = 1
# while x < 11:
#     # Línea de código.
#     if x % 2 != 0:
#         # Línea de código.
#         print(x)
#     # Línea de código.
#     x += 1 

# Ejercicio 3

# Crea un programa con un bucle for y una sentencia break. 
# El programa debe iterar sobre los caracteres en una dirección de correo electrónico, salir del bucle cuando llegue al símbolo @ e imprimir la parte antes de @ en una línea. Usa el esqueleto de abajo:

# for ch in "john.smith@pythoninstitute.org":
#     if ch == "@":
#         break
#     print(ch, end="")

# Ejercicio 4

# Crea un programa con un bucle for y una sentenciacontinue. El programa debe iterar sobre una cadena de dígitos, reemplazar cada 0 con x, e imprimir la cadena modificada en la pantalla. Usa el esqueleto de abajo:

# for digit in "0165031806510":
#     if digit == "0":
#         print("x", end="")
#         continue
#     print(digit, end="")

# Ejercicio 5

# ¿Cuál es la salida del siguiente código?

# n = 3

# while n > 0:
#     print(n + 1)
#     n -= 1
# else:
#     print(n)

# Ejercicio 5

# ¿Cuál es la salida del siguiente código?

# n = range(4)

# for num in n:
#     print(num - 1)
# else:
#     print(num)

# Ejercicio 7

# ¿Cuál es la salida del siguiente código?

# for i in range(0, 6, 3):
#     print(i)

######################
# Sección 3.3.1.1
######################

booleanos = [False, True]

# # Tabla de verdad de and

# print('x\t\ty\t\tx and y')
# print('-'*22)
# for x in booleanos:
#     for y in booleanos:
#         print(x, y, x and y, sep = '\t')
        
# print()

# # # Tabla de verdad de or

# print('x\t\ty\t\tx or y')
# print('-'*22)
# for x in booleanos:
#     for y in booleanos:
#         print(x, y, x or y, sep = '\t')

# print()

# Tabla de verdad de ^ (or exclusivo)

# print('x\t\ty\t\tx ^ y')
# print('-'*21)
# for x in booleanos:
#     for y in booleanos:
#         print(x, y, x ^ y, sep = '\t') 

# print()

# # Tabla de verdad de not

# print('x\t\tnot x')
# print('-'*13)
# for x in booleanos:
#     print(x, not x, sep = '\t')

######################
# Sección 3.3.1.2
######################

# &  (ampersand) - conjunción a nivel de bits.
# |  (barra vertical) - disyunción a nivel de bits.
# ~  (tilde) - negación a nivel de bits.
# ^  (signo de intercalación) - o exclusivo a nivel de bits (xor).

# var = 1

# # Ejemplo 1:
# print(var > 0)
# print(not (var <= 0)) # equivalente

# # # Ejemplo 2:
# print(var != 0)
# print(not (var == 0)) # equivalente

# p = False
# q = True

# ## La negación de una conjunción es la separación de las negaciones.

# print(not (p and q) == (not p) or (not q))

# # # La negación de una disyunción es la conjunción de las negaciones.

# print((not (p or q)) == ((not p) and (not q)))


# i = 1
# j = not not i

# print("Valor de i:", i)
# print("Valor de not i:", not i)
# print("Valor de not not i:", not not i)
# print(j)

# & requiere exactamente dos 1s para proporcionar 1 como resultado.
# | requiere al menos un 1 para proporcionar 1 como resultado.
# ^ requiere exactamente un 1 para proporcionar 1 como resultado.

######################
# Sección 3.3.1.3
######################

# numero1 = 15
# numero2 = 22

## Representación en binario con 32 bits

# print("Número 1:", "\t" * 4, format(numero1, '#032b'))
# print("Número 2:", "\t" * 4, format(numero2, '#032b'))

## Representación en binario

# print("Número 1:", "\t" * 4, bin(numero1))
# print("Número 2:", "\t" * 4, bin(numero2))

## The expression x and y first evaluates x; if x is false, 
## its value is returned; otherwise, 
## y is evaluated and the resulting value is returned.

# #print("numero1 and numero2:", "\t", numero1 and numero2)

#  AND a nivel de bits
# print("Conjunción lógica a nivel de bits (&):")
# print("numero1 & numero2:", "\t", format(numero1 & numero2 , '#032b'))

#  OR a nivel de bits
# print("Disyucción lógica a nivel de bits (|):")
# print("numero1 | numero2:", "\t", format(numero1 | numero2 , '#032b'))

#  OR exclusivo a nivel de bits
# print("Disyucción exclusiva a nivel de bits o xor (^):")
# print("numero1 ^ numero2:", "\t", format(numero1 ^ numero2 , '#032b'))

# print("not numero1:", "\t" * 3, not numero1)

# print("~numero1:", "\t" * 4, format(~numero1, '#32b'))

# # x = x & y	
# x &= y # equivalente en forma abreviada
# # x = x | y	
# x |= y # equivalente en forma abreviada
# # x = x ^ y	
# x ^= y # equivalente en forma abreviada

######################
# Sección 3.3.1.4
######################

flag_register = 8

print(format(flag_register, '#032b'))

# ## Comprobar el estado del bit

the_mask = 8 # el peso del bit es igual a 2 elevado a 3 (8) - tercer bit

print(format(the_mask, '#032b'))

# # verificar si el tercer bit está en 0 o 1

# if flag_register & the_mask == True:
#     # Mi bit se estableció en 1.
#     print("tercer bit igual a 1")
# else:
#     # Mi bit se restableció a 0.
#     print("tercer bit igual a 0")

# # Reiniciar el bit a 0

# flag_register = flag_register & ~the_mask
# flag_register &= ~the_mask # alternativa

# print("Cambiando tercer bit a cero")
# print(format(flag_register, '#032b'))

# # verificar si el tercer bit está en 0 o 1

# if flag_register & the_mask:
#     # Mi bit se estableció en 1.
#     print("tercer bit igual a 1")
# else:
#     # Mi bit se restableció a 0.
#     print("tercer bit igual a 0")

# # establecer el tercer bit a 1

# flag_register = flag_register | the_mask
# flag_register |= the_mask

# print("Estableciendo tercer bit a 1")
# print(format(flag_register, '#032b'))

# # Negación del tercer bit

# flag_register = flag_register ^ the_mask
# # flag_register ^= the_mask # CUIDADO!!!, si ejecuto ambas instrucciones niega el bit dos veces!!!!

# print("Negando tercer bit")
# print(format(flag_register, '#032b'))

# flag_register ^= the_mask

# print("Negando de nuevo tercer bit")
# print(format(flag_register, '#032b'))

######################################################################
# import time

# var = 2

# inicio = time.time()



# for i in range(30):

#     var **= 2    
    
# fin1 = time.time()

# print(round(fin1 - inicio, 2), "segundos")


# var = 2

# for i in range(30):

#     var = var << 1

# fin2 = time.time()
    

# print(round(fin2 - fin1, 2), "segundos")


######################
# Sección 3.3.1.5
######################

# Prioridad	Operador	
# 1	~, +, -	unario
# 2	**	
# 3	*, /, //, %	
# 4	+, -	binario
# 5	<<, >>	
# 6	<, <=, >, >=	
# 7	==, !=	
# 8	&	
# 9	|	
# 10	=, +=, -=, *=, /=, %=, &=, ^=, |=, >>=, <<=	

# 17 >> 1 → 17 // 2 (17 dividido entre 2 a la potencia de 1) → 8 (desplazarse hacia la derecha en un bit equivale a la división entera entre dos)
# 17 << 2 → 17 * 4 (17 multiplicado por 2 a la potencia de 2) → 68 (desplazarse hacia la izquierda dos bits es lo mismo que multiplicar números enteros por cuatro)

# var = 17

# print(var)
# print(format(var, '#032b'))

# var_right = var >> 1

# print(var_right)
# print(format(var_right, '#032b'))

# var_left = var << 2

# print(var_left)
# print(format(var_left, '#032b'))

######################
# Sección 3.3.1.6
######################

# &  (ampersand) - conjunción a nivel de bits.
# |  (barra vertical) - disyunción a nivel de bits.
# ~  (tilde) - negación a nivel de bits.
# ^  (signo de intercalación) - o exclusivo a nivel de bits (xor).

# # Ejercicio 1

# # ¿Cuál es la salida del siguiente fragmento de código?

# x = 1
# y = 0

# z = ((x == y) and (x == y)) or not(x == y)
# print(not(z))

# # Ejercicio 2

# # ¿Cuál es la salida del siguiente fragmento de código?

# x = 4
# y = 1

# print("Valor de x en decimal:", x)
# print(format(x, '#032b'))

# print("Valor de y en decimal:", y)
# print(format(y, '#032b'))

# a = x & y

# print("Valor de a en decimal:", a)
# print(format(a, '#032b'))

# b = x | y

# print("Valor de a en decimal:", b)
# print(format(b, '#032b'))

# c = ~x  # !difícil! negación!!

# print("Valor de c en decimal:", c)
# print(format(c, '#032b'))

# d = x ^ 5

# print("Valor de d en decimal:", d)
# print(format(d, '#032b'))

# # e = x >> 2

# # print("Valor de e en decimal:", e)
# # print(format(e, '#032b'))

# # f = x << 2

# # print("Valor de f en decimal:", f)
# # print(format(f, '#032b'))

# # print(a, b, c, d, e, f)

######################
# Sección 3.4.1.1
######################

# numeros = [10, 5, 7, 2, 1]

# print(type(numeros))

# # Impresión de elementos de la lista

# print(numeros)

# #  Referencia a elementos por índice

# print("Valor en posición 1:" , numeros[1])

# # Procesamiento en bucle for

# for numero in numeros:   
#     print("Valores dentro del bucle for:", numero)

# # Procesamiento en bucle while

# indice = 0

# while indice < len(numeros):
    
#     print("Valores dentro del bucle while", numeros[indice])
#     indice += 1

######################
# Sección 3.4.1.2
######################

# numbers = [10, 5, 7, 2, 1]
# print("Contenido de la lista original:", numbers)  # Imprimiendo contenido de la lista original.

# numbers[0] = 111
# print("Nuevo contenido de la lista: ", numbers)  # Contenido de la lista actual.

# copiar el valor del quinto elemento al segundo elemento.

# numbers[1] = numbers[4]  # Copiando el valor del quinto elemento al segundo elemento.
# print("Nuevo contenido de la lista:", numbers)  # Imprimiendo el contenido de la lista actual.

######################
# Sección 3.4.1.3
######################

# numbers = [10, 5, 7, 2, 1]

# print("Contenido de la lista original:", numbers)  # Imprimiendo el contenido de la lista original.

# numbers[0] = 111
# print("\nContenido de la lista con cambio:", numbers)  # Imprimiendo contenido de la lista con 111.

# numbers[1] = numbers[4]  # Copiando el valor del quinto elemento al segundo elemento.
# print("Contenido de la lista con intercambio:", numbers)  # Imprimiendo contenido de la lista con intercambio.

# print("\nLongitud de la lista:", len(numbers))  # Imprimiendo la longitud de la lista.



# indice = 0

# while indice < len(numbers):
    
#     print(numbers[indice])
#     indice += 1

# # # Equivalente

# for number in numbers:   
#     print(number)

# # # Equivalente

# for indice in range(len(numbers)):   
#     print(numbers[indice])

######################
# Sección 3.4.1.4
######################

# numbers = [10, 5, 7, 2, 111]
# print("Contenido de la lista original:", numbers)  # Imprimiendo el contenido de la lista original.

# numbers[0] = 111
# print("\nContenido de la lista con cambio:", numbers)  # Imprimiendo contenido de la lista con 111.

# numbers[1] = numbers[4]  # Copiando el valor del quinto elemento al segundo elemento.

# print("Contenido de la lista con intercambio:", numbers)  # Imprimiendo contenido de la lista con intercambio.

# print("\nLongitud de la lista:", len(numbers))  # Imprimiendo la longitud de la lista.

# del numbers[1]      # Eliminando el segundo elemento de la lista.

# numbers.remove(111) # Eliminando por valor

# print(numbers)
# print("Longitud de la nueva lista:", len(numbers))  # Imprimiendo nueva longitud de la lista.
# print("\nNuevo contenido de la lista:", numbers)  # Imprimiendo el contenido de la lista actual.

# print(help(numbers))

# del numbers[1]  # Eliminando el segundo elemento de la lista.
# print("Longitud de la nueva lista:", len(numbers))  # Imprimiendo nueva longitud de la lista.
# print("\nNuevo contenido de la lista:", numbers)  # Imprimiendo el contenido de la lista actual.

######################
# Sección 3.4.1.5
######################

# numbers = [111, 7, 2, 1]

# print(numbers[-1]) # Ultimo
# print(numbers[-2]) # Penúltimo
# print(numbers[-3]) # Antepenúltimo
# print(numbers[-4])
# print(numbers[-5]) # Error IndexOutOfRange!!!!

####################################
# Sección 3.4.1.6 - Laboratorio
####################################

# lista_sombreros = [1, 2, 3, 4, 5]

# # Paso 1
# lista_sombreros[2] = int(input("Ingresa un número entero: "))

# # Paso 2
# del lista_sombreros[-1]
# # del lista_sombreros[4]  # Equivalente!!

# # Paso 3
# print(len(lista_sombreros))

# # imprimir lista completa para comprobar

# print(lista_sombreros)

# # Concatenar todos los valores como String

# resultado = ""

# for valor in lista_sombreros:
#     resultado += str(valor)
# print(resultado)

######################
# Sección 3.4.1.8
######################

# numbers = [111, 7, 2, 1]
# print(len(numbers))
# print(numbers)

# # ###

# numbers.append(4)

# print(len(numbers))
# print(numbers)

# # # ###

# numbers.insert(0, 222)
# print(len(numbers))
# print(numbers)

# # eliminación por valor!!!

# numbers.remove(111)
# print(len(numbers))
# print(numbers)

######################
# Sección 3.4.1.9
######################

# my_list = []  # Creando una lista vacía.

# for i in range(5):
#     my_list.append(i + 1)
# print(my_list)


# my_list = []  # Creando una lista vacía.

# for i in range(5):
#     my_list.insert(0, i + 1)
#     print(my_list)

# print(my_list)

# my_list = []  # Creando una lista vacía.

# for i in range(5):
#     my_list.insert(-1, i + 1) # inserta en penúltima posición!!!!!!!!!
#     print(my_list)

# print(my_list)

######################
# Sección 3.4.1.10
######################

# my_list = [10, 1, 8, 3, 5]
# total = 0

# for i in my_list:
#     total += i

# print(total)


# my_list = [10, 1, 8, 3, 5]
# total = 0

# for i in range(len(my_list)):
#     total += my_list[i]

# print(total)

######################
# Sección 3.4.1.11
######################

# variable_1 = 1
# variable_2 = 2

# variable_2 = variable_1
# variable_1 = variable_2

# print(variable_1)
# print(variable_2)


# variable_1 = 1
# variable_2 = 2

# auxiliary = variable_1
# variable_1 = variable_2
# variable_2 = auxiliary

# print(variable_1)
# print(variable_2)


# variable_1 = 1
# variable_2 = 2

# variable_1, variable_2 = variable_2, variable_1

# print(variable_1)
# print(variable_2)

## ¿funciona con más de dos valores?

# variable_1 = 1
# variable_2 = 2
# variable_3 = 3

# variable_1, variable_2, variable_3 = variable_3, variable_2, variable_1

# print(variable_1)
# print(variable_2)
# print(variable_3)

######################
# Sección 3.4.1.12
######################

# my_list = [10, 1, 8, 3, 5]

# my_list[0], my_list[4] = my_list[4], my_list[0]
# my_list[1], my_list[3] = my_list[3], my_list[1]

# print(my_list)

# my_list = [10, 1, 8, 3, 5]
# length = len(my_list)

# for contador in range(length // 2):
    
#     print("\nValor de contador: ", contador, "\n")
#     print("\tmy_list[contador]:", my_list[contador])
#     print("\tmy_list[length - contador - 1]", my_list[length - contador - 1])
    
#     my_list[contador], my_list[length - contador - 1] = my_list[length - contador - 1], my_list[contador]

# print()
# print(my_list)

#####################################
# Sección 3.4.1.13 - Laboratorio
#####################################

# # Paso 1: Crea una lista vacía llamada beatles.

# Beatles = []
# print("Paso 1:", Beatles)

# # Paso 2: Emplea el método append() para agregar los siguientes miembros 
# # de la banda a la lista: John Lennon, Paul McCartney y George Harrison.

# Beatles.append("John Lennon")
# Beatles.append("Paul McCartney")
# Beatles.append("George Harrison")
# print("Paso 2:", Beatles)

# # Paso 3: Emplea el bucle for y el append() para pedirle al usuario 
# # que agregue los siguientes miembros de la banda a la lista: Stu Sutcliffe, y Pete Best.

# for members in range(2):
#     Beatles.append(input("Nuevo miembro de la banda: "))
# print("Paso 3:", Beatles)

# #  Paso 4: Usa la instrucción del para eliminar a Stu Sutcliffe y Pete Best de la lista.

# del Beatles[-1]
# del Beatles[-1]

# # Alternativa
# # Beatles.remove("Stu Sutcliffe")
# # Beatles.remove("Pete Best")

# print("Paso 4:", Beatles)

# # Paso 5: Usa el método insert() para agregar a Ringo Starr al principio de la lista.

# Beatles.insert(0, "Ringo Starr")
# print("Paso 5:", Beatles)
# print("Los Fav:",len(Beatles))

######################
# Sección 3.4.1.14
######################

# ¿Cuál es la salida del siguiente fragmento de código?

# lst = [1, 2, 3, 4, 5]
# lst.insert(1, 6)
# del lst[0]
# lst.append(1)

# print(lst)

# ¿Cuál es la salida del siguiente fragmento de código?

# lst = [1, 2, 3, 4, 5]
# lst_2 = []
# add = 0

# for number in lst:
#     add += number
#     lst_2.append(add)

# print(lst_2)

# ¿Cuál es la salida del siguiente fragmento de código?

# lst = []
# del lst
# print(lst)

# ¿Cuál es la salida del siguiente fragmento de código?

# lst = [1, [2, 3], 4]
# print(lst[1])
# print(len(lst))

######################
# Sección 3.5.1.2
######################

# my_list = [8, 10, 6, 2, 4]  # lista a ordenar

# for i in range(len(my_list) - 1):  # necesitamos (5 - 1) comparaciones

#     if my_list[i] > my_list[i + 1]:  # compara elementos adyacentes
#         my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]  # Si terminamos aquí, tenemos que intercambiar elementos.

#     print("Iteración ", i , ":", my_list)

# my_list = [8, 10, 6, 2, 4]  # lista a ordenar
# swapped = True  # Lo necesitamos verdadero (True) para entrar en el bucle while.

# while swapped:
#     swapped = False  # no hay intercambios hasta ahora
    
#     for i in range(len(my_list) - 1):
        
#         if my_list[i] > my_list[i + 1]:
            
#             swapped = True  # ¡ocurrió el intercambio!
#             my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
            
#     print("Iteración de bucle while:",my_list)

######################
# Sección 3.5.1.3
######################

# my_list = [8, 10, 6, 2, 4]
# my_list.sort()
# print(my_list)


# my_list = []
# swapped = True
# num = int(input("¿Cuántos elementos deseas ordenar?: "))

# # rellenar la lista
# for i in range(num):
#     val = int(input("Ingresa un elemento de la lista: "))
#     my_list.append(val)
    
#     print("Elementos en la lista:", my_list)

# # ordenar la lista
# while swapped:
#     swapped = False
#     for i in range(len(my_list) - 1):
#         if my_list[i] > my_list[i + 1]:
#             swapped = True
#             my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

# print("\nOrdenada:")
# print(my_list)

######################
# Sección 3.5.1.4
######################

# # Ejercicio 1

# # ¿Cuál es la salida del siguiente fragmento de código?

# lst = ["D", "F", "A", "Z"]
# lst.sort()

# print(lst)


# # Ejercicio 2

# # ¿Cuál es la salida del siguiente fragmento de código?

# a = 3
# b = 1
# c = 2

# lst = [a, c, b]
# lst.sort()

# print(lst)


# # Ejercicio 3

# # ¿Cuál es la salida del siguiente fragmento de código?

# a = "A"
# b = "B"
# c = "C"
# d = " "

# lst = [a, b, c, d]
# lst.reverse()

# print(lst)

######################
# Sección 3.6.1.1
######################

# list_1 = [1]

# list_2 = list_1

# list_1[0] = 2

# print(list_2)

######################
# Sección 3.6.1.2
######################

# # Copiando la lista entera.
# list_1 = [1]
# list_2 = list_1[:]
# list_1[0] = 2
# list_2[0] = 37

# print(list_1)
# print(list_2)

# ## Copiando parte de la lista.

# my_list = [10, 8, 6, 4, 2]
# new_list = my_list[1:3]

# print(new_list)

######################
# Sección 3.6.1.3
######################

# # start es el índice del primer elemento incluido en la rebanada.
# # end es el índice del primer elemento no incluido en la rebanada.

# my_list = [10, 8, 6, 4, 2]
# new_list = my_list[1:-1]
# print(new_list)

# # Si start especifica un elemento que se encuentra más allá 
# # del descrito por end (desde el punto de vista inicial de la lista), 
# # la rebanada estará vacía:

# my_list = [10, 8, 6, 4, 2]
# new_list = my_list[-1:1]
# print(new_list)

######################
# Sección 3.6.1.4
######################

# my_list = [10, 8, 6, 4, 2]
# new_list = my_list[:3]
# print(new_list)

# my_list = [10, 8, 6, 4, 2]
# new_list = my_list[3:]
# print(new_list)

######################
# Sección 3.6.1.5
######################

# my_list = [10, 8, 6, 4, 2]
# new_list = my_list[:]
# print(new_list)

# # La instrucción del descrita anteriormente puede eliminar 
# # más de un elemento de la lista a la vez, también puede eliminar rebanadas:
# # Nota: En este caso, la rebanada ¡no produce ninguna lista nueva!

# my_list = [10, 8, 6, 4, 2]
# del my_list[1:3]
# print(my_list)

# # También es posible eliminar todos los elementos a la vez:

# my_list = [10, 8, 6, 4, 2]
# del my_list[:]
# print(my_list)

# # Al eliminar la rebanada del código, su significado cambia dramáticamente.

# # Echa un vistazo:

# my_list = [10, 8, 6, 4, 2]
# del my_list
# print(my_list)


# # La instrucción del eliminará la lista, no su contenido.

# # La función print() de la última línea del código provocará un error de ejecución.

######################
# Sección 3.6.1.6
######################

# my_list = [0, 3, 12, 8, 2]

# print(5 in my_list)
# print(5 not in my_list)
# print(12 in my_list)

######################
# Sección 3.6.1.7
######################

# my_list = [17, 3, 11, 5, 1, 99, 7, 15, 13]
# largest = my_list[0]

# for indice in range(1, len(my_list)):
#     if my_list[indice] > largest:
#         largest = my_list[indice]

# print(largest)


# my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
# largest = my_list[0]

# for elemento in my_list:
#     if elemento > largest:
#         largest = elemento

# print(largest)


# my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
# largest = my_list[0]

# for elemento in my_list[1:]:
#     if elemento > largest:
#         largest = elemento

# print(largest)

######################
# Sección 3.6.1.8
######################

# my_list = ["A","B","C","D","E","F","G"]

# valor_a_buscar = "F"

# for indice in range(len(my_list)):
#     found = (my_list[indice] == valor_a_buscar)
#     if found:
#         break
    
# if found:
#     print("Elemento encontrado en el índice", indice)
# else:
#     print("ausente")

# # Nota:

# # La lista drawn almacena todos los números sorteados.
# # La lista bets almacena los números con que se juega.
# # La variable hits cuenta tus aciertos.

# resultado = [5, 11, 9, 42, 3, 49]
# apuesta = [3, 7, 11, 42, 34, 49]
# aciertos = 0

# for numero in apuesta:        # Se recorre todos los números de la apuesta
#     if numero in resultado:   # Verifica cada numero de nuestra apuesta con los resultados
#         print(numero, end="-")
#         aciertos += 1

# print("\nNúmero de Aciertos:",aciertos)

# # Nota:

# # La lista drawn almacena todos los números sorteados.
# # La lista bets almacena los números con que se juega.
# # La variable hits cuenta tus aciertos.

# resultado = [5, 11, 9, 42, 3, 49]
# apuesta = [3, 7, 11, 42, 34, 49]
# aciertos = 0

# for numero in apuesta:
#     if numero in resultado:
#         aciertos += 1

# print(aciertos)

####################################
# Sección 3.6.1.9 - Laboratorio
####################################

# my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
# new_list = []
# for number in my_list:              # Recorre todos los números de la lista original.
#     if number not in new_list:      # Si el número no aparece dentro de la nueva lista...
#         new_list.append(number)     # ...agregarlo aquí.
# my_list = new_list               # Crea una copia de new_list.
# del new_list
# print("La lista con elementos únicos:")
# print(my_list)

######################
# Sección 3.6.1.10
######################

# # Ejercicio 1

# # ¿Cuál es la salida del siguiente fragmento de código?

# list_1 = ["A", "B", "C"]
# list_2 = list_1
# list_3 = list_2

# del list_1[0]
# del list_2[0]

# print(list_3)


# # Ejercicio 2

# # ¿Cuál es la salida del siguiente fragmento de código?

# list_1 = ["A", "B", "C"]
# list_2 = list_1
# list_3 = list_2

# del list_1[0]
# del list_2

# print(list_3)


# # Ejercicio 3

# # ¿Cuál es la salida del siguiente fragmento de código?

# list_1 = ["A", "B", "C"]
# list_2 = list_1
# list_3 = list_2

# del list_1[0]
# del list_2[:]

# print(list_3)


# # Ejercicio 4

# # ¿Cuál es la salida del siguiente fragmento de código?

# list_1 = ["A", "B", "C"]
# list_2 = list_1[:]
# list_3 = list_2[:]

# del list_1[0]
# del list_2[0]

# print(list_3)

# # Ejercicio 5

# # Inserta in o not in en lugar de ??? para que el código genere el resultado esperado.

# my_list = [1, 2, "in", True, "ABC"]

# print(1 in my_list)  # salida True
# print("A" in my_list)  # salida True
# print(3 not in my_list)  # salida True
# print(False in my_list)  # salida False

######################
# Sección 3.7.1.1
######################

# row = []

# for i in range(8):
#     row.append("peón blanco")
# print(row)


# row = ["peón blanco" for i in range(8)]
# print(row)

# # Ejemplo #1:

# squares = [numero ** 2 for numero in range(10)]
# print(squares)

# # # Ejemplo #2:

# twos = [2 ** i for i in range(8)]
# print(twos)

# # # Ejemplo #3:

# impares = [elemento for elemento in squares if elemento % 2 != 0 ]

# print(impares)

######################
# Sección 3.7.1.2
######################

# tablero = []

# for contador in range(8):
#     fila = [contador for contador in range(8)]
#     # print("Contador:",contador,"-",fila)
#     tablero.append(fila)

# print(tablero)

# Ejemplo de relleno e impresión 

# filas = int(input("¿Cuántas filas quieres crear? "))
# columnas = int(input("¿Cuántas columnas quieres crear? "))

# matriz = []

# for fila in range(filas):
#     matriz.append([])               # crea una lista vacía por cada fila

#     for columna in range(columnas):
#         matriz[fila].append(str(fila) + "-" + str(columna))

# # print(matriz)

# #  Impresión de la matriz con formato

# for fila in range(len(matriz)):
#     print() 
#     for columna in range(len(matriz[fila])):
#         print(matriz[fila][columna], end =" ")

# #  Alternativa

# import pprint

# board = []

# for i in range(8):
#     row = ["EMPTY" for i in range(8)]
#     board.append(row)

# pprint.pprint(board)

######################
# Sección 3.7.1.3
######################

# EMPTY = "XXXXXXXX"
# PAWN = "PEON"
# ROOK = "TORRE"
# KNIGHT = "CABALLO"
# board = []

# for i in range(8):
#     row = [EMPTY for i in range(8)]
#     board.append(row)

# board[0][0] = ROOK
# board[0][7] = ROOK
# board[7][0] = ROOK
# board[7][7] = ROOK
# board[7][1] = KNIGHT
# board[7][6] = KNIGHT
# board[7][2] = "ALFIL"
# board[7][5] = "ALFIL"
# board[7][3] = "REINA"
# board[7][4] = "REY"

# # print(board)

# for row in board:
#     print()
#     for cell in row:
#         print(format(cell,"8"), end =" ")

# Alternativa

# import pprint

# EMPTY = "-"
# PAWN = "PEON"
# ROOK = "TORRE"
# KNIGHT = "CABALLO"
# board = []

# for i in range(8):
#     row = [EMPTY for i in range(8)]
#     board.append(row)

# board[0][0] = ROOK
# board[0][7] = ROOK
# board[7][0] = ROOK
# board[7][7] = ROOK

# pprint.pprint(board)

######################
# Sección 3.7.1.4
######################

# import random

# temps = [[0.0 for h in range(24)] for d in range(31)]

# total = 0.0

# # # Rellenar con valores aleatorios

# for fila in range(len(temps)):
#     for columna in range(len(temps[fila])):
#         temps[fila][columna] = random.choice(range(10, 450))/10


# for day in temps:
#     total += day[11] # Las 12:00 horas

# average = total / 31

# print("Temperatura promedio al mediodía:", round(average,1), "grados centígrados")
        
# # Imprimir lista con formato

# for fila in range(len(temps)):
#     print("\nDía", fila + 1)
#     for columna in range(len(temps[fila])):
#         print(temps[fila][columna], end = "  ")
     

# print()
# highest = -100.0

# for day in temps:
#     for temp in day:
#         if temp > highest:
#             highest = temp
            
# print("La temperatura más alta fue de", highest, "grados")


# #  Días con temperatura superior a 20 grados a las 12 del mediodía

# hot_days = 0

# for day in temps:
#     if day[11] > 20.0:
#         hot_days += 1

# print(hot_days, "fueron los días calurosos.")

######################
# Sección 3.7.1.5
######################

# rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]

# rooms[1][9][13] = True

# rooms[0][4][1] = False

# ##  Habitaciones ocupadas en la planta 15 del tercer hotel

# rooms[2][14][0] = True    # Hotel 3, Planta 15, Habitación 1
# rooms[2][14][1] = True    # Hotel 3, Planta 15, Habitación 2

# vacancy = 0

# #  Número de habitaciones libres en la planta 15 del tercer hotel

# for room_number in range(20):
    # if not rooms[2][14][room_number]:
#         vacancy += 1

# print("Hay", vacancy, "habitaciones libres en la planta 15 del tercer hotel")

######################
# Sección 3.7.1.6
######################

# # Este es un ejemplo de una comprensión de lista:
# # el código siguiente crea una lista de cinco elementos 
# # con los primeros cinco números naturales elevados a la potencia de 3:

# cubed = [num ** 3 for num in range(5)]
# print(cubed)  # outputs: [0, 1, 8, 27, 64]

# #  Una tabla de cuatro columnas y cuatro filas: un arreglo bidimensional (4x4)

# table = [[":(", ":)", ":(", ":)"],
#          [":)", ":(", ":)", ":)"],
#          [":(", ":)", ":)", ":("],
#          [":)", ":)", ":)", ":("]]

# print(table)
# print(table[0][0])  # outputs: ':('
# print(table[0][3])  # outputs: ':)'



# # Cubo - un arreglo tridimensional (3x3x3)

# cube = [[[':(', 'x', 'x'],
#          [':)', 'x', 'x'],
#          [':(', 'x', 'x']],

#         [[':)', 'x', 'x'],
#          [':(', 'x', 'x'],
#          [':)', 'x', 'x']],

#         [[':(', 'x', 'x'],
#          [':)', 'x', 'x'],
#          [':)', 'x', 'x']]]

# print(cube)
# print(cube[0][0][0])  # outputs: ':('
# print(cube[2][2][0])  # outputs: ':)'
