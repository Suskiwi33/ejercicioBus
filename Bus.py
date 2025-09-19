class Bus:
    __numero_serie = 0
    __contador_buses = 0
    __plazas_libres = 0
    __plazas_ocupadas = 0

    def __init__(self, num_plazas):
        Bus.__numero_serie += 1
        Bus.__plazas_libres = num_plazas
        Bus.__contador_buses += 1

    
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
    
    @classmethod
    def liberarPlaza(cls):
        cls.__plazas_libres += 1
        cls.__plazas_ocupadas -= 1
    
    @classmethod
    def getNumSerie(cls):
        return cls.__numero_serie
    
    def getPlazasTotales(cls):
        return cls.__plazas_libres + cls.__plazas_ocupadas