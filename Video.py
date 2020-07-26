class Video:

    def __init__(self, idVideo, nombre, url, fechaPublicacion):
        self.__idVideo = idVideo
        self.__nombre = nombre
        self.__url = url
        self.__fechaPublicacion = fechaPublicacion

    @property
    def idVideo(self):
        return self.__idVideo

    @idVideo.setter
    def idVideo(self, valor):
        self.__idVideo = valor

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, valor):
        self.__url = valor

    @property
    def fechaPublicacion(self):
        return self.__fechaPublicacion

    @fechaPublicacion.setter
    def fechaPublicacion(self, valor):
        self.__fechaPublicacion = valor

    @staticmethod #Listo
    def agregarVideo():
        while True:
            while True:
                try:
                    idVideo = int(input("\nIngresa el ID: "))
                    break
                except:
                    print("_"*30)
                    print("¡Error, digite solo números enteros!\nIntente de nuevo...")
                    print("_"*30)
                    input("Pulsa cualquier tecla para continuar...")
            with open("./archivos/videos.txt","r",encoding="utf8") as videosTXT:
                lineas = videosTXT.readlines()
                for linea in lineas:
                    if str(idVideo) == linea.split("|")[0]:
                        print("_"*35)
                        print("ID ya existe!")
                        print("_"*35)
                        input("Pulsa cualquier tecla para continuar...")
                        videosTXT.close()
                        break
                else:
                    idVideo = input("ID del video: ")
                    nombre = input("Nombre: ")
                    Video(idVideo, nombre, url)
                    videosTXT = open("./archivos/videos.txt", "a", encoding = "utf8")
                    videosTXT.write(f"{idvideo}|{nombre}|{url}\n")
                    print("="*31)
                    print("\nVideo agregado exitosamente!\n")
                    print("="*31)
                    videoTXT.close()
                    break

    @staticmethod
    def borrarVideo():
        while True: #Ciclo principal, el ciclo se apaga cuando se borra el video
            nuevaLista = []
            while True:#Este ciclo valida que solo introduzca numeros enteros
                try:
                    idVideo = int(input("\nID a borrar: "))
                    break #Sale del ciclo si el usuario introduce un entero
                except:
                    print("_"*30)
                    print("¡Error, digite solo números enteros!\nIntente de nuevo...")
                    print("_"*30)
                    input("Pulsa cualquier tecla para continuar...")

            #Verifica si el video existe o no en la lista
            with open("./archivos/video.txt","r",encoding="utf8") as videosTXT:
                lineas = videosTXT.readlines()
                for linea in lineas:
                    if str(idVideo) == linea.split("|")[0]:
                        verificador = True #Si el idVideo existe en la lista verificador se queda en True y procede a borrar
                        break
                    else:
                        verificador = False #Si no existe en la lista se queda en False e imprime por pantalla que no existe
                if verificador == False:
                    print("_"*35)
                    print("ID no existe!")
                    print("_"*35)
                    input("Pulsa cualquier tecla para continuar...")
                videosTXT.close()

            #Si el ID si existe entonces hará esto y borrara
            if verificador == True:
                with open("./archivos/videos.txt","r", encoding="utf8") as videosTXT:
                    for linea in videosTXT:
                        if linea.split("|")[0] != str(idVideo):
                            nuevaLista.append(linea)
                    videosTXT.close()
                    with open("./archivos/videos.txt","w", encoding="utf8") as videosW:
                        for n in nuevaLista:
                            videosW.write(str(n))
                    print("_"*30)
                    print("Borrado existosamente!")
                    print("_"*30)
                    input("Pulsa cualquier tecla para continuar...")
                    videosW.close()
                    break #Break del ciclo inicial

    @staticmethod
    def modificarVideo():
        while True:
            try:
                idvideo = int(input("\nIngresa el ID a modificar: "))
                break
            except:
                print("_"*30)
                print("¡Error, digite solo números enteros!\nIntente de nuevo...")
                print("_"*30)
                input("Pulsa cualquier tecla para continuar...")
        #Verifica si el video existe o no en la lista
        with open("./archivos/videos.txt","r",encoding="utf8") as videosTXT:
            lineas = videosTXT.readlines()
            for linea in lineas:
                if str(idVideo) == linea.split("|")[0]:
                    verificador = True #Si el idEmpleado existe en la lista verificador se queda en True y procede a borrar
                    break
                else:
                    verificador = False #Si no existe en la lista se queda en False e imprime por pantalla que no existe
            if verificador == False:
                print("_"*35)
                print("ID no existe!")
                print("_"*35)
                input("Pulsa cualquier tecla para continuar...")
                videosTXT.close()
            elif verificador == True:
                eleccionMod = input("\n¿Que dato quieres modificar?\n1.- Nombre\n2.- url\nIngresa una opcion: ")
                if eleccionMod == "1":
                    nombre = input("Ingresa el nuevo nombre: ")
                    print("_"*35)
                    print("\nModificacion existosa!\n")
                    print("_"*35)
                    input("Pulsa cualquier tecla para continuar...")
                elif eleccionMod == "2":
                    direccion = input("Ingresa el nuevo url: ")
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
                videosTXT = open("./archivos/videos.txt","r",encoding="utf8")
                readlines = videosTXT.readlines()
                for line in readlines:
                    line = line.replace("\n","")
                    listaCambios.append(line)
                for linea in listaCambios:
                    datos = linea.split("|")
                    if datos[0] == str(idVideo):
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
                videosTXT.close()
                videosTXTW = open("./archivos/videos.txt","w",encoding="utf8")
                for i in listaCambios2:
                    videosTXTW.write(i)
                videosTXTW.close()

    @staticmethod #Listo
    def mostrarVideos():
        print("_"*33)
        print(f"{'ID':^5}{'|':^}{'NOMBRE':^10}{'|':^}{'URL':^15}")
        print("_"*33)
        with open("./archivos/videos.txt", encoding="utf8") as videosTXT:
            for linea in videosTXT:
                datos = linea.strip().split('|')
                print(f"{datos[0]:<5}{'|':^}{datos[1]:^10}{'|':^}{datos[2]:^15}{'|':^}")
        videosTXT.close()
        

    @staticmethod
    def buscarVideo(): #Falta agregar si el video no existe imprimirlo por pantalla
        while True:
            try:
                idVideo = int(input("\nIntroduce el ID que quieres buscar: "))
                break
            except:
                print("_"*30)
                print("¡Error, digite solo números enteros!\nIntente de nuevo...")
                print("_"*30)
                input("Pulsa cualquier tecla para continuar...")
        with open("./archivos/videos.txt","r",encoding="utf8") as videosTXT:
            lineas = videosTXT.readlines()
            for linea in lineas:
                if str(idvideo) == linea.split("|")[0]:
                    verificador = True #Si el idVideo existe en la lista verificador se queda en True y procede a borrar
                    break
                else:
                    verificador = False #Si no existe en la lista se queda en False e imprime por pantalla que no existe
            if verificador == False:
                print("_"*35)
                print("ID no existe!")
                print("_"*35)
                input("Pulsa cualquier tecla para continuar...")
            videosTXT.close()
        with open("./archivos/videos.txt","r",encoding="utf8") as videosTXT:
            for linea in videosTXT:
                datos = linea.split("|")
                datoID = linea.split("|")[0]
                if datoID == str(idVideo):
                    print(f"{'ID':<5}{'NOMBRE':^10}{'URL':>15}")
                    print("_"*31)
                    print(f"{datos[0]:<5}{datos[1]:^10}{datos[2]:>15}")
                    videosTXT.close()
                    break
                    