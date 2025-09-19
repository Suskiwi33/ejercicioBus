class Bus:
    __contador_buses = 0

    def __init__(self, num_plazas):
        Bus.__contador_buses += 1
        self.__numero_serie = Bus.__contador_buses
        self.__plazas_libres = num_plazas
        self.__plazas_ocupadas = 0

    
    def getPlazasLibres(self):
        return self.__plazas_libres
    
    def getPlazasOcupadas(self):
        return self.__plazas_ocupadas
    
    def ocuparPlaza(self):
        self.__plazas_libres -= 1
        self.__plazas_ocupadas += 1
    
    def liberarPlaza(self):
        self.__plazas_libres += 1
        self.__plazas_ocupadas -= 1
    
    def getNumSerie(self):
        return self.__numero_serie
    
    def getPlazasTotales(self):
        return self.__plazas_libres + self.__plazas_ocupadas