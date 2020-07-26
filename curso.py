class Curso:

    def __init__(self, idCurso, descripcion, idEmpleado):
        self.__idCurso = idCurso
        self.__descripcion = descripcion
        self.__idEmpleado = idEmpleado

    @property
    def idCurso(self):
        return self.__idCurso
    
    @idCurso.setter
    def idCurso(self, valor):
        self.__idCurso = valor

    @property
    def descripcion(self):
        return self.__descripcion
    
    @descripcion.setter
    def descripcion(self, valor):
        self.__descripcion = valor
    
    @property
    def idEmpleado(self):
        return self.__idEmpleado

    @idEmpleado.setter
    def idEmpelado(self, valor):
        self.__idEmpleado = valor

    @staticmethod #Listo
    def agregarCurso():
        while True:
            while True:
                try:
                    idCurso=int(input("Ingresar el ID: "))
                    break
                except:
                    print("\n¡Error, digite solo enteros!\nIntente de nuevo...\n")
            with open("./archivos/cursos.txt","r",encoding="utf8") as cursosTXT:
                lineas = cursosTXT.readlines()
                for linea in lineas:
                    if str(idCurso) == linea.split("|")[0]:
                        print("\nID ya existe!\n")
                        cursosTXT.close()
                        break
                else:
                    descripcion = input("Descripcion: ")
                    idEmpleado = int(input("Ingrese Id del empleado: "))
                    Curso(idCurso, descripcion, idEmpleado)
                    cursosTXT = open("./archivos/cursos.txt", "a", encoding = "utf8")
                    cursosTXT.write(f"{idCurso}|{descripcion}|{idEmpleado}\n")
                    print("="*31)
                    print("\nCurso agregado exitosamente!\n")
                    print("="*31)
                    cursosTXT.close()
                    break

    @staticmethod #Listo
    def borrarCurso():
        while True:
            nuevaLista = []
            while True:
                try:
                    idCurso = int(input("ID a borrar: "))
                    break
                except:
                        print("_"*30)
                        print("¡Error, digite solo números enteros!\nIntente de nuevo...")
                        print("_"*30)
                        input("Pulsa cualquier tecla para continuar...")               
            with open("./archivos/cursos.txt","r", encoding="utf8") as cursosTXT:
                lineas = cursosTXT.readlines()
                for linea in lineas:
                    if str(idCurso) == linea.split("|")[0]:
                        verificador=True
                        break
                    else:
                        verificador=False
                if verificador == False:
                    print("_"*35)
                    print("ID no existe!")
                    print("_"*35)
                    input("Pulsa cualquier tecla para continuar...")
                cursosTXT.close() 

                if verificador ==True:
                    with open("./archivos/cursos.txt","w", encoding="utf8") as cursosTXT:
                        for linea in cursosTXT:
                            if linea.split("|")[0] != str(idCurso):
                                nuevaLista.append(linea)
                        cursosTXT.close()
                        with open("./archivos/cursos.txt","w", encoding="utf8") as cursosW:
                            for n in nuevaLista:
                                cursosW.write(str(n))
                        print("_"*30)
                        print("Curso Borrado existosamente!")
                        print("_"*30)
                        input("Pulsa cualquier tecla para continuar...")
                        cursosW.close()
                        break 

    @staticmethod
    def modificarCurso():
        pass

    @staticmethod
    def mostrarCurso():
        print(f"{'ID':<5}{'DESCRIPCION':^10}{'IdEmpleado':>15}")
        print("_"*31)
        with open("./archivos/cursos.txt", encoding="utf8") as cursosTXT:
            for linea in cursosTXT:
                datos = linea.strip().split('|')
                print(f"{datos[0]:<5}{datos[1]:^10}{datos[2]:>15}")
        cursosTXT.close()

    @staticmethod
    def buscarCurso(self):
        pass
           
