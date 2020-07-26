class Curso_Tema:
    def __init__(self,idCursoTema,idCurso,idTema):
        self.__idCursoTema =idCursoTema
        self.__idCurso=idCurso
        self.__idTema=idTema

    @property
    def idCursoTema(self):
        return self.__idCursoTema
    
    @idCursoTema.setter
    def idCursoTema(self,valor):
        self.__idCursoTema=valor

    @property
    def idCurso(self):
        return self.__idCurso
    
    @idCurso.setter
    def idCurso(self,valor):
        self.__idCurso=valor
    
    @property
    def idTema(self):
        return self.__idTema
    
    @idTema.setter
    def idTema(self,valor):
        self.__idTema=valor

        @staticmethod #Listo
    def agregarCurso_Tema():
        while True:
            while True:
                try:
                    idCursoTema = int(input("\nIngresa el ID: "))
                    break
                except:
                    print("_"*30)
                    print("¡Error, digite solo números enteros!\nIntente de nuevo...")
                    print("_"*30)
                    input("Pulsa cualquier tecla para continuar...")
            with open("./archivos/Curso_Tema.txt","r",encoding="utf8") as Curso_TemaTXT:
                lineas = Curso_TemaTXT.readlines()
                for linea in lineas:
                    if str(idCursoTema) == linea.split("|")[0]:
                        print("_"*35)
                        print("ID ya existe!")
                        print("_"*35)
                        input("Pulsa cualquier tecla para continuar...")
                        Curso_TemaTXT.close()
                        break
                else:
                    nombre = input("Nombre: ")
                    direccion = input("Dirección: ")
                    Curso_Tema(idCursoTema, nombre, direccion)
                    Curso_TemaTXT = open("./archivos/Curso_Tema.txt", "a", encoding = "utf8")
                    Curso_TemaTXT.write(f"{idCursoTema}|{nombre}|{direccion}\n")
                    print("="*31)
                    print("\nCurso_Tema agregado exitosamente!\n")
                    print("="*31)
                    Curso_TemaTXT.close()
                    break

    @staticmethod
    def borrarCurso_Tema():
        while True: #Ciclo principal, el ciclo se apaga cuando se borra el Curso_Tema
            nuevaLista = []
            while True:#Este ciclo valida que solo introduzca numeros enteros
                try:
                    idCursoTema = int(input("\nID a borrar: "))
                    break #Sale del ciclo si el usuario introduce un entero
                except:
                    print("_"*30)
                    print("¡Error, digite solo números enteros!\nIntente de nuevo...")
                    print("_"*30)
                    input("Pulsa cualquier tecla para continuar...")

            #Verifica si el usuario existe o no en la lista
            with open("./archivos/Curso_Tema.txt","r",encoding="utf8") as Curso_TemaTXT:
                lineas = Curso_TemaTXT.readlines()
                for linea in lineas:
                    if str(idCursoTema) == linea.split("|")[0]:
                        verificador = True #Si el idCursoTema existe en la lista verificador se queda en True y procede a borrar
                        break
                    else:
                        verificador = False #Si no existe en la lista se queda en False e imprime por pantalla que no existe
                if verificador == False:
                    print("_"*35)
                    print("ID no existe!")
                    print("_"*35)
                    input("Pulsa cualquier tecla para continuar...")
                Curso_TemaTXT.close()

            #Si el ID si existe entonces hará esto y borrara
            if verificador == True:
                with open("./archivos/Curso_Tema.txt","r", encoding="utf8") as Curso_TemaTXT:
                    for linea in Curso_TemaTXT:
                        if linea.split("|")[0] != str(idCursoTema):
                            nuevaLista.append(linea)
                    Curso_TemaTXT.close()
                    with open("./archivos/Curso_Tema.txt","w", encoding="utf8") as Curso_TemaTXT:
                        for n in nuevaLista:
                            Curso_TemaTXT.write(str(n))
                    print("_"*30)
                    print("Borrado existosamente!")
                    print("_"*30)
                    input("Pulsa cualquier tecla para continuar...")
                    Curso_TemaTXT.close()
                    break #Break del ciclo inicial

    @staticmethod
    def modificarCurso_Tema():
        while True:
            try:
                idCursoTema = int(input("\nIngresa el ID a modificar: "))
                break
            except:
                print("_"*30)
                print("¡Error, digite solo números enteros!\nIntente de nuevo...")
                print("_"*30)
                input("Pulsa cualquier tecla para continuar...")
        #Verifica si el usuario existe o no en la lista
        with open("./archivos/Curso_Tema.txt","r",encoding="utf8") as CursoTemaTXT:
            lineas = Curso_TemasTXT.readlines()
            for linea in lineas:
                if str(idCursoTema) == linea.split("|")[0]:
                    verificador = True #Si el idCursoTema existe en la lista verificador se queda en Trua y procede a borrar
                    break
                else:
                    verificador = False #Si no existe en la lista se queda en False e imprime por pantalla que no existe
            if verificador == False:
                print("_"*35)
                print("ID no existe!")
                print("_"*35)
                input("Pulsa cualquier tecla para continuar...")
                Curso_TemaTXT.close()
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
                Curso_TemaTXT = open("./archivos/Curso_Tema.txt","r",encoding="utf8")
                readlines = Curso_TemaTXT.readlines()
                for line in readlines:
                    line = line.replace("\n","")
                    listaCambios.append(line)
                for linea in listaCambios:
                    datos = linea.split("|")
                    if datos[0] == str(idCursoTema):
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
                Curso_TemaTXT.close()
                Curso_TemaTXTW = open("./archivos/Curso_Tema.txt","w",encoding="utf8")
                for i in listaCambios2:
                    Curso_TemaTXTW.write(i)
                Curso_TemaTXTW.close()

    @staticmethod #Listo
    def mostrarCurso_Tema():
        print("_"*33)
        print(f"{'ID':^5}{'|':^}{'NOMBRE':^10}{'|':^}{'DIRECCIÓN':^15}")
        print("_"*33)
        with open("./archivos/Curso_Tema.txt", encoding="utf8") as Curso_TemaTXT:
            for linea in Curso_TemaTXT:
                datos = linea.strip().split('|')
                print(f"{datos[0]:<5}{'|':^}{datos[1]:^10}{'|':^}{datos[2]:^15}{'|':^}")
        Curso_TemaTXT.close()
        

    @staticmethod
    def buscarCurso_Tema(): #Falta agregar si el usuario no existe imprimirlo por pantalla
        while True:
            try:
                idCursoTema = int(input("\nIntroduce el ID que quieres buscar: "))
                break
            except:
                print("_"*30)
                print("¡Error, digite solo números enteros!\nIntente de nuevo...")
                print("_"*30)
                input("Pulsa cualquier tecla para continuar...")
        with open("./archivos/Curso_Tema.txt","r",encoding="utf8") as Curso_TemaTXT:
            lineas = Curso_TemaTXT.readlines()
            for linea in lineas:
                if str(idCursoTema) == linea.split("|")[0]:
                    verificador = True #Si el idCursoTema existe en la lista verificador se queda en Trua y procede a borrar
                    break
                else:
                    verificador = False #Si no existe en la lista se queda en False e imprime por pantalla que no existe
            if verificador == False:
                print("_"*35)
                print("ID no existe!")
                print("_"*35)
                input("Pulsa cualquier tecla para continuar...")
            Curso_TemaTXT.close()
        with open("./archivos/Curso_Tema.txt","r",encoding="utf8") as Curso_TemaTXT:
            for linea in Curso_TemaTXT:
                datos = linea.split("|")
                datoID = linea.split("|")[0]
                if datoID == str(idCursoTema):
                    print(f"{'ID':<5}{'NOMBRE':^10}{'DIRECCION':>15}")
                    print("_"*31)
                    print(f"{datos[0]:<5}{datos[1]:^10}{datos[2]:>15}")
                    Curso_TemaTXT.close()
                    break