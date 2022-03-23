from Clases.Electrodomestico import Electrodomestico


class Lavadora(Electrodomestico):
    #Propiedades

    carga = 5

    #Constructor

    def __init__(self, newColor, newConsumo, newPeso):
        Electrodomestico.__init__(self, newColor, newConsumo, newPeso)

    #Métodos

    def getCarga(self):
        return self.carga

    def setCarga(self, newCarga):
        self.carga = newCarga

    def precioFinal(self):
        precioDefinitivo = super().precioFinal()
        if self.carga > 30:
            precioDefinitivo += 50
        return precioDefinitivo

