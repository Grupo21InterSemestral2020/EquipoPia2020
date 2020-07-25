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
                    idEmpleado = int(input("\nIngresa el ID: "))
                    break
                except:
                    print("_"*30)
                    print("¡Error, digite solo números enteros!\nIntente de nuevo...")
                    print("_"*30)
                    input("Pulsa cualquier tecla para continuar...")
            with open("./archivos/empleados.txt","r",encoding="utf8") as empleadosTXT:
                lineas = empleadosTXT.readlines()
                for linea in lineas:
                    if str(idEmpleado) == linea.split("|")[0]:
                        print("_"*35)
                        print("ID ya existe!")
                        print("_"*35)
                        input("Pulsa cualquier tecla para continuar...")
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
        while True: #Ciclo principal, el ciclo se apaga cuando se borra el empleado
            nuevaLista = []
            while True:#Este ciclo valida que solo introduzca numeros enteros
                try:
                    idEmpleado = int(input("\nID a borrar: "))
                    break #Sale del ciclo si el usuario introduce un entero
                except:
                    print("_"*30)
                    print("¡Error, digite solo números enteros!\nIntente de nuevo...")
                    print("_"*30)
                    input("Pulsa cualquier tecla para continuar...")

            #Verifica si el usuario existe o no en la lista
            with open("./archivos/empleados.txt","r",encoding="utf8") as empleadosTXT:
                lineas = empleadosTXT.readlines()
                for linea in lineas:
                    if str(idEmpleado) == linea.split("|")[0]:
                        verificador = True #Si el idEmpleado existe en la lista verificador se queda en Trua y procede a borrar
                        break
                    else:
                        verificador = False #Si no existe en la lista se queda en False e imprime por pantalla que no existe
                if verificador == False:
                    print("_"*35)
                    print("ID no existe!")
                    print("_"*35)
                    input("Pulsa cualquier tecla para continuar...")
                empleadosTXT.close()

            #Si el ID si existe entonces hará esto y borrara
            if verificador == True:
                with open("./archivos/empleados.txt","r", encoding="utf8") as empleadosTXT:
                    for linea in empleadosTXT:
                        if linea.split("|")[0] != str(idEmpleado):
                            nuevaLista.append(linea)
                    empleadosTXT.close()
                    with open("./archivos/empleados.txt","w", encoding="utf8") as empleadosW:
                        for n in nuevaLista:
                            empleadosW.write(str(n))
                    print("_"*30)
                    print("Borrado existosamente!")
                    print("_"*30)
                    input("Pulsa cualquier tecla para continuar...")
                    empleadosW.close()
                    break #Break del ciclo inicial

    @staticmethod
    def modificarEmpleado():
        while True:
            try:
                idEmpleado = int(input("\nIngresa el ID a modificar: "))
                break
            except:
                print("_"*30)
                print("¡Error, digite solo números enteros!\nIntente de nuevo...")
                print("_"*30)
                input("Pulsa cualquier tecla para continuar...")
        #Verifica si el usuario existe o no en la lista
        with open("./archivos/empleados.txt","r",encoding="utf8") as empleadosTXT:
            lineas = empleadosTXT.readlines()
            for linea in lineas:
                if str(idEmpleado) == linea.split("|")[0]:
                    verificador = True #Si el idEmpleado existe en la lista verificador se queda en Trua y procede a borrar
                    break
                else:
                    verificador = False #Si no existe en la lista se queda en False e imprime por pantalla que no existe
            if verificador == False:
                print("_"*35)
                print("ID no existe!")
                print("_"*35)
                input("Pulsa cualquier tecla para continuar...")
                empleadosTXT.close()
            elif verificador == True:
                eleccionMod = input("\n¿Que dato quieres modificar?\n1.- Nombre\n2.- Dirección\nIngresa una opcion: ")
                if eleccionMod == "1":
                    nombre = input("Ingresa el nuevo nombre: ")
                    print("_"*35)
                    print("\nModificacion existosa!\n")
                    print("_"*35)
                    input("Pulsa cualquier tecla para continuar...")
                elif eleccionMod == "2":
                    direccion = input("Ingresa la nueva dirección: ")
                    print("_"*35)
                    print("\nModificacion existosa!\n")
                    print("_"*35)
                    input("Pulsa cualquier tecla para continuar...")
                else:
                    print("_"*30)
                    print("Opcion invalida.\nIntente de nuevo...")
                    print("_"*30)
                    input("Pulsa cualquier tecla para continuar...")
                listaCambios = [] #En esta lista se guarda la lista actual sin cambios
                listaCambios2 = [] #En esta lista se guarda todos los datos incluidos los cambios
                empleadosTXT = open("./archivos/empleados.txt","r",encoding="utf8")
                readlines = empleadosTXT.readlines()
                for line in readlines:
                    line = line.replace("\n","")
                    listaCambios.append(line)
                for linea in listaCambios:
                    datos = linea.split("|")
                    if datos[0] == str(idEmpleado):
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
        print("_"*33)
        print(f"{'ID':^5}{'|':^}{'NOMBRE':^10}{'|':^}{'DIRECCIÓN':^15}")
        print("_"*33)
        with open("./archivos/empleados.txt", encoding="utf8") as empleadosTXT:
            for linea in empleadosTXT:
                datos = linea.strip().split('|')
                print(f"{datos[0]:<5}{'|':^}{datos[1]:^10}{'|':^}{datos[2]:^15}{'|':^}")
        empleadosTXT.close()
        

    @staticmethod
    def buscarEmpleado(): #Falta agregar si el usuario no existe imprimirlo por pantalla
        while True:
            try:
                idEmpleado = int(input("\nIntroduce el ID que quieres buscar: "))
                break
            except:
                print("_"*30)
                print("¡Error, digite solo números enteros!\nIntente de nuevo...")
                print("_"*30)
                input("Pulsa cualquier tecla para continuar...")
        with open("./archivos/empleados.txt","r",encoding="utf8") as empleadosTXT:
            lineas = empleadosTXT.readlines()
            for linea in lineas:
                if str(idEmpleado) == linea.split("|")[0]:
                    verificador = True #Si el idEmpleado existe en la lista verificador se queda en Trua y procede a borrar
                    break
                else:
                    verificador = False #Si no existe en la lista se queda en False e imprime por pantalla que no existe
            if verificador == False:
                print("_"*35)
                print("ID no existe!")
                print("_"*35)
                input("Pulsa cualquier tecla para continuar...")
            empleadosTXT.close()
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




