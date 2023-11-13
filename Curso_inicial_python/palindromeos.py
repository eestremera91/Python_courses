
def check_palindromo(palabra):
    palabra           = palabra.replace(' ','')
    palabra           = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra==palabra_invertida:
        return True
    else:
        return False
     

def run():
    palabra         = input('Escribe una palabra: ')
    es_palindromo   = check_palindromo(palabra)
    if es_palindromo == True:
        print('Es palindrmo')
    else:
        print('No es palindrmo')
      

if __name__ == '__main__':
    run()
