import random


def run():
    variable   = random.randint(1,100)
    posible_numero  = int(input('Introduce un número del 1 al 100: '))
    while variable != posible_numero:
        if  posible_numero < variable:
            posible_numero  = int(input('Introduzca un numero mas grande: '))
            continue
        else:
            posible_numero  = int(input('Introduzca un numero mas pequeño: '))
    print('Felicidades, ese es el número')
            
    



if __name__ == '__main__':
    run()