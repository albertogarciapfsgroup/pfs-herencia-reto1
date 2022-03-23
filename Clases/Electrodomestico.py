'''
        ################################################
        ### Autor: Eduardo Bono - Fecha: 23/03/2022  ###
        ### Version: 1.0  -  Clase Electrodomestico  ###
        ################################################
'''

class Electrodomestico():
    # Atributos de la clase
    precio_base = 100
    color = 'blanco'
    consumo = 'F'
    peso = 5

    # Constructor de la clase
    def __init__(self, newColor, newConsumo, newPeso):
        self.color = self.comprobarColor(newColor)
        self.consumo = self.comprobarConsumoEnergetico(newConsumo)
        self.peso = newPeso

    # Metodos de la clase
    def comprobarConsumoEnergetico(self, consumo):
        comprueba = ['A', 'B', 'C', 'D', 'E', 'F']
        if consumo in comprueba:
            return consumo
        else:
            print("El consumo introducido no es valido, por favor introduzca uno de los siguientes valores")
            otro = input("A, B, C, D, E o F: ")
            self.comprobarConsumoEnergetico(otro)

    def comprobarColor(self, color):
        comprueba = ['blanco', 'negro', 'rojo', 'azul', 'gris']
        if color in comprueba:
            return color
        else:
            print("El color introducido no es valido, por favor introduzca uno de los siguientes valores")
            otro = input("blanco, negro, rojo, azul o gris: ")
            self.comprobarColor(otro)

    def precioFinal(self):
        # variables locales
        precio = 0

        # comprobamos consumo energetico
        if (self.consumo == 'A'):
            precio = self.precio_base + 100
        elif (self.consumo == 'B'):
            precio = self.precio_base + 80
        elif (self.consumo == 'C'):
            precio = self.precio_base + 60
        elif (self.consumo == 'D'):
            precio = self.precio_base + 50
        elif (self.consumo == 'E'):
            precio = self.precio_base + 30
        elif (self.consumo == 'F'):
            precio = self.precio_base + 10

        # comprobamos peso
        if (self.peso > 0) and (self.peso < 20):
            precio = precio +10
        elif (self.peso > 19) and (self.peso < 50):
            precio = precio + 50
        elif (self.peso > 49) and (self.peso < 80):
            precio = precio + 80
        elif (self.peso > 79):
            precio = precio + 100

        return precio


    # Getters y setters
    def getPrecio(self):
        return self.precio_base

    def getColor(self):
        return self.color

    def getConsumo(self):
        return self.consumo

    def getPeso(self):
        return self.peso





