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