class Cliente:

    __num_cliente = 0

    def __init__(self, nombre, apellido):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__lista_billetes = []
        Cliente.__num_cliente += 1

    def getBilletes(self):
        return self.__lista_billetes

    def agregarBillete(self, billete):
        self.__lista_billetes.append(billete)

    def devolverBillete(self, billete):
        self.__lista_billetes.remove(billete)
    
    def getNombre(self):
        return self.__nombre
    def getApellido(self):
        return self.__apellido
