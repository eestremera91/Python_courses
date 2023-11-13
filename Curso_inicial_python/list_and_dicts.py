def run():
    #creación de listas y diccionarios
    my_list = [1, 'Hello', True, 4.5]
    my_dic = {'Firstname': 'facundo', 'lastname': 'Garcia'}
    
    super_list = [
        {'Firstname': 'Facundo', 'lastname': 'Garcia'} , 
        {'Firstname': 'Jose', 'lastname': 'Martinez'},
        {'Firstname': 'Pedro', 'lastname': 'Castro'},
        {'Firstname': 'Coco', 'lastname': 'Garcia'},
    ]

    super_dict  = {
        "natural_nums":  [1,2,3,4,5,6],
        "integer_nums":   [-1,-2,0,1,2],
        "floating_nums":  [1.1, 4.5, 6.43]
    }
    
    #como moverme entre listas y diccionarios con for
    for  key, value in super_dict.items():
        print(key, '_', value)

    for  value in super_list:
        print(value['Firstname'], value['lastname'])

    # list_nums_square = [],

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

    lista1 = 2


    def procesar_elementos_de_lista(x):
        x +=1
        print("Esto está dentro de la función",x)
        return x

   
    lista1 = procesar_elementos_de_lista(lista1)

    print("Esto está fuera de la función",lista1)




if  __name__  ==  '__main__' :
    run()