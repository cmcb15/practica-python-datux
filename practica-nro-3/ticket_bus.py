class Conductor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.horarios = []  
    
    def asignar_horario(self, hora):
        if hora in self.horarios:
            print(f"El conductor {self.nombre} ya tiene asignado el horario {hora}.")
        else:
            self.horarios.append(hora)
            print(f"El horario {hora} ha sido asignado al conductor {self.nombre}.")


class Bus:
    def __init__(self, cod_bus):
        self.cod_bus = cod_bus
        self.ruta = None
        self.horarios = []  
        self.conductor = None  
    
    def asignar_ruta(self, ruta):
        self.ruta = ruta
        print(f"Ruta {ruta} asignada al bus {self.cod_bus}.")
    
    def registrar_horario(self, horario):
        if horario in self.horarios:
            print(f"El horario {horario} ya está registrado para el bus {self.cod_bus}.")
        else:
            self.horarios.append(horario)
            print(f"El horario {horario} ha sido registrado para el bus {self.cod_bus}.")
    
    def asignar_conductor(self, conductor):
        if self.horarios:
            horarios_coincidentes = []
            for hora in self.horarios:
                if hora in conductor.horarios:
                    horarios_coincidentes.append(hora)
            
            if horarios_coincidentes:
                self.conductor = conductor
                print(f"El conductor {conductor.nombre} ha sido asignado al bus {self.cod_bus}.")
            else:
                print(f"No se puede asignar el conductor {conductor.nombre} porque sus horarios no coinciden con los del bus {self.cod_bus}.")
        else:
            print(f"No se puede asignar el conductor {conductor.nombre} porque el bus {self.cod_bus} no tiene horarios registrados.")


class Admin:
    def __init__(self):
        self.buses = []
        self.conductores = []
    
    def agregar_bus(self, cod_bus):
        bus = Bus(cod_bus)
        self.buses.append(bus)
        print(f"El bus {cod_bus} ha sido agregado correctamente.")
    
    def agregar_conductor(self, nombre):
        conductor = Conductor(nombre)
        self.conductores.append(conductor)
        print(f"El conductor {nombre} ha sido agregado correctamente.")
    
    def buscar_bus(self, cod_bus):
        for bus in self.buses:
            if bus.cod_bus == cod_bus:
                return bus
        return None
    
    def buscar_conductor(self, nombre):
        for conductor in self.conductores:
            if conductor.nombre == nombre:
                return conductor
        return None
    
    def menu(self):
        while True:
            print("\nMenú del Administrador:")
            print("1. Agregar Bus")
            print("2. Agregar Ruta a Bus")
            print("3. Registrar Horario a Bus")
            print("4. Agregar Conductor")
            print("5. Agregar Horario a Conductor")
            print("6. Asignar Bus a Conductor")
            print("7. Salir")
            opcion = input("Seleccione una opción: ")
            
            match opcion:
                case "1":
                    cod_bus = input("Ingrese el codigo del bus: ")
                    self.agregar_bus(cod_bus)
                case "2":
                    while True:
                        cod_bus = input("Ingrese el codigo del bus: ")
                        bus = self.buscar_bus(cod_bus)
                        if bus:
                            ruta = input("Ingrese la ruta: ")
                            bus.asignar_ruta(ruta)
                            break
                        else:
                            print("El bus no se ha encontrado. Intente de nuevo.")
                case "3":
                    while True:
                        cod_bus = input("Ingrese el codigo del bus: ")
                        bus = self.buscar_bus(cod_bus)
                        if bus:
                            horario = input("Ingrese el horario en formato HH:MM (24 horas), por favor: ")
                            bus.registrar_horario(horario)
                            break
                        else:
                            print("El bus no se ha encontrado. Intente de nuevo.")
                case "4":
                    nombre = input("Ingrese el nombre del conductor: ")
                    self.agregar_conductor(nombre)
                case "5":
                    while True:
                        nombre = input("Ingrese el nombre del conductor: ")
                        conductor = self.buscar_conductor(nombre)
                        if conductor:
                            horario = input("Ingrese el horario en formato HH:MM (24 horas), por favor: ")
                            conductor.asignar_horario(horario)
                            break
                        else:
                            print("El conductor no se ha encontrado. Intente de nuevo.")
                case "6":
                    while True:
                        cod_bus = input("Ingrese el codigo del bus: ")
                        bus = self.buscar_bus(cod_bus)
                        if bus:
                            while True:
                                nombre = input("Ingrese el nombre del conductor: ")
                                conductor = self.buscar_conductor(nombre)
                                if conductor:
                                    bus.asignar_conductor(conductor)
                                    break
                                else:
                                    print("El conductor no se ha encontrado. Intente de nuevo.")
                            break
                        else:
                            print("El bus no se ha encontrado. Intente de nuevo.")
                case "7":
                    print("Saliendo del programa...")
                    print("\n")
                    break
                case _:
                    print("Opción no válida, intente de nuevo.")


if __name__ == "__main__":
    Admin().menu()