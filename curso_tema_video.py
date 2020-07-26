class CursoTV:
    def __init__(self,idCursoTV,idCurso_Tema,idVideo):
        self.__idCursoTV=idCursoTV
        self.__idCurso_Tema=idCurso_Tema
        self.__idVideo=idVideo
    
    @property
    def idCursoTV(self):
        return self.__idCursoTV
    
    @idCursoTV.setter
    def idCursoTV(self,valor):
        self.__idCursoTV=valor
    
    @property
    def idCurso_Tema(self):
        return self.__idCurso_Tema
    
    @idCurso_Tema.setter
    def idCurso_Tema(self,valor):
        self.__idCurso_Tema=valor
    
    @property
    def idVideo (self):
        return self.__idVideo
    
    @idVideo.setter
    def idVideo(self,valor):
        self.__idVideo=valor

    @staticmethod #Listo
    def agregarCursoTV():
        while True:
            while True:
                try:
                    idCursoTV = int(input("\nIngresa el ID: "))
                    break
                except:
                    print("_"*30)
                    print("¡Error, digite solo números enteros!\nIntente de nuevo...")
                    print("_"*30)
                    input("Pulsa cualquier tecla para continuar...")
            with open("./archivos/ctv.txt","r",encoding="utf8") as ctvTXT:
                lineas = ctvTXT.readlines()
                for linea in lineas:
                    if str(idCursoTV) == linea.split("|")[0]:
                        print("_"*35)
                        print("ID ya existe!")
                        print("_"*35)
                        input("Pulsa cualquier tecla para continuar...")
                        ctvTXT.close()
                        break
                else:
                    idCursoVideo = input("Ingresa el id del Curso-Video: ")
                    idVideo = input("Ingresa el id del Video: ")
                    CursoTV(idCursoTV, idCursoVideo, idVideo)
                    ctvTXT = open("./archivos/ctv.txt", "a", encoding = "utf8")
                    ctvTXT.write(f"{idCursoTV}|{idCursoVideo}|{idVideo}\n")
                    print("="*31)
                    print("\nEmpleado agregado exitosamente!\n")
                    print("="*31)
                    ctvTXT.close()
                    break

    @staticmethod
    def borrarCursoTV():
        while True: #Ciclo principal, el ciclo se apaga cuando se borra el empleado
            nuevaLista = []
            while True:#Este ciclo valida que solo introduzca numeros enteros
                try:
                    idCursoTV = int(input("\nID a borrar: "))
                    break #Sale del ciclo si el usuario introduce un entero
                except:
                    print("_"*30)
                    print("¡Error, digite solo números enteros!\nIntente de nuevo...")
                    print("_"*30)
                    input("Pulsa cualquier tecla para continuar...")

            #Verifica si el usuario existe o no en la lista
            with open("./archivos/ctv.txt","r",encoding="utf8") as ctvTXT:
                lineas = ctvTXT.readlines()
                for linea in lineas:
                    if str(idCursoTV) == linea.split("|")[0]:
                        verificador = True #Si el idEmpleado existe en la lista verificador se queda en Trua y procede a borrar
                        break
                    else:
                        verificador = False #Si no existe en la lista se queda en False e imprime por pantalla que no existe
                if verificador == False:
                    print("_"*35)
                    print("ID no existe!")
                    print("_"*35)
                    input("Pulsa cualquier tecla para continuar...")
                ctvTXT.close()

            #Si el ID si existe entonces hará esto y borrara
            if verificador == True:
                with open("./archivos/ctv.txt","r", encoding="utf8") as ctvTXT:
                    for linea in ctvTXT:
                        if linea.split("|")[0] != str(idCursoTV):
                            nuevaLista.append(linea)
                    ctvTXT.close()
                    with open("./archivos/ctv.txt","w", encoding="utf8") as ctvW:
                        for n in nuevaLista:
                            ctvW.write(str(n))
                    print("_"*30)
                    print("Borrado existosamente!")
                    print("_"*30)
                    input("Pulsa cualquier tecla para continuar...")
                    ctvW.close()
                    break #Break del ciclo inicial

    @staticmethod
    def modificarEmpleado():
        while True:
            try:
                idCursoTV = int(input("\nIngresa el ID a modificar: "))
                break
            except:
                print("_"*30)
                print("¡Error, digite solo números enteros!\nIntente de nuevo...")
                print("_"*30)
                input("Pulsa cualquier tecla para continuar...")
        #Verifica si el usuario existe o no en la lista
        with open("./archivos/ctv.txt","r",encoding="utf8") as ctvTXT:
            lineas = ctvTXT.readlines()
            for linea in lineas:
                if str(idCursoTV) == linea.split("|")[0]:
                    verificador = True #Si el idEmpleado existe en la lista verificador se queda en Trua y procede a borrar
                    break
                else:
                    verificador = False #Si no existe en la lista se queda en False e imprime por pantalla que no existe
            if verificador == False:
                print("_"*35)
                print("ID no existe!")
                print("_"*35)
                input("Pulsa cualquier tecla para continuar...")
                ctvTXT.close()
            elif verificador == True:
                eleccionMod = input("\n¿Que dato quieres modificar?\n1.- ID Curso Video\n2.- ID Video\nIngresa una opcion: ")
                if eleccionMod == "1":
                    idCursoVideo = input("Ingresa el nuevo ID Curso Video: ")
                    print("_"*35)
                    print("\nModificacion existosa!\n")
                    print("_"*35)
                    input("Pulsa cualquier tecla para continuar...")
                elif eleccionMod == "2":
                    idVideo = input("Ingresa la nueva ID Video: ")
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
                ctvTXT = open("./archivos/ctv.txt","r",encoding="utf8")
                readlines = ctvTXT.readlines()
                for line in readlines:
                    line = line.replace("\n","")
                    listaCambios.append(line)
                for linea in listaCambios:
                    datos = linea.split("|")
                    if datos[0] == str(idCursoTV):
                        if eleccionMod == "1":
                            datosNuevos = datos[1].replace(datos[1], idCursoVideo + "|" + datos[2])
                            datosCambiados = (datos[0] + "|" + datosNuevos + "\n")
                            listaCambios2.append(datosCambiados)
                        elif eleccionMod == "2":
                            datosNuevos = datos[1].replace(datos[1], datos[1] + "|" + idVideo)
                            datosCambiados = (datos[0] + "|" + datosNuevos + "\n")
                            listaCambios2.append(datosCambiados)
                    else:
                        datos = (linea + "\n")
                        listaCambios2.append(datos)
                ctvTXT.close()
                ctvTXTW = open("./archivos/ctv.txt","w",encoding="utf8")
                for i in listaCambios2:
                    ctvTXTW.write(i)
                ctvTXTW.close()

    @staticmethod #Listo
    def mostrarCursoTV():
        print("_"*33)
        print(f"{'ID':^5}{'|':^}{'NOMBRE':^10}{'|':^}{'DIRECCIÓN':^15}")
        print("_"*33)
        with open("./archivos/ctv.txt", encoding="utf8") as ctvTXT:
            for linea in ctvTXT:
                datos = linea.strip().split('|')
                print(f"{datos[0]:<5}{'|':^}{datos[1]:^10}{'|':^}{datos[2]:^15}{'|':^}")
        ctvTXT.close()
        

    @staticmethod
    def buscarCursoTV(): #Falta agregar si el usuario no existe imprimirlo por pantalla
        while True:
            try:
                idCursoTV = int(input("\nIntroduce el ID que quieres buscar: "))
                break
            except:
                print("_"*30)
                print("¡Error, digite solo números enteros!\nIntente de nuevo...")
                print("_"*30)
                input("Pulsa cualquier tecla para continuar...")
        with open("./archivos/ctv.txt","r",encoding="utf8") as ctvTXT:
            lineas = ctvTXT.readlines()
            for linea in lineas:
                if str(idCursoTV) == linea.split("|")[0]:
                    verificador = True #Si el idEmpleado existe en la lista verificador se queda en Trua y procede a borrar
                    break
                else:
                    verificador = False #Si no existe en la lista se queda en False e imprime por pantalla que no existe
            if verificador == False:
                print("_"*35)
                print("ID no existe!")
                print("_"*35)
                input("Pulsa cualquier tecla para continuar...")
            ctvTXT.close()
        with open("./archivos/ctv.txt","r",encoding="utf8") as ctvTXT:
            for linea in ctvTXT:
                datos = linea.split("|")
                datoID = linea.split("|")[0]
                if datoID == str(idCursoTV):
                    print(f"{'ID':<5}{'NOMBRE':^10}{'DIRECCION':>15}")
                    print("_"*31)
                    print(f"{datos[0]:<5}{datos[1]:^10}{datos[2]:>15}")
                    ctvTXT.close()
                    break