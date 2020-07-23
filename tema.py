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
                    print("\n¡Error, digite solo enteros!\nIntente de nuevo...\n")
            with open("./archivos/temas.txt","r",encoding="utf8") as temasTXT:
                lineas = temasTXT.readlines()
                for linea in lineas:
                    if str(idTema) == linea.split("|")[0]:
                        print("\nID ya existe!\n")
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
    def mostrarTemas():
        print(f"{'ID':<5}{'NOMBRE':>10}")
        print("_"*20)
        with open("./archivos/temas.txt", encoding="utf8") as temasTXT:
            for linea in temasTXT:
                datos = linea.strip().split('|')
                print(f"{datos[0]:<5}{datos[1]:>10}")
        temasTXT.close()

    def buscarTema(self):
        pass
