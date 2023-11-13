def run():
    # # operaciones normales con diccionarios
    dict_nums_squares = {}
    # for  i in range(1,101):
    #     if (i**2) % 3 != 0:
    #        dict_nums_squares[i] = i**3

    #Hacer lo anterior más facil con list comprehensions (generar listas sin ciclos)
    #list = [element for element in iterable if condition]
    dict_nums_squares = {i: i**3 for i in range(1,101) if i%3 != 0}
    print(dict_nums_squares)


if  __name__  ==  '__main__' :
    run()