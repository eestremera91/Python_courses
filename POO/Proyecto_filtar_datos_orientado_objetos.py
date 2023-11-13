class Empleado:
    #constructor de la clase
    def __init__(self,p_name = 'Nombre por defecto', p_age = 'Edad por defecto', p_organization='Edad por defecto', p_position = 'Posición por defecto', p_language = 'Apellido por defecto'):
        self.name          = p_name
        self.age           = p_age
        self.organization  = p_organization 
        self.position      = p_position 
        self.language      = p_language 
        self.dictionario   = {'name': p_name, 'age':p_age, 'organization': p_organization, 'language': p_language}      

    def __str__(self):
        print(self.dictionario)
        return 'nombre:'+ self.name + '  age:'+ str(self.age) +'  organization:' + self.organization +'  position:' + self.position +'  language:' + self.language


def run():
    emp1 = Empleado('Facundo', 72, 'Platzi','Technical Coach','python')
    emp2 = Empleado('Luisana', 33, 'Globant','UX Designer','javascript')
    emp3 = Empleado('Héctor', 19, 'Platzi','Associate','ruby')
    emp4 = Empleado('Gabriel', 20, 'Platzi','Associate','javascript')
    emp5 = Empleado('Karo', 23, 'Everis','Backend Developer','python')
    emp6 = Empleado('Isabella', 30, 'Platzi','QA Manager','java')
    lista_dict_emp = [emp1.__dict__, emp2.dictionario, emp3.dictionario,emp4.dictionario, emp5.dictionario, emp6.dictionario]
    print(lista_dict_emp)

    all_python_devs    = [worker['name'] for worker in lista_dict_emp if worker['language'] == 'python']
    for worker in all_python_devs:
        print(worker)

    all_python_devs_lambda = list(filter(lambda worker:worker['language'] == 'python',lista_dict_emp))
    all_python_devs_lambda = list(map(lambda worker:worker['name'],all_python_devs_lambda))
    for worker in all_python_devs_lambda:
        print(worker)

    # for worker in dict_emp:
    #    print(worker.)

    # print(emp3)
    # print(dict_emp[1].name)
    # # list comprehensions
    # # all_python_devs    = [worker['name'] for worker in DATA if worker['language'] == 'python']
    # # all_Platzi_workers = [worker['name'] for worker in DATA if worker['organization'] == 'Platzi']
    # # adult_workers      = [worker['name'] for worker in DATA if worker['age'] > 18]
 
    # # #hacer lo mismo con funciones de orden superior
    # # all_python_devs = list(filter(lambda worker:worker['language'] == 'python',DATA))
    # # all_python_devs = list(map(lambda worker:worker['name'],all_python_devs))


    # # # adult_workers = list(filter(lambda worker: worker['age']>18,DATA))
    # # # adult_workers = list(map(lambda worker: worker['name'],adult_workers))

    
    # # # #sumar un diccionario a otro o lo q es lo mismo agregar otros key
    # # # old_people_flag = list(map(lambda worker: worker | {'old': worker['age']>70},DATA))
    # # # for worker in all_python_devs:
    # # #     print(worker)
    # lista_dict = []
    # for worker in dict_emp:
    #     lista_dict.append(worker.dictionario)
    # print(lista_dict)


if  __name__  ==  '__main__' :
    run()