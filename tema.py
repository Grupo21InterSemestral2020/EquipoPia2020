class tema:
    def __int__(self,idTema,Nombre):
        self.__idTema = idTema
        self.__Nombre = Nombre

    @property
    def idTema(self):
        return self.__idTema

    @idTema.setter
    def idTema(self,valor):
        self.__idTema = valor

    @property
    def Nombre(self):
        return self.__Nombre

    @Nombre.setter
    def Nombre(setter,valor):
        self.__Nombre = valor