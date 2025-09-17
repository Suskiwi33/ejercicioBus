class Bus:

    __contador_buses = 0
    __plazas_libres = 0
    __plazas_ocupadas = 0

    def __init__(self, numero_serie, num_plazas):
        self.__numero_serie = numero_serie
        self.__num_plazas_totales = num_plazas
        Bus.__plazas_libres = num_plazas
        Bus.__contador_buses += 1

    def getNumeroSerie(self):
        return self.__numero_serie
    
    @classmethod
    def getPlazasLibres(cls):
        return cls.__plazas_libres
    
    @classmethod
    def getPlazasOcupadas(cls):
        return cls.__plazas_ocupadas
    
    @classmethod
    def ocuparPlaza(cls):
        cls.__plazas_libres -= 1
        cls.__plazas_ocupadas += 1

    def getPlazasTotales(self):
        return self.__num_plazas_totales