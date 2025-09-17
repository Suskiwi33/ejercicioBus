class Cliente:

    __lista_billetes = []
    __num_cliente = 0

    def __init__(self, nombre, apellido):
        self.__nombre = nombre
        self.__apellido = apellido
        Cliente.__num_cliente += 1

    def getBilletes(self):
        return Cliente.__lista_billetes

    def agregarBillete(self, billete):
        Cliente.__lista_billetes.append(billete)

    def devolverBillete(self, billete):
        Cliente.__lista_billetes.remove(billete)
    
    def getNombre(self):
        return self.__nombre
    def getApellido(self):
        return self.__apellido
