def nearlySimilarRectangles(sides):   
    relacion_entre_lados = [sides[i][1]/sides[i][0] for i in range(len(sides))]
    relacion_entre_lados.sort()
    print(relacion_entre_lados)

    no_coinciden = [1 for i in range(1,len(relacion_entre_lados)) if relacion_entre_lados[i-1] == relacion_entre_lados[i]]
    flag_igual = False
    total = 0
    for i in range(1,len(relacion_entre_lados)):
        if relacion_entre_lados[i-1] == relacion_entre_lados[i]:
           total += 1
           flag_igual = True
        elif flag_igual:
            total += 1
            flag_igual = False
    if i==len(relacion_entre_lados)-1 and flag_igual:
        total += 1

    print(total)

    



if __name__ == '__main__':

    #sides = [[4,8], [15,30],[25, 50]]  
    sides = [[5,10], [10,10],[3, 6],[9, 9]]  
    #sides = [[2,1], [10,7],[9, 6],[6, 9], [7, 3]]  

    result = nearlySimilarRectangles(sides)