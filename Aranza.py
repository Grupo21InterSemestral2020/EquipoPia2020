class mouse:
    def __int__(self,marca,color,tipo):
        self.__marca= marca
        self.__color= color
        self.__tipo= tipo

    @property
    def marca(self):
        return self.__marca

    @property
    def color(self):
        return self.__color

     @property
    def tipo(self):
        return self.__tipo
