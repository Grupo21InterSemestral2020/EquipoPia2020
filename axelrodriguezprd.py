class Mouse:
    def __init__(self, marca, color, tipo):
        self.__marca = marca
        self.__color = color 
        self.__tipo = tipo

    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, valor):
        self.__marca = valor

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, valor):
        self.__color = valor


