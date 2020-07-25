class Tema:

    def __init__(self, idTema, nombre):
        self.__idTema = idTema
        self.__nombre = nombre

    @property
    def idTema(self):
        return self.__idTema

    @idTema.setter
    def idTema(self, valor):
        self.__idTema = valor

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    @staticmethod
    def agregarTema():
        while True:
            while True:
                try:
                    idTema = int(input("Ingresa el ID: "))
                    break
                except:
                    print("_"*30)
                    print("¡Error, digite solo numeros enteros!\nIntente de nuevo..."
                    print("_"*30)
                    input("Pulsa cualquier tecla para continuar...")
            with open("./archivos/tema.txt","r",encoding="utf8")as temaTXT:
                lineas = temaTXT.readlines()
                for linea in lineas:
                    if str(idTema) == linea.split("|")[0]:
                        print("_"*35)
                        print("ID ya existe!")
                        print("_"*35)
                        input("Pulsa cualquier tecla para continuar...")
                        temaTXT.close()
                        break
                else:
                    nombre = input("Nombre: ")
                    Tema(idTema,nombre)
                    temasTXT = open("./archivos/temas.txt", "a", encoding = "utf8")
                    temasTXT.write(f"{idTema}|{nombre}\n")
                    print("="*31)
                    print("\nTema agregado exitosamente!\n")
                    print("="*31)
                    temasTXT.close()
                    break

    @staticmethod 
    def borrarTema():
        while True: #Ciclo principal, el ciclo se apaga cuando se borra el empleado
        nuevaLista = []
        while True: #Solo numeros enteros
            try:
                idTema = int(input("\nID a borrar: "))
                break #Sale del ciclo si introducen un numero entero
            except:
                 print("_"*30)
                    print("¡Error, digite solo números enteros!\nIntente de nuevo...")
                    print("_"*30)
                    input("Pulsa cualquier tecla para continuar...")

        #Verifica si el usuario existe o no en la lista
        with open("./archivos/tema.txt","r",encoding="utf8")as temaTXT: 
            lineas = temaTXT.readlines()
            for linea in lineas:
                if str(idTema) == linea.split("|")[0]:   
                    verificador = True #si el empleado existe en la lista verificador
                    break
                else:
                    verificador = False #Si no existe en la lista se queda en False e imprime por pantalla que no existe
            if verificador == False:
                    print("_"*35)
                    print("ID no existe!")
                    print("_"*35)
                    input("Pulsa cualquier tecla para continuar...")
            temaTXT.close()

        #Si el ID si existe entonces hara esto y lo borrara
        if verificador == True:
            with open("./archivos/tema.txt","r",encoding="utf8")as temaTXT:
                for linea in temaTXT:
                    if linea.split("|")[0] != str(idTema):
                        nuevaLista.append(linea)
                temaTXT.close()
                with open("./archivos/tema.txt","w", encoding="utf8") as temaW:
                        for n in nuevaLista:
                            temaW.write(str(n))
                print("_"*30)
                print("Borrado existosamente!")
                print("_"*30)
                input("Pulsa cualquier tecla para continuar...")
                temaW.close()
                break #Break del ciclo inicial

    @staticmethod
    def modificarTema():
        while True:
            try:
                idTema = int(input("\nIngresa el Id a modificar"))
                break
            except:
                print("_"*30)
                print("¡Error, digite solo números enteros!\nIntente de nuevo...")
                print("_"*30)
                input("Pulsa cualquier tecla para continuar...")
        #Verifica si el usuario existe o no en la lista
        with open("./archivos/tema.txt","r",encoding="utf8") as temaTXT:
            lineas = temaTXT.readlines()
            for linea in lineas:
                if str(idTema) == linea.split("|")[0]:
                    verificador = True #Si el idTema existe en la lista verificador se queda en Trua y procede a borrar
                    break
                else:
                    verificador = False #Si no existe en la lista se queda en False e imprime por pantalla que no existe
            if verificador == False:
                print("_"*35)
                print("ID no existe!")
                print("_"*35)
                input("Pulsa cualquier tecla para continuar...")
                temaTXT.close()
            elif verificador == True:
                eleccionMod = input("\n¿Que dato quieres modificar?\n1.- Nombre\nIngresa una opcion: ")
                if eleccionMod == "1":
                    nombre = input("Ingresa el nuevo nombre: ")
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
                temaTXT = open("./archivos/tema.txt","r",encoding="utf8")
                readlines = temaTXT.readlines()
                for line in readlines:
                    line = line.replace("\n","")
                    listaCambios.append(line)
                for linea in listaCambios:
                    datos = linea.split("|")
                    if datos[0] == str(idTema):
                        if eleccionMod == "1":
                            datosNuevos = datos[1].replace(datos[1], nombre + "|"  )
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
    def mostrarTemas():
        print("_"*33)
        print(f"{'ID':^5}{'|':^}{'NOMBRE':^10}")
        print("_"*33)
        with open("./archivos/tema.txt", encoding="utf8") as temaTXT:
            for linea in temaTXT:
                datos = linea.strip().split('|')
                print(f"{datos[0]:<5}{'|':^}{datos[1]:^10}{'|':^}{datos[2]:^15}{'|':^}")
        temaTXT.close()
        

    @staticmethod
    def buscarTema(): #Falta agregar si el usuario no existe imprimirlo por pantalla
        while True:
            try:
                idEmpleado = int(input("\nIntroduce el ID que quieres buscar: "))
                break
            except:
                print("_"*30)
                print("¡Error, digite solo números enteros!\nIntente de nuevo...")
                print("_"*30)
                input("Pulsa cualquier tecla para continuar...")
        with open("./archivos/tema.txt","r",encoding="utf8") as temaTXT:
            lineas = temaTXT.readlines()
            for linea in lineas:
                if str(idTema) == linea.split("|")[0]:
                    verificador = True #Si el idEmpleado existe en la lista verificador se queda en Trua y procede a borrar
                    break
                else:
                    verificador = False #Si no existe en la lista se queda en False e imprime por pantalla que no existe
            if verificador == False:
                print("_"*35)
                print("ID no existe!")
                print("_"*35)
                input("Pulsa cualquier tecla para continuar...")
            temaTXT.close()
        with open("./archivos/tema.txt","r",encoding="utf8") as temaTXT:
            for linea in temaTXT:
                datos = linea.split("|")
                datoID = linea.split("|")[0]
                if datoID == str(idEmpleado):
                    print(f"{'ID':<5}{'NOMBRE':^10}")
                    print("_"*31)
                    print(f"{datos[0]:<5}{datos[1]:^10}{datos[2]:>15}")
                    temaTXT.close()
                    break



    