from Clases.Electrodomestico import Electrodomestico


class Televisor(Electrodomestico):
    #Propiedades

    resolucion = 20
    sintonizador = False

    #Constructor

    def __init__(self, newColor, newConsumo, newPeso):
        Electrodomestico.__init__(self, newColor, newConsumo, newPeso)

    #Métodos

    def getResolucion(self):
        return self.resolucion

    def setResolucion(self, newResolucion):
        self.resolucion = newResolucion

    def getSintonizador(self):
        return self.sintonizador

    def setSintonizador(self, newSintonizador):
        self.sintonizador = newSintonizador

    def precioFinal(self):
        precioDefinitivo = super().precioFinal()
        if self.resolucion > 40:
            precioDefinitivo += precioDefinitivo * 0.3
        if self.sintonizador:
            precioDefinitivo += 50
        return precioDefinitivo
