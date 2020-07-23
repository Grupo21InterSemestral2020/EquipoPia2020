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

    @staticmethod #Listo
    def agregarEmpleado():
        while True:
            while True:
                try:
                    idEmpleado = int(input("Ingresa el ID: "))
                    break
                except:
                    print("\n¡Error, digite solo enteros!\nIntente de nuevo...\n")
            with open("./archivos/empleados.txt","r",encoding="utf8") as empleadosTXT:
                lineas = empleadosTXT.readlines()
                for linea in lineas:
                    if str(idEmpleado) == linea.split("|")[0]:
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

    @staticmethod #Falta agregar si el usuario no existe imprimirlo por pantalla
    def borrarEmpleado():
        nuevaLista = []
        while True:
            try:
                idEmpleado = int(input("ID a borrar: "))
                break
            except:
                print("\n¡Error, digite solo enteros!\nIntente de nuevo...\n")
        with open("./archivos/empleados.txt","r", encoding="utf8") as empleadosTXT:
            for linea in empleadosTXT:
                if linea.split("|")[0] != str(idEmpleado):
                    nuevaLista.append(linea)
            empleadosTXT.close()
            with open("./archivos/empleados.txt","w", encoding="utf8") as empleadosW:
                for n in nuevaLista:
                    empleadosW.write(str(n))
            print("Borrado exitosamente\n")
            empleadosW.close()

    @staticmethod #test v1 (falta verificacion de ID)
    def modificarEmpleado():
        idEmpleado = input("Ingresa el ID a modificar: ")
        eleccionMod = input("¿Que dato quieres modificar?\n1.- Nombre\n2.- Direccion\nIngresa una opcion: ")
        if eleccionMod == "1":
            nombre = input("Ingresa el nuevo nombre: ")
        elif eleccionMod == "2":
            direccion = input("Ingresa la nueva direccion: ")
        else:
            print("Ingresa una opcion valida!")
        listaCambios = []
        listaCambios2 = []
        empleadosTXT = open("./archivos/empleados.txt","r",encoding="utf8")
        readlines = empleadosTXT.readlines()
        for line in readlines:
            line = line.replace("\n","")
            listaCambios.append(line)
        for linea in listaCambios:
            datos = linea.split("|")
            if datos[0] == idEmpleado:
                if eleccionMod == "1":
                    datosNuevos = datos[1].replace(datos[1], nombre + "|" + datos[2])
                    datosCambiados = (datos[0] + "|" + datosNuevos + "\n")
                    listaCambios2.append(datosCambiados)
                elif eleccionMod == "2":
                    datosNuevos = datos[1].replace(datos[1], datos[1] + "|" + direccion)
                    datosCambiados = (datos[0] + "|" + datosNuevos + "\n")
                    listaCambios2.append(datosCambiados)
            else:
                datos = (linea + "\n")
                listaCambios2.append(datos)
        empleadosTXT.close()
        empleadosTXTW = open("./archivos/empleados.txt","w",encoding="utf8")
        for i in listaCambios2:
            empleadosTXTW.write(i)
        empleadosTXTW.close()

    @staticmethod #Listo
    def mostrarEmpleados():
        print(f"{'ID':<5}{'NOMBRE':^10}{'DIRECCION':>15}")
        print("_"*31)
        with open("./archivos/empleados.txt", encoding="utf8") as empleadosTXT:
            for linea in empleadosTXT:
                datos = linea.strip().split('|')
                print(f"{datos[0]:<5}{datos[1]:^10}{datos[2]:>15}")
        empleadosTXT.close()

    @staticmethod
    def buscarEmpleado(): #Falta agregar si el usuario no existe imprimirlo por pantalla
        while True:
            try:
                idEmpleado = int(input("Introduce el ID que quieres buscar: "))
                break
            except:
                print("Introduce solo numeros enteros!")
        with open("./archivos/empleados.txt","r",encoding="utf8") as empleadosTXT:
            for linea in empleadosTXT:
                datos = linea.split("|")
                datoID = linea.split("|")[0]
                if datoID == str(idEmpleado):
                    print(f"{'ID':<5}{'NOMBRE':^10}{'DIRECCION':>15}")
                    print("_"*31)
                    print(f"{datos[0]:<5}{datos[1]:^10}{datos[2]:>15}")
                    empleadosTXT.close()
                    break




