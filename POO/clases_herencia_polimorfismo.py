class Empleado:
    #constructor de la clase
    def __init__(self,p_nombre = 'Nombre por defecto', p_apellido = 'Apellido por defecto',p_salario=0.0):
        self.nombre   = p_nombre
        self.apellido = p_apellido
        self.salario  = p_salario 

    #método que se ejecuta por defeccto al ejecutar un print de la clase
    def __str__(self):
        return 'nombre: '+ self.nombre + '-Apellido: '+self.apellido+'-Salario: ' + str(self.salario)

    def recuperarSalario(self):
        return self.salario

    def incrementarsalario(self,porcentaje):
        if not (porcentaje >= 1 and porcentaje <=5):
            raise ('El porcentaje debe estar entre 1 y 15%')
        else:
            self.salario = self.salario*(1+(porcentaje)/100)

         #ejemplo de herencia y polimorfismo   
class Animal:
    def __str__(self):
        return ("Sin valor")

class Perro(Animal):
    def __str__(self):
        return ("Guau!")

class Gato(Animal):
    def __str__(self):
        return ("Miau!")
    
class Canario(Animal):
    pass

class Gallo(Animal):
    def __str__(self):
        return ("KikiriKiii!")
    
class Oveja(Animal):
    def __str__(self):
        return ("Beeeeh!")

class Caniche(Perro):
    pass







def run():
    emp1 = Empleado('Cesar', 'Martín',2000)
    emp2 = Empleado('Jose', 'Martí',4000)
    emp3 = Empleado()
    emp4 = Empleado('Javier')
    emp3 = Empleado('Antonio', 'Maceo',2000)
    emp1.incrementarsalario(5)
    print(emp1)
    print(emp2)
    print(emp3)
    print(emp4)
    print(emp4.__dict__)

    perro   = Perro()
    gato    = Gato()
    canario = Canario()
    oveja   = Oveja()
    gallo   = Gallo()
    caniche = Caniche()

    lista_animales = [perro, gato, canario, gallo, oveja, caniche]

    for animal in lista_animales:
        print(animal)
        



if  __name__  ==  '__main__' :
    run()