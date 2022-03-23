from Clases.Lavadora import Lavadora
from Clases.Televisor import Televisor

if __name__ == '__main__':
    arrayElectrodomesticos = []

    lav1 = Lavadora('blanco', 'A', 20)
    lav1.setCarga(10)
    arrayElectrodomesticos.append(lav1)

    lav2 = Lavadora('rojo', 'B', 50)
    lav2.setCarga(40)
    arrayElectrodomesticos.append(lav2)

    lav3 = Lavadora('negro', 'C', 10)
    lav3.setCarga(20)
    arrayElectrodomesticos.append(lav3)

    lav4 = Lavadora('verde', 'Z', 40)
    lav4.setCarga(15)
    arrayElectrodomesticos.append(lav4)

    lav5 = Lavadora('gris', 'F', 30)
    lav5.setCarga(10)
    arrayElectrodomesticos.append(lav5)

    tel1 = Televisor('negro', 'B', 18)
    tel1.setResolucion(50)
    tel1.setSintonizador(True)
    arrayElectrodomesticos.append(tel1)

    tel2 = Televisor('negro', 'B', 9)
    tel2.setResolucion(30)
    tel2.setSintonizador(True)
    arrayElectrodomesticos.append(tel2)

    tel3 = Televisor('gris', 'B', 5)
    tel3.setResolucion(20)
    tel3.setSintonizador(False)
    arrayElectrodomesticos.append(tel3)

    tel4 = Televisor('rojo', 'B', 70)
    tel4.setResolucion(60)
    tel4.setSintonizador(False)
    arrayElectrodomesticos.append(tel4)

    tel5 = Televisor('blanco', 'B', 30)
    tel5.setResolucion(40)
    tel5.setSintonizador(True)
    arrayElectrodomesticos.append(tel5)

    precioElectrodomesticos = 0
    precioLavadoras = 0
    precioTelevisores = 0

    for elec in arrayElectrodomesticos:
        precioElectrodomesticos += elec.precioFinal()
        if isinstance(elec, Lavadora):
            precioLavadoras += elec.precioFinal()
        elif isinstance(elec, Televisor):
            precioTelevisores += elec.precioFinal()

    print('Electrodomesticos: ', precioElectrodomesticos)
    print('Lavadoras: ', precioLavadoras)
    print('Televisores: ', precioTelevisores)
