def run():
    mi_diccionario = {
        'llave1':1,
        'llave2':2,
        'llave3':3,
    }
    print(mi_diccionario['llave1'])

    poblacion_paises = {
        'Argentina':44938712,
        'Brasil':2100000000,
        'Colombia':524512,
    }
    print(poblacion_paises['Colombia'])
    poblacion_paises.pop('Argentina')
if __name__ == '__main__':
    run()