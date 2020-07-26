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
                    print("¡Error, digite solo numeros enteros!\nIntente de nuevo...")
                    print("_"*30)
                    input("Pulsa cualquier tecla para continuar...")
            with open("./archivos/temas.txt","r",encoding="utf8") as temasTXT:
                lineas = temasTXT.readlines()
                for linea in lineas:
                    if str(idTema) == linea.split("|")[0]:
                        print("_"*35)
                        print("ID ya existe!")
                        print("_"*35)
                        input("Pulsa cualquier tecla para continuar...")
                        temasTXT.close()
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
            with open("./archivos/temas.txt","r",encoding="utf8")as temasTXT: 
                lineas = temasTXT.readlines()
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
                temasTXT.close()

            #Si el ID si existe entonces hara esto y lo borrara
            if verificador == True:
                with open("./archivos/temas.txt","r",encoding="utf8")as temasTXT:
                    for linea in temasTXT:
                        if linea.split("|")[0] != str(idTema):
                            nuevaLista.append(linea)
                    temasTXT.close()
                    with open("./archivos/temas.txt","w", encoding="utf8") as temasW:
                            for n in nuevaLista:
                                temasW.write(str(n))
                    print("_"*30)
                    print("Borrado existosamente!")
                    print("_"*30)
                    input("Pulsa cualquier tecla para continuar...")
                    temasW.close()
                    break #Break del ciclo inicial

    @staticmethod
    def modificarTema():
        while True:
            try:
                idTema = int(input("\nIngresa el Id a modificar: "))
                break
            except:
                print("_"*30)
                print("¡Error, digite solo números enteros!\nIntente de nuevo...")
                print("_"*30)
                input("Pulsa cualquier tecla para continuar...")
        #Verifica si el usuario existe o no en la lista
        with open("./archivos/temas.txt","r",encoding="utf8") as temasTXT:
            lineas = temasTXT.readlines()
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
                temasTXT.close()
            elif verificador == True:
                    nombre = input("Ingresa el nuevo nombre: ")
                    print("_"*35)
                    print("\nModificacion existosa!\n")
                    print("_"*35)
                    input("Pulsa cualquier tecla para continuar...")
                    listaCambios = [] #En esta lista se guarda la lista actual sin cambios
                    listaCambios2 = [] #En esta lista se guarda todos los datos incluidos los cambios
                    temasTXT = open("./archivos/temas.txt","r",encoding="utf8")
                    readlines = temasTXT.readlines()
                    for line in readlines:  
                        line = line.replace("\n","")
                        listaCambios.append(line)
                    for linea in listaCambios:
                        datos = linea.split("|")
                        if datos[0] == str(idTema): #Si el idTema del txt es igual al idTema ingresado por el usuario se hace el cambio
                                datosNuevos = datos[1].replace(datos[1], nombre)
                                datosCambiados = (datos[0] + "|" + datosNuevos + "\n")
                                listaCambios2.append(datosCambiados)
                        else: #Si no solo agrega la linea igual a como estaba
                            datos = (linea + "\n")
                            listaCambios2.append(datos)
                    temasTXT.close()
                    temasTXTW = open("./archivos/temas.txt","w",encoding="utf8")
                    for i in listaCambios2:
                        temasTXTW.write(i)
                    temasTXTW.close()

    @staticmethod
    def mostrarTemas():
        print("_"*25)
        print(f"{'ID':^5}{'|':^}{'NOMBRE':^10}")
        print("_"*25)
        with open("./archivos/temas.txt", encoding="utf8") as temasTXT:
            for linea in temasTXT:
                datos = linea.strip().split('|')
                print(f"{datos[0]:<5}{'|':^}{datos[1]:^10}")
        temasTXT.close()

    @staticmethod
    def buscarTema():
        while True:
            try:
                idTema = int(input("\nIntroduce el ID que quieres buscar: "))
                break
            except:
                print("_"*30)
                print("¡Error, digite solo números enteros!\nIntente de nuevo...")
                print("_"*30)
                input("Pulsa cualquier tecla para continuar...")
        with open("./archivos/temas.txt","r",encoding="utf8") as temasTXT:
            lineas = temasTXT.readlines()
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
            temasTXT.close()
        with open("./archivos/temas.txt","r",encoding="utf8") as temasTXT:
            for linea in temasTXT:
                datos = linea.split("|")
                datoID = linea.split("|")[0]
                if datoID == str(idTema):
                    print(f"{'ID':<5}{'NOMBRE':^10}")
                    print("_"*31)
                    print(f"{datos[0]:<5}{datos[1]:^10}")
                    temasTXT.close()
                    break