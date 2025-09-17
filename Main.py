from Bus import Bus
from Billete import Billete
from Cliente import Cliente

clientes = []
buses = []

def main():
    while True:
        opcion = menu()
        if opcion == '1':
            crearBus()
        elif opcion == '2':
            crearCliente()
        elif opcion == '3':
            comprarBillete(clientes, buses)
        elif opcion == '4':
            devolverBillete(clientes)
        elif opcion == '5':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


def menu():
    print("1. Crear Bus")
    print("2. Crear Cliente")
    print("3. Comprar Billete")
    print("4. Devolver Billete")
    print("5. Salir")
    return input("Seleccione una opción: ")

def crearBus():
    numero_serie = input("Ingrese el número de serie del bus: ")
    numero_plazas = input("Ingrese el número de plazas del bus: ")
    bus = Bus(numero_serie, numero_plazas)
    buses.append(bus)
    print(f"Bus creado con número de serie: {bus.getNumeroSerie()}")

def plazasLibres():
    print("Buses disponibles:")
    for idx, bus in enumerate(buses):
        print(f"{idx + 1}. Bus número de serie: {bus.getNumeroSerie()}")
    bus_idx = int(input("Seleccione el número de serie del bus: ")) - 1
    bus = buses[bus_idx]
    print(f"Plazas libres: {bus.getPlazasLibres()}")

def plazasOcupadas():
    print("Buses disponibles:")
    for idx, bus in enumerate(buses):
        print(f"{idx + 1}. Bus número de serie: {bus.getNumeroSerie()}")
    bus_idx = int(input("Seleccione el número de serie del bus: ")) - 1
    bus = buses[bus_idx]
    print(f"Plazas libres: {bus.getPlazasOcupadas()}")

def crearCliente():
    nombre = input("Ingrese el nombre del cliente: ")
    apellido = input("Ingrese el apellido del cliente: ")
    cliente = Cliente(nombre, apellido)
    clientes.append(cliente)
    print(f"Cliente creado: {cliente.getNombre()} {cliente.getApellido()}")

def comprarBillete(clientes, buses):
    if not clientes:
        print("No hay clientes disponibles. Cree un cliente primero.")
        return
    if not buses:
        print("No hay buses disponibles. Cree un bus primero.")
        return

    print("Clientes disponibles:")
    for idx, cliente in enumerate(clientes):
        print(f"{idx + 1}. {cliente.getNombre()} {cliente.getApellido()}")
    cliente_idx = int(input("Seleccione el número del cliente que quiere comprar el billete: ")) - 1
    cliente = clientes[cliente_idx]

    print("Buses disponibles:")
    for idx, bus in enumerate(buses):
        print(f"{idx + 1}. Bus número de serie: {bus.getNumeroSerie()}")
    bus_idx = int(input("Seleccione el número de serie del bus: ")) - 1
    bus = buses[bus_idx]

    billete = Billete(cliente, bus)
    cliente.agregarBillete(billete)
    bus.ocuparPlaza()
    print(f"Billete comprado para {cliente.getNombre()} en el bus {bus.getNumeroSerie()}")

def devolverBillete(clientes):
    if not clientes:
        print("No hay clientes disponibles.")
        return

    print("Clientes disponibles:")
    for idx, cliente in enumerate(clientes):
        print(f"{idx + 1}. {cliente.getNombre()} {cliente.getApellido()}")
    cliente_idx = int(input("Seleccione el número del cliente que quiere devolver el billete: ")) - 1
    cliente = clientes[cliente_idx]

    if not cliente.getBilletes():
        print("Este cliente no tiene billetes para devolver.")
        return

    print("Billetes del cliente:")
    for idx, billete in enumerate(cliente.getBilletes()):
        print(f"{idx + 1}. Billete en bus número de serie: {billete.getBus().getNumeroSerie()}")
    billete_idx = int(input("Seleccione el num serie del billete que quiere devolver: ")) - 1
    billete = cliente.getBilletes()[billete_idx]

    cliente.devolverBillete(billete)
    billete.getBus().liberarPlaza()
    print(f"Billete devuelto para {cliente.getNombre()} en el bus {billete.getBus().getNumeroSerie()}")

main()