
import math, random

def run():
    lista1 = [1,2]

    lista1[1] = lista1[0]


    lista2 = lista1

    lista2.append(2 - lista1[0])

    lista1.append(lista1[2] + 1)
    print(lista1)

    # hora = int(input("Hora de inicio (horas): "))
    # min  = int(input("Minuto de inicio (minutos): "))
    # dura = int(input("Duración del evento (minutos): "))

    # min_to_hour_int     = (min+dura)//60
    # min_to_hora_resto   = (min+dura)%60
    # horas_total         = hora + min_to_hour_int
    # horas_resto         = horas_total%24
    # print("Salida esperada: "+str(horas_resto)+":"+str(min_to_hora_resto))
    # print(f'Salida esperada: {horas_resto:02}:{min_to_hora_resto:02}')   #si tiene un solo dígito lo lleva a formato 00

    # nombre = "Alicia"
    # edad = 35.4
    # print(f"Me llamo {nombre:05} y tengo {edad:05} años.")
    # for i in range(10):
    #     pass
    # print(i)
    # bloques_disponibles = int(input("Entre la cantidad de bloques: "))
    # capas               = 0
    # bloques_per_capas   = 0
    # while bloques_per_capas <= bloques_disponibles:
    #      bloques_per_capas    += 1
    #      bloques_disponibles  -= bloques_per_capas
    #      capas                += 1

    # print("La altura de la pirámide es: ",capas, " y sobran ",bloques_disponibles)
    # numero = 0
    # while numero < 1:
    #     numero = int(input('Introduzca un número positivo: '))
    # pasos = 0
    # while numero != 1:
    #     if numero%2 == 0:
    #         numero = numero//2
    #     else:
    #         numero = 3*numero + 1
    #     print(numero)
    #     pasos += 1
    # print("pasos = ", pasos)

    # numero = 0
    # pasos  = 0
    # while True:
    #     if numero < 1: 
    #        numero = int(float(input('Introduzca un número positivo: ')))
    #        continue
    #     elif numero == 1:
    #        break
    #     else:  
    #         if numero%2 == 0:
    #             numero = numero//2
    #         else:
    #             numero = 3*numero + 1
    #         print(numero)
    #         pasos += 1
    # print("pasos = ", pasos)
    # numeros = []
    # for indice in range(1,1001):
    #     numeros.append(indice)


    # print(numeros)

    # beatles_members = []
    # beatles_members.append('John Lennon')
    # beatles_members.append('Poul McCartney')
    # beatles_members.append('George Harrison')
    # print('los miembros de los Beatles son: ',beatles_members)

    # for i in range(2):
    #    new_integrante = input('agregue el nombre del nuevo miembro: ')
    #    beatles_members.append(new_integrante)
    # print('los miembros de los Beatles son: ',beatles_members)  
    # del(beatles_members[3])
    # beatles_members.pop()
    # print('los miembros de los Beatles son: ',beatles_members)  
    # beatles_members.insert(len(beatles_members),'Ringo')
    # print('los miembros de los Beatles son: ',beatles_members) 



    # def invertircadena(cadena_objetivo):
    #     return cadena_objetivo[::-1]

    # cadena           = input("introduzca la cadena: ")
    # cadena_invertida = invertircadena(cadena)
    # print("La cadena invertida: ",cadena_invertida)
    #tupla = ('hola',2,"de")

    # from platform import machine,processor, system, version, uname
    # import platform
    # print(processor())
    # print(machine())
    # print(system())
    # print(version())
    # print(uname())
    # print(dir(platform))

    # from sys import path
    # path.append('D:\Personal\!!!Copia Disco Duro\Documentos')
    # print(path)

#     print(func(10,5))
#     print(func(6,2))
#     print(func(10,0))

       




# def func(a,b):
#     return b and (a//b)**3 or 'X'

     
   

if  __name__  ==  '__main__' :
    run()