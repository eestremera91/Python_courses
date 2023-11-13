from operator import mod

def run():
    numero = int(input('entre un número: '))
    for i in (numero+1):
        if i == 0:
            continue
        if i > 1 and i < numero and mod(numero,i) == 0:
            print ('No es primo')
            break
        if i == numero:
            print ('No es primo')




if __name__ == '__main__':
    run()