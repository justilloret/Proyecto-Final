# class gato():
#     def __init__(self,raza,nombre,color):
#         self.raza = raza
#         self.nombre = nombre
#         self.color = color
#         self.hambre = False
   
#     def dormir(self):
#         print(f"{self.nombre}: zzzz")

#     def mauyar (self):
#         print(f"{self.nombre}: miauuuu ")
    
#     def comer(self):
#         if (self.hambre):
#             self.hambre = True
#             print(f"{self.nombre}: ñam ñam ñam")

#     def correr(self):
#         if self.hambre == True:
#             print(f"{self.nombre}: miau miau")
#         else:
#             print(f"{self.nombre} tiene mucha hambre como para correr")
        
# tito = gato('persa', 'Tito', 'gris' )
# garfield = gato('exótico', 'Garfield', 'naranja')

# tito.comer()
# garfield.mauyar()
# tito.correr()
# garfield.correr()





class animal():
    def __init__(self, nombre, color, tamaño):
        self.nombre = nombre
        self.color = color 
        self.tamaño = tamaño

    def moverse(self):
        print(f"{self.nombre}: me estoy moviendo!")

    def dormir(self):
        print(f"{self.nombre}: zzz")

class perro(animal):
    def __init__(self, nombre, color, tamaño, raza):
        super().__init__(nombre, color, tamaño)
        self.raza = raza

    def ladrar(self):
        print(f"{self.nombre}: guau guau")

class gato(animal):
    def __init__(self, nombre, color, tamaño, juguete_favorito):
        super().__init__(nombre, color, tamaño)
        self.juguete_favorito = juguete_favorito

    def jugar(self):
        print(f"{self.nombre} esta jugando con su {self.juguete_favorito}")

Firulais = perro('Firulais', 'marrón', 'pequeño', 'caschi')
Leon = gato('Leon', 'naranja', 'mediano', 'ratoncito de peluche')

Firulais.moverse()
Leon.dormir()
Firulais.ladrar()
Leon.jugar()