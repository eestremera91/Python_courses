def run():
    # operaciones normales con listas
    # list_nums_squares = []
    # for i in range(1, 101):
    #     if (i**2) % 3 != 0:
    #         list_nums_squares.append(i**2)


    #Hacer lo anterior más facil con list comprehensions (generar listas sin ciclos)
    # list = [element for element in iterable if condition]
    list_nums_squares = [i**2 for i in range(1,101) if i%3 != 0]

    list_nums_squares = [i**2 for i in range(1,101) if i%3]
    print(list_nums_squares)


if  __name__  ==  '__main__' :
    run()