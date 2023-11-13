def run():
    base     = 2
    contador = 0
    while base**contador <= 1000:
        print('2 elevado a ' + str(contador) + ' es igual a: ' + str(base**contador)) 
        contador = contador + 1
   


if __name__ == '__main__':
    run()