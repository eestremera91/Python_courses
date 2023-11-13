#definición de una función normal
# def palindrome(string):
#     return string == string[::-1]

#funciones anónimas (solo tienen una línea de código) la palabra clave es lambda
palindrome = lambda string: string == string[::-1]      

def run():
    print(palindrome('ANA'))
    


if  __name__  ==  '__main__' :
    run()