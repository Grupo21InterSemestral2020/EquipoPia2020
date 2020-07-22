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

    @Nombre.setter
    def nombre(setter, valor):
        self.__nombre = valor

    @staticmethod
    def agregarTema():
        while True:
            idTema = input("Ingresa el ID: ")
            with open#chale no se
            lineas = temaTXT.readlines()
            for linea in lineas:
                if idTema in linea:
                    print("\nID ya existe!\n")
                        temaTXT.close()
                        break
                else:
                    nombre = input("Nombre: ")
                    #Tema(idTema,nombre)
                    #temaTXT = open("./archivos/empleados.txt", "a", encoding = "utf8")
                    #temaTXT.write(f"{idTema}|{nombre}|\n")
                    #print("="*31)
                    #print("\nEmpleado agregado exitosamente!\n")
                    #print("="*31)
                    #temaTXT.close()
                    break

    @staticmethod
     def mostrarTemas():
        print(f"{'ID':<5}{'NOMBRE':^10}")
        print("_"*31)
        with open("./archivos/tema.txt", encoding="utf8") as empleadosTXT:
            for linea in temaTXT:
                datos = linea.strip().split('|')
                print(f"{datos[0]:<5}{datos[1]:^10}{datos[2]:>15}")
        temaTXT.close()



    def buscarTema(self):
        pass
