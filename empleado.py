class Empleado:

    def __init__(self, idEmpleado, nombre, direccion):
        self.__idEmpleado = idEmpleado
        self.__nombre = nombre
        self.__direccion = direccion

    @property
    def idEmpleado(self):
        return self.__idEmpleado

    @idEmpleado.setter
    def idEmpelado(self, valor):
        self.__idEmpleado = valor

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    @property
    def direccion(self):
        return self.__direccion

    @direccion.setter
    def direccion(self, valor):
        self.__direccion = valor

    @staticmethod
    def agregarEmpleado():
        while True:
            idEmpleado = input("Ingresa el ID: ")
            with open("./archivos/empleados.txt","r",encoding="utf8") as empleadosTXT:
                lineas = empleadosTXT.readlines()
                for linea in lineas:
                    if idEmpleado in linea:
                        print("\nID ya existe!\n")
                        empleadosTXT.close()
                        break
                else:
                    nombre = input("Nombre: ")
                    direccion = input("Dirección: ")
                    Empleado(idEmpleado, nombre, direccion)
                    empleadosTXT = open("./archivos/empleados.txt", "a", encoding = "utf8")
                    empleadosTXT.write(f"{idEmpleado}|{nombre}|{direccion}\n")
                    print("="*31)
                    print("\nEmpleado agregado exitosamente!\n")
                    print("="*31)
                    empleadosTXT.close()
                    break

    @staticmethod
    def borrarEmpleado():
        pass


    def modificarEmpleado(self):
        pass

    @staticmethod
    def mostrarEmpleados():
        print(f"{'ID':<5}{'NOMBRE':^10}{'DIRECCION':>15}")
        print("_"*31)
        with open("./archivos/empleados.txt", encoding="utf8") as empleadosTXT:
            for linea in empleadosTXT:
                datos = linea.strip().split('|')
                print(f"{datos[0]:<5}{datos[1]:^10}{datos[2]:>15}")
        empleadosTXT.close()



    def buscarEmpleado(self):
        pass


