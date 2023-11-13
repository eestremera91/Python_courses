def divisors(num):
    try:
        if (num<0):
            raise(ValueError('Introduzca número positivo'))
        divisors_list = [i for i in range(1,num+1) if num%i==0] 
        return divisors_list
    except ValueError as ve:
        print(ve)
        return False



def run():
    # con Try_except
    try:  
        num=int(input('Introduzca su numero: '))
        print(divisors(num))
        print('End')
    except ValueError:
        print('Debes ingresar un numero')

        
    # con Assert statements
    num=input('Introduzca su numero: ')
    assert num.isnumeric(), 'Tiene que introducir un número'
    print(divisors(int(num)))
    print('End')



if  __name__  ==  '__main__' :
    run()