from operator import mod
def es_primo(numero):
    variable = 34

    if numero==1:
        return False
    else:
        for i in range(1,numero+1):
            if i > 1 and i < numero and mod(numero,i) == 0:
                return False
                break
            if i == numero:
                return True

def run():
    numero = int(input('entre un número: '))
    if es_primo(numero):
        print ('Es primo')
    else:
        print ('No es primo')
  


if __name__ == '__main__':
    run()
