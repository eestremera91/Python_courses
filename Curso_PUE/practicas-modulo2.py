"""
@author: cesar.martin@numaconsulting.com
"""

# print("Hola Mundo!")

#######################
#   Sección 2.1.1.1
#######################

# print("¡Hola, Mundo!")

# help(print)

#######################
#   Sección 2.1.1.4
#######################

# print("¡Hola,", "Mundo!", "- ESTO", 10, 12.34, "ES", "UN", "alpha7", 'DE', "PASO", "DE", "PARAMETROS")
# print()
# print(123456)

#################################
#   Sección 2.1.1.7 - Laboratorio
#################################

# Utiliza la función print() para imprimir la linea "¡Hola, Mundo!" en la pantalla.

# print("¡Hola Mundo!")

# Una vez hecho esto, utiliza la función print() nuevamente, pero esta vez imprime tu nombre.

# print("César Martín")

# Elimina las comillas dobles y ejecuta el código. Observa la reacción de Python. ¿Qué tipo de error se produce?

# falla
# print(César Martín)

# Luego, elimina los paréntesis, vuelve a poner las comillas dobles y vuelve a ejecutar el código. ¿Qué tipo de error se produce esta vez?

# falla
# print"César Martín"

# Experimenta tanto como puedas. Cambia las comillas dobles a comillas simples, utiliza múltiples funciones print() en la misma línea y luego en líneas diferentes. Observa que es lo que ocurre.

# falla
# print'César Martín'

# print("uno")
# print("dos")
# print("tres")

# falla
# print("uno"); print("dos"), print("tres")

#######################
# Sección 2.1.1.8
#######################

# help(print)

# sentencia original
# print("La Witsi Witsi Araña subió a su telaraña.")
# print()
# print("Vino la lluvia y se la llevó.")

# print("La Witsi Witsi Araña subió a su telaraña.")   
# print("\nVino la lluvia y se la llevó.")

# print("La Witsi Witsi Araña subió a su telaraña." \
# "\n\nVino la lluvia y se la llevó.")

# print()

# # dos cadenas diferentes sin separar con comas
# print("La Witsi Witsi Araña subió a su telaraña." \
# "Vino la lluvia y se la llevó.")

# # # print()

# # # dos cadenas diferentes separadas por comas
# print("La Witsi Witsi Araña subió a su telaraña.", \
# "Vino la lluvia y se la llevó.")
    
# # # print()
    
# # # una sola cadena dividida en dos lineas
# print("La Witsi Witsi Araña subió a su telaraña.\
# Vino la lluvia y se la llevó.")

#######################
# Sección 2.1.1.9
#######################

# print("La Witsi Witsi Araña subió a su telaraña.")
# print()
# print("Vino la lluvia y se la llevó.")

#######################
# Sección 2.1.1.10
#######################

# print("La Witsi Witsi Araña subió a su telaraña.")
# print()    
# print("Vino la lluviay se la llevó.")

# print("La Witsi Witsi Araña\nsubió a su telaraña.\n")
# print()    
# print("Vino la lluvia\ny se la llevó.")
                    
# print("La Witsi Witsi Araña\n\
# subió a su telaraña.\n\n\n\
# Vino la lluvia\ny se la llevó.")

# print("""
# La Witsi Witsi Araña
# subió a su telaraña.


# Vino la lluvia
# y se la llevó.
# """)

# help(print)


# print("hola","\n","adios")

# print("hola",chr(10),"adios")

# print("La Witsi Witsi Araña\tsubió a su telaraña.\n")
# print("1\t2\t3\t4\t5\t6\t7\t")    
# print("Vino la lluvia\t\t\ty se la llevó.")

#######################
# Sección 2.1.1.11
#######################

#print("\\") # duplicar para imprimir el caracter de escape

#######################
# Sección 2.1.1.12
#######################

# print("La Witsi Witsi Araña" , "subió" , "a su telaraña.")

# # sin comas
# print("La Witsi Witsi Araña"  "subió"  "a su telaraña.") 

# print("La Witsi Witsi Araña" ,  
# "subió" , 
# "a su telaraña.")

# print("La Witsi Witsi Araña" ,  \
#   "subió" , \
#   "a su telaraña.")

# # sin comas
# print("La Witsi Witsi Araña"  \
#  "subió"  \
#  "a su telaraña.")

#######################
# Sección 2.1.1.13
#######################

# print("Mi nombre es","Python.")
# print("Monty Python.")

#######################
# Sección 2.1.1.14
#######################

# help(print)

# print("Mi nombre es", "Python.")
# print("Monty Python.")

# print("Mi nombre es", "Python.", end="***\n****", sep ="_")
# print("Monty Python.")

#######################
# Sección 2.1.1.15
#######################

# print("Mi nombre es ", end="") # end = nada
# print("Monty Python.")

#######################
# Sección 2.1.1.16
#######################

# print("hola","clase","otro mensaje" , sep = str(12345))
# print("curso")

# print("Mi", "nombre", "es", "Monty", "Python.", sep="-")

#######################
# Sección 2.1.1.17
#######################

# print("Mi", "nombre", "es", sep="_", end="*")
# print("Monty", "Python.", sep="*", end="*\n")

#####################################
# Sección 2.1.1.19 - Laboratorio
#####################################

# Modificar las siguientes líneas para conseguir éste resultado: 
    
# Fundamentos***Programación***en...Python

# print("Fundamentos","Programación","en")
# print("Python")

# solución

# print("Fundamentos","Programación","en", sep="***", end="...")
# print("Python")

#####################################
# Sección 2.1.1.20 - Laboratorio
#####################################

# print("    *")
# print("   * *")
# print("  *   *")
# print(" *     *")
# print("***   ***")
# print("  *   *")
# print("  *   *")
# print("  *****")

# minimizar el número de invocaciones de la función print

# solucion 1

# print("\
#       *\n\
#      * *\n\
#     *   *\n\
#    *     *\n\
#   ***   ***\n\
#     *   *\n\
#     *   *\n\
#     *****")

# solución 2

# print("     *     ",      
#       "    * *    ",     
#       "   *   *   ",    
#       "  *     *  ",   
#       " ***   *** ",  
#       "   *   *   ",    
#       "   *   *   ",    
#       "   *****   ",    
#       sep="\n")

# solución 3

# print("    *",      
#       "   * *",     
#       "  *   *",    
#       " *     *",   
#       "***   ***",  
#       "  *   *",    
#       "  *   *",    
#       "  *****",    
#       sep="\n")

# hacer la flecha dos veces más grande pero mantener las proporciones

# print(
#     "        *         " ,
#     "       * *        " ,
#     "      *   *       " ,
#     "     *     *      " ,
#     "    *       *     " ,
#     "   *         *    " ,
#     "  *           *   " ,
#     " *             *  " ,
#     "******     ****** " ,
#     "     *     *      " ,
#     "     *     *      " ,
#     "     *     *      " ,
#     "     *     *      " ,
#     "     *******      " ,
#     sep="\n")


# print("""
#             *         
#            * *        
#           *   *       
#          *     *      
#         *       *     
#        *         *    
#       *           *   
#      *             *  
#     ******     ****** 
#          *     *      
#          *     *      
#          *     *      
#          *     *      
#          *******      """)

# Duplicar la flecha, colocando ambas flechas lado a lado

# print("    *     " * 2 ,
#       "   * *    " * 2 ,
#       "  *   *   " * 2 ,
#       " *     *  " * 2 ,
#       "***   *** " * 2 ,
#       "  *   *   " * 2 ,
#       "  *   *   " * 2 ,
#       "  *****   " * 2 ,
#       sep="\n")

#######################
# Sección  2.1.2.2
#######################

# print("2" * 5)
# print(2 * 5)

# print(type("2"))
# print(type(2))

#######################
# Sección  2.1.2.3
#######################

# print(123456789 + 1)
# print(1_23_45_67_89 +1)

# El uso de _ para literales numéricos está disponible a partir de Python 3.6

# print(+11_111_111.999_99)

# print(-11_111_111.999_99)

# print(11_111_111  ,  999_99) # esto son dos parámetros distintos

#######################
# Sección  2.1.2.4
#######################

# Octal

# Calculadora online:
# https://www.calculadoras.uno/binario-decimal/___123_en_octal_

# print(0o123)    # en decimal = 83

# Hexadecimal

# print(0x123)    # en decimal = 291

#######################
# Sección  2.1.2.5
#######################

# print(2.5)
# print(2,5) # cuidado con la coma!!

# print(0.4)
# print(.4) # equivalente

# print(-0.4)
# print(-.4) # equivalente

# print(.4)
# print(0.4) # equivalente

# print(4.)
# print(4.0) # equivalente

#######################
# Sección  2.1.2.6
#######################

# print(300_000_000.0)
# print(3e8)
# print(3E8)
# print(3 * 10. ** 8)

# print(0.000000000000000000000000000000000000000000000000000000000076654)
# print(7.6654e-59)

# print(4)
# print(4.0)

# consumo de memoria
# import sys
 
# print(sys.getsizeof(4), end = " bytes (entero)\n")
# print(sys.getsizeof(4.0), end = " bytes (flotante)\n")

# print(sys.getsizeof(""), end = " bytes (por defecto para cadenas vacías)\n")
# print(sys.getsizeof("a"), end = " bytes\n")
# print(sys.getsizeof("ab"), end = " bytes\n")
# print(sys.getsizeof("abc"), end = " bytes\n")
# print(sys.getsizeof("abcd"), end = " bytes\n")
# print(sys.getsizeof("abcde"), end = " bytes\n")
# print(sys.getsizeof("abcdef"), end = " bytes\n")

# print("Velocidad de la luz=",300000000)         # notación decimal
# print("Velocidad de la luz=",3E8)               # notación exponencial (E mayúscula)
# print("Velocidad de la luz=",3e8)               # notación exponencial (e minúscula)
# print("Velocidad de la luz=",3 * 10**8)         # equivalente al ejemplo anterior

#######################
# Sección  2.1.2.7
#######################

# 6.62607 x 10 elevado a -34

# print("Constante de Plank=", 6.62607E-34)       # notación exponencial
# print("Constante de Plank=", 6.62607 * 10**-34) # equivalente al ejemplo anterior

# print(0.0000000000000000000001) # 1e-22
# print(1e-22)

#######################
# Sección  2.1.2.8
#######################

# codificar comillas dentro de cadenas (strings)

# print("Me gusta \"Monty Python\"")

# print('Me gusta "Monty Python"')

#######################
# Sección  2.1.2.9
#######################

# print('I\'m Monty Python.')     # con escape
# print("I'm Monty Python.")      # sin escape

# print("""I'm Monty Python.""")  # sin escape
# print('''I'm Monty Python.''')  # sin escape

# print("I","m Monty Python.",sep="'")  # sin escape pero con sep

#######################
# Sección  2.1.2.10
#######################

# print(True)
# print(False)

# print("Valor True en número:" , int(True))
# print("Valor False en número:" , int(False))

# print("True > False =", True > False)
# print("True < False =", True < False)

# print("1 > False =", 1 > False)

# print(True - False + True)

# print("1 > 2 =", 1 > 2)
# print("1 < 2 =", 1 < 2)

# print("0 > True =", 0 > True)
# print("0 < False =", 0 < False)

#######################
# Sección 2.1.2.11
#######################

# print('"Estoy"',
#       '""aprendiendo""',
#       '"""Python"""', 
#       sep = '\n')

# print()

# print("\"Estoy\"",
#       "\"\"aprendiendo\"\"",
#       "\"\"\"Python\"\"\"",
#       sep = "\n")

# print()

# print('''"Estoy"
# ""aprendiendo""
# """Python"""''')

# print()

# print('''\"Estoy"''',
# '''\"\"aprendiendo""''',
# '''\"""Python"""''', sep="\n")

# print('"Estoy"\n""aprendiendo""\n"""Python"""')

# print('"Estoy"\n','""aprendiendo""\n','"""Python"""')

# print('"Estoy"','""aprendiendo""','"""Python"""', sep = "\n")

# print('''""Estoy""\n""aprendiendo""\n"""Python"""''')

# print("\"Estoy\"", "\"\"aprendiendo\"\"", "\"\"\"Python\"\"\"", sep="\n")

# print(1*'"' + "Estoy"+1*'"' , 2 * '"' + "aprendiendo" + 2 * '"' , 3 * '"' + "python" + 3 * '"' ,sep="\n")

#######################
# Sección 2.1.2.12
#######################

# https://www.rapidtables.org/convert/number/binary-to-decimal.html

# 1011 en decimal?

# Multiplicar cada dígito del número binario por la potencia de 2 correspondiente:
    
#    1        0       1        1
# 1*2**3 + 0*2**2 + 1*2**1 + 1*2**0

# Resolver las potencias
    
# 1*8 + 0*4 + 1*2 + 1*1 = 8 + 0 + 2 + 1

# y sumar:
    
# 8 + 0 + 2 + 1 = 11.

#######################
# Sección 2.1.3.1
#######################

# print("3+2 =", 3+2)     # suma
# print("3-2 =", 3-2)     # resta
# print("3*2 =", 3*2)     # producto
# print("3/2 =", 3/2)     # división
# print("3//2 =", 3//2)   # floor division (división entera o redondeando hacia abajo)
# print("11%2 =", 11%2)   # resto de la división
# print("3**2 =", 3**2)   # elevado a

#######################
# Sección 2.1.3.2
#######################

# print(2 ** 3)
# print(2 ** 3.2)
# print(2. ** 3)
# print(2. ** 3.)

#######################
# Sección 2.1.3.3
#######################

# print(2 * 3)
# print(2 * 3.)
# print(2. * 3)
# print(2. * 3.)

# # con divisiones el resultado siempre es flotante!!!!

# print(6 / 3)
# print(6 / 3.)
# print(6. / 3)
# print(6. / 3.)

#######################
# Sección 2.1.3.4
#######################

# división entera (redondeando hacia abajo)

# print(7 // 3)
# print(7 // 3.)
# print(7. // 3)
# print(7. // 3.)

# print(7 // 4)
# print(7. // 4)

#######################
# Sección 2.1.3.5
#######################

# resto

# print("Resto de la división 14/4:", 14 % 4)

# print("Resto de la división 12/4.5:",12 % 4.5)

# # errores al operar con cero

# print(2 / 0)  # ZeroDivisionError: division by zero
# print(2 // 0) # ZeroDivisionError: division by zero
# print(2 % 0)  # ZeroDivisionError: division by zero

#######################
# Sección 2.1.3.6
#######################
# print(-4 - 4)
# print(4. - 8)
# print(-1.1)

# print(-4 + 4)
# print(-4. + 8) # resultado decimal!!

# print(-1.1) # operador unario
# print(+2)   # operador unario

#######################
# Sección 2.1.3.7
#######################

# print(2 + 3 * 5) # primero el producto y después la suma

# print(9 % 6 % 2) # enlazado del lado izquierdo!!!

#######################
# Sección 2.1.3.8
#######################

# print(2 ** 2 ** 3) # el operador exponencial utiliza enlazado del lado derecho!!!!!! 2 ** 3 → 8; 2 ** 8 → 256
# explicación --> 2 ** 3 → 8; 2 ** 8 → 256

#######################
# Sección 2.1.3.9
#######################

# Prioridad	Operador	
# 1	+, -	 unario
# 2	**                 
# 3	*, /, //, %	
# 4	+, -	 binario

# print(2 * 3 % 5)

# print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)
#     (5 * ((   12  ) + 100) / (  26  )) // 2)
#     (5 * (      112      ) / (  26  )) // 2)
#     (           560        /    26   ) // 2)
#                   21.5384615           // 2 # floor division!!
#                       10.0

#######################
# Sección 2.1.3.10
#######################

# print((2 ** 4), (2 * 4.), (2 * 4))
#         16   ,    8.0  ,     8      

# print((-2 / 4), (2 / 4), (2 // 4), (-2 // 4))
#         -0.5  ,   0.5  ,    0    ,    -1

# print((2 % -4), (2 % 4), (2 ** 3 ** 2))

#######################
# Sección 2.1.4.3
#######################

# help("keywords")

# convenciones de nomenclatura
# https://cosasdedevs.com/posts/convencion-nombres-python/

# var = 1

# print(type(var)) # comprobar qué tipo de dato almacena var?

# print(var)

# var = "Cadena"

# print(type(var))

# print(var)

# var = 1.0

# print(type(var))

# print(var)

# var = True

# print(type(var))

# print(var)

#######################
# Sección 2.1.4.4
#######################

# var = 1
# account_balance = 1000.0
# client_name = 'John Doe'

# print(var, account_balance, client_name)
# print(var)

# var = 1
# print(Var)  # Error!!

# var = "3.8.5"
# print("Versión de Python: " + var)

# numero = 1.5
# print("Numero: " + numero) # concatenación --> Falla!!!

# print("Número: " + str(numero)) # str()

# print("Número:", numero) # dos argumentos, conversión automática de la variable a string

#######################
# Sección 2.1.4.5
#######################

# var = 1
# print(var)

# var = var + 1
# print(var)

# var += 1        # EQUIVALENTE!!
# print(var)

# var = 100
# var = 200 + 300
# print(var)

#######################
# Sección 2.1.4.6
#######################

# El cuadrado de la hipotenusa es igual 
# a la suma de los cuadrados de los dos catetos.

# a = 3.0
# b = 4.0
# c = (a ** 2 + b ** 2) ** 0.5

# print("c =", c)

###################################
# Sección 2.1.4.7 - Laboratorio
###################################

# Crear las variables: juan, maria, y adan.
# Asignar valores a las variables. 
# El valor debe de ser igual al número de manzanas que cada quien tenía.

# juan = 3; maría = 5; adán = 6

# Una vez almacenados los números en las variables, 
# imprimir las variables en una línea, 
# y separar cada una de ellas con una coma.

# print(juan, maría, adán, sep=", " )

# print(str(juan) + ", " + str(maría) + ", " + str(adán))

# print(juan,", ",maría,", ",adán, sep ="")

# Después se debe crear una nueva variable llamada total_manzanas 
# y se debe igualar a la suma de las tres variables anteriores.

# total_manzanas = juan + maría + adán

# Imprime el valor almacenado en total_manzanas en la consola.

# print(total_manzanas)

# Experimenta con tu código: crea nuevas variables, asigna diferentes valores a ellas, y realiza varias operaciones aritméticas con ellas (por ejemplo, +, -, *, /, //, etc.). Intenta poner una cadena con un entero juntos en la misma línea, por ejemplo, "Número Total de Manzanas:" y total_manzanas.

# print("Número total de manzanas:", total_manzanas)

# print("Número total de manzanas: " + str(total_manzanas))

#######################
# Sección 2.1.4.8
#######################

# x = 2
# x = x * 2
# x *= 2

# x = x + 1
# x += 1

# print(x)

# i = 1
# var = 1
# rem = 1
# j = 1
# x = 1

# i = i + 2 * j
# i += 2 * j # equivalente

# var = var / 2
# var /= 2 # equivalente

# rem = rem % 10
# rem %= 10 # equivalente

# j = j - (i + var + rem)
# j -= (i + var + rem) # equivalente

# x = x ** 2
# x **= 2 # equivalente

# UnaVariableConNombreMuyLargo = 17

# UnaVariableConNombreMuyLargo = UnaVariableConNombreMuyLargo + 1
# UnaVariableConNombreMuyLargo += 1

###################################
# Sección 2.1.4.9 - Laboratorio
###################################

# Millas y kilómetros son unidades de longitud o distancia.

# Teniendo en mente que 1 milla equivale aproximadamente 
# a 1.61 kilómetros, complementa el programa en el editor 
# para que convierta de:
    
# Millas a kilómetros.
# Kilómetros a millas.
# No se debe cambiar el código existente. 
# Escribe tu código en los lugares indicados con  ###. 
# Prueba tu programa con los datos que han sido provistos 
# en el código fuente.


# Pon mucha atención a lo que esta ocurriendo dentro de la 
# función print(). Analiza como es que se proveen múltiples 
# argumentos para la función, y como es que se muestra el resultado.

# Nota que algunos de los argumentos dentro de la función print() 
# son cadenas (por ejemplo "millas son", y otros son variables 
# (por ejemplo miles).

# Resultado esperado:
# 7.38 millas son 11.88 kilómetros
# 12.25 kilómetros son 7.61 millas

# regla de tres para calcular el valor de la siguiente variable
# 1.61 -> 1
# 1 -> x
# calculado como 1*1 / 1.61 = 0.62

# kilometers = 12.25
# miles = 7.38

# miles_to_kilometers = 1.61
# kilometers_to_miles = 0.621371

# print(miles, "millas son", round(miles_to_kilometers * miles, 2), "kilómetros")
# print(kilometers, "kilómetros son", round(kilometers_to_miles * kilometers, 2), "millas")


# Solución 2

# kilometers = 12.25
# miles = 7.38

# miles_to_kilometers = (miles * 1.61)
# kilometers_to_miles = (kilometers / 1.61)

# print(miles, "millas son", round(miles_to_kilometers, 2), "kilómetros")
# print(kilometers, "kilómetros son", round(kilometers_to_miles, 2), "millas")

# convertidor de dolar-euro

# cotizacion_actual_dolar = 1.1

# euros = 1
# dolares = 1

# dolar_a_euro = dolares * cotizacion_actual_dolar
# euro_a_dolar = euros / cotizacion_actual_dolar

# print (euros , "euros son", round(euro_a_dolar, 3), "dólares")
# print (dolares, "dólares son", round(dolar_a_euro, 3), "euros")

###################################
# Sección 2.1.4.10 - Laboratorio
###################################

# Tu tarea es completar el código para evaluar la siguiente expresión:

# 3 * x elevado a 3 - 2 * x elevado a 2 + 3 * x -1

# El resultado debe ser asignado a y.

# Entrada de Muestra

# x = 0
# x = 1
# x = -1

# Salida Esperada

# y = -1.0
# y = 3.0
# y = -9.0

# Solución

# x = 0
# x = float(x)
# y = (3 * x ** 3) - (2 * x ** 2) + (3 * x -1)

# print("y =", y)

########################
# Sección 2.4.1.11
########################

# var = "007"
# print("Agente " + var)

# var = 1007
# print("Agente " + var) # TypeError: can only concatenate str (not "int") to str

# ¿Cuál es el resultado del siguiente fragmento de código?

# var = 2
# var = 3
# print(var) # resultado 3

# ¿Cuáles de los siguientes nombres de variables son ilegales en Python?


# my_var
# m
# 101 # ilegal, no puede empezar con dígitos
# averylongvariablename
# m101
# m 101 # ilegal, espacio en blanco
# Del
# del # ilegal, palabra reservada!!

# ¿Cuál es el resultado del siguiente fragmento de código?

# a = '1'
# b = "1"
# print(a + b) # 11 (operador + con cadenas = concatenación)

# ¿Cuál es el resultado del siguiente fragmento de código?

# a = 6
# b = 3

# a /= 2 * b      # Precedencia de operadores, primero el producto, después la división

# print(a)

# restaurando variables con sus valores originales
# a = 6
# b = 3

# a = a / (2 * b) # Esto es equivalente!!!

# print(a)

# restaurando variables con sus valores originales
# a = 6
# b = 3

# a = a / 2 * b   # Esto no es equivalente!!!

# print(a) 

########################
# Sección 2.1.5.1
########################

# Esto es un comentario de Python

# """ 
#     Esto es otro comentario de Python,
#     útil para comentar múltiples líneas.
    
#     Hay que tener en cuenta que se trata realmente de una cadena
#     de caracteres que no ha sido asignada a ninguna variable, 
#     por ese motivo la herramienta lo muestra resaltado en verde.
    
#     Puede resultar algo incómodo al depurar código, porque Python
#     lo detecta como una instrucción, no un comentario.
# """

# print(123) # Este es otro comentario al final de la instrucción

# print(123) """ Este es otro comentario al final de la instrucción
# que continúa en la siguiente línea y falla"""

###################################
# Sección 2.1.5.2 - Laboratorio
###################################

# este programa calcula los segundos en cierto número de horas determinadas 
# este programa fue escrito el día 21 de Noviembre de 2022
# autor: cesar.martin@numaconsulting.com

# numero_horas = 2                                                # número de horas
# numero_segundos = 3600                                          # número de segundos en una hora

# print("Horas: ", numero_horas)                                  # imprime el numero de horas
# print("Segundos en Horas: ", numero_horas * numero_segundos)    # se imprime el numero de segundos en determinado numero de horas

# print("Adiós")

# este el es fin del programa que calcula el numero de segundos en 2 horas

########################
# Sección 2.1.5.3
########################

# ¿Cuál es la salida del siguiente fragmento de código?

## print("Cadena #1")
# print("Cadena #2")

# ¿Qué ocurrirá cuando se ejecute el siguiente código?

# # Esto es
# un comentario # SyntaxError: invalid syntax
# en varias líneas #

# print("¡Hola!")

########################
# Sección 2.1.6.1
########################

# print("Dime algo...")

# valor_introducido = input()

# print("Mmm...", valor_introducido, "...¿en serio?")

########################
# Sección 2.1.6.2
########################

# anything = input("Dime algo...\n")
# print(type(anything))
# print("Mmm...", anything, "...¿En serio?")

# anything = input("Inserta un número: ")
# something = anything ** 2.0                    # TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'float'
# print(anything, "al cuadrado es", something)

########################
# Sección 2.1.6.3
########################

# anything = input("Inserta un número: ")
# something = anything ** 2.0 # TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'float'
# print(anything, "al cuadrado es", something)

########################
# Sección 2.1.6.4
########################

# anything = float(input("Inserta un número: "))
# something = anything ** 2.0
# print(anything, "al cuadrado es", something)

########################
# Sección 2.1.6.5
########################

# leg_a = float(input("Inserta la longitud del primer cateto: "))
# leg_b = float(input("Inserta la longitud del segundo cateto: "))
# hypo = (leg_a**2 + leg_b**2) ** .5
# print("La longitud de la hipotenusa es:", hypo)

########################
# Sección 2.1.6.6
########################

# Concatenación de cadenas con + 

# fnam = input("¿Me puedes dar tu nombre por favor? ")
# lnam = input("¿Me puedes dar tu apellido por favor? ")
# print("Gracias.")
# print("\nTu nombre es " + fnam + " " + lnam + ".")

########################
# Sección 2.1.6.7
########################

# Replicación con * para cadenas

# print("+" + 10 * "-" + "+")
# print(("|" + " " * 10 + "|\n") * 5, end="")
# print("+" + 10 * "-" + "+")

# con variables

# anchura = int(input("Introduce la anchura del rectángulo: "))
# altura = int(input("Introduce la altura del rectángulo: "))

# print("+" + anchura * "-" + "+")
# print(("|" + " " * anchura + "|\n") * altura, end="")
# print("+" + anchura * "-" + "+")

########################
# Sección 2.1.6.8
########################

# leg_a = float(input("Inserta la longitud del primer cateto: "))
# leg_b = float(input("Inserta la longitud del segundo cateto: "))

# print("La longitud de la hipotenusa es " + str((leg_a**2 + leg_b**2) ** .5))
# print("La longitud de la hipotenusa es", (leg_a**2 + leg_b**2) ** .5)

#####################################
# Sección 2.1.6.9 - Laboratorio
#####################################

# # ingresa un valor flotante para la variable numero1 aquí
# numero1 = float(input("Ingresa el valor para numero1: "))

# # ingresa un valor flotante para la variable numero2 aquí
# numero2 = float(input("Ingresa el valor para numero2: "))

# print()

# # muestra el resultado de la suma aquí 
# # (llamando a str() y concatenando)
# print("La suma de " + str(numero1) + " y " + str(numero2) + " es igual a " + str(numero1 + numero2))

# # muestra el resultado de la resta aquí
# # (pasando distintos parámetros separados por comas)
# print("La resta de", numero1, "-", numero2, "es igual a", numero1 - numero2)

# # muestra el resultado de la multiplicación aquí
# # (llamando a str() y concatenando)
# print("El producto " + str(numero1) + " por " + str(numero2) + " es igual a " + str(numero1 * numero2))

# muestra el resultado de la división aquí
# (pasando distintos parámetros separados por comas)
# print("La división de", numero1, "/", numero2, "es igual a", numero1 / numero2)

# print("\n¡Eso es todo, amigos!")

#####################################
# Sección 2.1.6.10 - Laboratorio
#####################################

# x = float(input("Ingresa el valor para x: "))

# resultado = 1 / ( x + 1 / ( x + 1 / (x + ( 1 / x))))

# # David
# # resultado = 1 / (1 / (1 / (1 / x + x) + x) + x)

# print("Resultado =", resultado)

#####################################
# Sección 2.1.6.11 - Laboratorio
#####################################

# hora_inicial = int(input("Hora de inicio (horas): "))
# minutos_iniciales = int(input("Minuto de inicio (minutos): "))
# duracion = int(input("Duración del evento (minutos): "))

# # print("Hora inicial: " + str(hora_inicial) + ":" + str(minutos_iniciales))

# # coloca tu código aqui
# total_minutos = minutos_iniciales + duracion 

# # print("Total minutos:", total_minutos)

# minutos_finales = total_minutos % 60 # resto de la división

# # print("Minutos finales: " + str(minutos_finales))

# horas_adicionales = total_minutos // 60 # división entera

# # print("Horas adicionales:",horas_adicionales )

# hora_final = hora_inicial + horas_adicionales

# # ¿Necesitamos realmente esta variable?
# hora_final_de_0_a_24 = hora_final % 24 # por si nos pasamos de las 24 horas!!

# print(str(hora_final_de_0_a_24) + ":" + str(minutos_finales))


# solución con menos variables

# horas_iniciales = int(input("Hora de inicio (horas): "))
# minutos_iniciales = int(input("Minuto de inicio (minutos): "))
# duracion = int(input("Duración del evento (minutos): "))

# print((horas_iniciales + ((duracion + minutos_iniciales) // 60)) % 24,':',
#       (duracion + minutos_iniciales) % 60,sep='')

########################
# Sección 2.1.6.12
########################

# ¿Cuál es la salida del siguiente código?

# x = int(input("Ingresa un número: ")) # El usuario ingresa un 2 
# print(x * "5")

# ¿Cuál es la salida del siguiente código?

# x = input("Ingresa un número: ") # El usuario ingresa un 2 
# print(type(x))


