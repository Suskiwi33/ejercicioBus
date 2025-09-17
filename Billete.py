class Billete:

    __num_serie = 0
    
    def __init__(self, cliente, bus):
        Billete.__num_serie =+ 1
        self.__cliente = cliente
        self.__bus = bus

    def getNumSerie():
        return Billete.__num_serie        

    def setCliente(self, cliente):
        self.__cliente = cliente

    def getCliente(self):
        return self.__cliente

    def getBus(self):
        return self.__bus