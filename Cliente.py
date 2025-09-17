class Cliente:

    __lista_billetes = []

    def Cliente():
        def __init__(self, nombre, apellido):
            self.__nombre = nombre
            self.__apellido = apellido

    def getBillets(self):
        return Cliente.__lista_billetes

    def agregarBillete(billete):
        Cliente.__lista_billetes.append(billete)

    def devolverBillete(billete):
        Cliente.__lista_billetes.remove(billete)
