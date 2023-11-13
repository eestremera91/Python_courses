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
