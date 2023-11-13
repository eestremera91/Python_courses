DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]
def run():
    # list comprehensions
    print(DATA)
    all_python_devs    = [worker['name'] for worker in DATA if worker['language'] == 'python']
    all_Platzi_workers = [worker['name'] for worker in DATA if worker['organization'] == 'Platzi']
    adult_workers      = [worker['name'] for worker in DATA if worker['age'] > 18]
 
    #hacer lo mismo con funciones de orden superior
    all_python_devs = list(filter(lambda worker:worker['language'] == 'python',DATA))
    all_python_devs = list(map(lambda worker:worker['name'],all_python_devs))


    adult_workers = list(filter(lambda worker: worker['age']>18,DATA))
    # adult_workers = list(map(lambda worker: worker['name'],adult_workers))

    
    # #sumar un diccionario a otro o lo q es lo mismo agregar otros key
    # old_people_flag = list(map(lambda worker: worker | {'old': worker['age']>70},DATA))
    # for worker in all_python_devs:
    #     print(worker)

    for worker in adult_workers:
        print(worker)


if  __name__  ==  '__main__' :
    run()