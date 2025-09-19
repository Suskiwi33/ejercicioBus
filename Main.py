from Bus import Bus
from Billete import Billete
from Cliente import Cliente

__clientes = []
__buses = []


def main():
    while True:
        opcion = menu()
        if opcion == '1':
            crearBus()
        elif opcion == '2':
            crearCliente()
        elif opcion == '3':
            comprarBillete(__clientes, __buses)
        elif opcion == '4':
            devolverBillete(__clientes)
        elif opcion == '5':
            estadoVenta()
        elif opcion == '6':
            print(f"Saliendo del programa.\n")
            break
        else:
            print(f"Opción no válida. Intente de nuevo.\n")


def menu():
    print("1. Crear Bus")
    print("2. Crear Cliente")
    print("3. Comprar Billete")
    print("4. Devolver Billete")
    print("5. Mostrar Estado Bus")
    print("6. Salir")
    return input(f"Seleccione una opción: \n")


def crearBus():
    
    numero_plazas = input("Ingrese el número de plazas del bus: ")
    if numero_plazas.isdigit():
        bus = Bus(int(numero_plazas))
        __buses.append(bus)
        print(f"Bus creado con número de serie: {bus.getNumSerie()}\n")
    else:
        print(f"Error: El numero de plazas tiene que ser un número entero \n")


def plazasLibres(bus):
    return bus.getPlazasLibres()


def plazasOcupadas(bus):
    return bus.getPlazasOcupadas()


def crearCliente():
    nombre = input("Ingrese el nombre del cliente: ")
    apellido = input("Ingrese el apellido del cliente: ")
    cliente = Cliente(nombre, apellido)
    __clientes.append(cliente)
    print(f"Cliente creado: {cliente.getNombre()} {cliente.getApellido()} \n")


def comprarBillete(clientes, buses):
    if not clientes:
        print(f"No hay clientes disponibles. Cree un cliente primero. \n")
        return
    if not buses:
        print(f"No hay buses disponibles. Cree un bus primero. \n")
        return

    print("Clientes disponibles:")
    for idx, cliente in enumerate(clientes):
        print(f"{idx + 1}. {cliente.getNombre()} {cliente.getApellido()}")
    cliente_idx = input("Seleccione el número del cliente que quiere comprar el billete: ")

    if cliente_idx.isdigit():
        
        cliente_idx_int = int(cliente_idx) - 1
        cliente = clientes[cliente_idx_int]

        print("Buses disponibles:")
        for idx, bus in enumerate(buses):
            print(f"{idx + 1}. Bus número de serie: {bus.getNumSerie()}")
        bus_idx = int(input("Seleccione el número de serie del bus: ")) - 1
        bus = buses[bus_idx]

        billete = Billete(cliente, bus)
        cliente.agregarBillete(billete)
        bus.ocuparPlaza()
        print(
            f"Billete comprado para {cliente.getNombre()} en el bus {bus.getNumSerie()} \n")
    else:
        print("Numero de cliente no correcto")


def devolverBillete(clientes):
    if not clientes:
        print("No hay clientes disponibles.")
        return

    print("Clientes disponibles:")
    for idx, cliente in enumerate(clientes):
        print(f"{idx + 1}. {cliente.getNombre()} {cliente.getApellido()} \n")

    cliente_idx = input("Seleccione el número del cliente que quiere devolver el billete: ")
    
    if cliente_idx.isdigit():
        cliente_idx_int = int(cliente_idx) - 1
        cliente = clientes[cliente_idx_int]

    else:
        print(f"Error: El numero del cliente no es un entero \n")
        return
    
    if not cliente.getBilletes():
        print(f"Este cliente no tiene billetes para devolver. \n")
        return

    print("Billetes del cliente:")
    for idx, billete in enumerate(cliente.getBilletes()):
        print(
            f"{idx + 1}. Billete en bus número de serie: {billete.getNumSerie()}")
    billete_idx = int(
        input("Seleccione el num serie del billete que quiere devolver: ")) - 1
    billete = cliente.getBilletes()[billete_idx]

    cliente.devolverBillete(billete)
    billete.getBus().liberarPlaza()
    print(
        f"Billete devuelto para {cliente.getNombre()} en el bus {billete.getBus().getNumSerie()} \n")


def estadoVenta():
    if len(__buses) == 0:
        print("No hay buses disponibles.")
    else:
        print("Buses disponibles:")
        for idx, bus in enumerate(__buses):
            print(f"{idx + 1}. Bus número de serie: {bus.getNumSerie()}")
        bus_idx = int(input("Seleccione el número de serie del bus: ")) - 1

        for bus in __buses:
                print(
                    f"Plazas totales -> {bus.getPlazasTotales()}, plazas libres -> {plazasLibres(bus)}, billetes vendidos {plazasOcupadas(bus)}\n")
                return

        # if bus_idx in __buses.getNumSerie():
        #     bus = __buses[bus_idx]
        #     print(
        #         f"Plazas totales -> {bus.getPlazasTotales()}, plazas libres -> {plazasLibres(bus)}, billetes vendidos {plazasOcupadas(bus)}")
        # else:
        #     print("Ese bus no existe, escoge otro")

main()
