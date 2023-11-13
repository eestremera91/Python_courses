def read():
    numbers = []
    with open('./archivos/Txt_para_ejemplo_manejo_datos.txt','r',encoding='utf-8') as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)

def write():
    names = ['Ana','pepe','Ana2','pepe2']
    with open('./archivos/names.txt','w',encoding='utf-8') as f:
        for names in names:
            f.write(names)
            f.write('\n')

def write2():
    names = [' 2',' 3',' 4',' 5']
    with open('./archivos/names.txt','a+',encoding='utf-8') as f:
        for names in f:
            f.write(names)
            f.write('\n')

def run():

    write2()



if  __name__  ==  '__main__' :
    run()