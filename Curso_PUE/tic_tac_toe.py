from random import randrange 


def DisplayBoard():
# la función acepta un parámetro el cual contiene el estado actual del tablero
# y lo muestra en la consola  
    if len(jugadas_maquina) > 0:
        lista_posiciones[0] = lista_posiciones[0].replace(jugadas_maquina[len(jugadas_maquina)-1],'X')
        lista_posiciones[1] = lista_posiciones[1].replace(jugadas_maquina[len(jugadas_maquina)-1],'X')
        lista_posiciones[2] = lista_posiciones[2].replace(jugadas_maquina[len(jugadas_maquina)-1],'X')
    if len(jugadas_usuario) > 0:
        lista_posiciones[0] = lista_posiciones[0].replace(jugadas_usuario[len(jugadas_usuario)-1],'O')
        lista_posiciones[1] = lista_posiciones[1].replace(jugadas_usuario[len(jugadas_usuario)-1],'O')
        lista_posiciones[2] = lista_posiciones[2].replace(jugadas_usuario[len(jugadas_usuario)-1],'O')

    for line in range(1,20):
        if line==1 or line==7 or line==13 or line ==19:
            print(bordes_tablero[0])
        elif line%2==0:
            if line == 4:
                print(lista_posiciones[0])
            elif line == 10:
                print(lista_posiciones[1])
            elif line==16:
                print(lista_posiciones[2])
            else:
                print(bordes_tablero[1])
        else:
            print(bordes_tablero[2])
        


def DrawMove():
    while True:
        maquina_move = randrange(1,10)
        if int(maquina_move) > 9 or int(maquina_move) < 1:
            continue
        elif str(maquina_move) in jugadas_maquina or str(maquina_move) in jugadas_usuario:
             continue
        else:
            jugadas_maquina.append(str(maquina_move))
            break
    DisplayBoard()



def check_win(chek_jugador):
    ganador = False
    if('1' in chek_jugador and '2' in chek_jugador and '3' in chek_jugador):
        ganador = True
    elif('4' in chek_jugador and '5' in chek_jugador and '6' in chek_jugador):
        ganador = True
    elif('7' in chek_jugador and '8' in chek_jugador and '9' in chek_jugador):
        ganador = True
    elif('1' in chek_jugador and '4' in chek_jugador and '7' in chek_jugador):
        ganador = True
    elif('2' in chek_jugador and '5' in chek_jugador and '8' in chek_jugador):
        ganador = True
    elif('3' in chek_jugador and '6' in chek_jugador and '9' in chek_jugador):
        ganador = True
    elif('1' in chek_jugador and '5' in chek_jugador and '9' in chek_jugador):
        ganador = True
    elif('3' in chek_jugador and '5' in chek_jugador and '7' in chek_jugador):
        ganador = True
    return ganador



def VictoryFor(juego_finalizado):
# la función analiza el estatus del tablero para verificar si
# el jugador que utiliza las 'O's o las 'X's ha ganado el juego
    if check_win(jugadas_usuario):
        print('Felicidades, has ganado la partida')
        juego_finalizado = True
    elif check_win(jugadas_maquina):
        print('Lo siento, has perdido la partida')
        juego_finalizado = True
    if  len(jugadas_maquina) == 5 and juego_finalizado==False:
        print('Ha sido tablas')
        juego_finalizado = True
    return juego_finalizado



def EnterMove():
# la función dibuja el movimiento de la maquina y actualiza el tablero
    usuario_move = input('Ingrese su movimiento: ')
    while True:
        try:
            int(usuario_move)
        except: 
            usuario_move = input('Movimiento incorrecto. Por favor introduzca un numero del 1 al 9: ')
            continue
        if int(usuario_move) > 9 or int(usuario_move) < 1:
           usuario_move = input('Movimiento incorrecto. Por favor introduzca un numero del 1 al 9: ')
           continue
        elif usuario_move in jugadas_maquina or usuario_move in jugadas_usuario:
           usuario_move = input('Movimiento ya realizado. Por favor introduzca otro movimiento: ')
           continue
        else:
            jugadas_usuario.append(str(usuario_move))
            break
    DisplayBoard()


def run():
    global jugadas_maquina, jugadas_usuario, bordes_tablero, lista_posiciones
    bordes_tablero   = ('+-----------+-----------+-----------+', '|           |           |           |', '                                     ')
    lista_posiciones = ['|     1     |     2     |     3     |', '|     4     |     5     |     6     |', '|     7     |     8     |     9     |']
    jugadas_maquina  = ['5']
    jugadas_usuario  = []
    juego_finalizado = False
    DisplayBoard()
    while not juego_finalizado:
        EnterMove()
        DrawMove()
        if len(jugadas_maquina)>=3:
           juego_finalizado = VictoryFor(juego_finalizado)



if  __name__  ==  '__main__' :
    run()