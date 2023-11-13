from random import randrange 
from os import system
import time

def load_word(): 
    with open('./archivos/Palabras_ahorcado.txt','r',encoding='utf-8') as f:
        words = [i.replace('\n','') for i in f]        
    selected_word   = words[randrange(len(words))]
    selected_word_1 = selected_word.maketrans('áéíóúñ', 'aeioun')  #esta linea y la de abajo juntas para sustituir los caracteres q quiera por otros q defina
    selected_word   = selected_word.translate(selected_word_1)
    selected_word   = selected_word.upper()
    return selected_word

def check_letter(failed_attempts,hide_word, letter):
    if letter in selected_word:
        index = [i for i in range(len(selected_word)) if letter ==selected_word[i]]
        for i in index:
            hide_word = hide_word[:i] + letter + hide_word[i+1:]
    else:
        failed_attempts += 1        
    return hide_word, failed_attempts

def draw_failed_attempts(failed_attempts,picture_TEMP):
    tabla_switch = {
        '0': [8,15,22,23,24,29,31],
        '1': [15,22,23,24,29,31],
        '2': [22,23,24,29,31],
        '3': [22,24,29,31],
        '4': [24,29,31],
        '5': [29,31],
        '6': [31],
        '7': [],
    }
    index = tabla_switch.get(str(failed_attempts))
    for i in index:
        picture_TEMP = picture_TEMP[:i] + ' ' + picture_TEMP[i+1:]
    print(picture_TEMP)
        

def run():
    print('Welcome to the hangman game. Guess the word:')
    global selected_word, dimension_word, failed_attempts
    failed_attempts = 0
    selected_word   = load_word()
    dimension_word  = len(selected_word)
    start_game      = True
    hide_word       = '_'*dimension_word
    history_letter  = []
    picture = ('''
+----+
|    |
O    |
/|\  |
/ \  |
     |
    =====''')
    while start_game:
        try:
            draw_failed_attempts(failed_attempts,picture)
            if failed_attempts==7:
                start_game = False
                print('Sorry, you lose')
                break
            print(hide_word)
            letter = input('Enter letter: ')
            letter = letter.upper()
            system('cls')
            if letter.isnumeric() or len(letter)==0 or len(letter) > 1:
                raise(ValueError('You must enter a single letter'))           
             
            if not(letter in history_letter):
                history_letter.append(letter) 
                hide_word,failed_attempts = check_letter(failed_attempts,hide_word, letter)   
                if not('_' in hide_word):
                    start_game = False
                    print(hide_word)
                    print('You win, Congratulations')
            else:
                print(letter + ' is a letter already entered')
        except ValueError as ve:
            print(ve)

        
if  __name__  ==  '__main__' :
    system('cls')
    run()