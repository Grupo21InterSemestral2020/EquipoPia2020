
class Mouse:
    def __init__(self,marca,color,tipo):
        self.__marca=marca
        self.__color=color 
        self.__tipo=tipo

    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self,x):
        self.__marca=x

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self,x):
        self.__color=x

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self,x):
        self.__tipo=x

    def ImpInfo(self):
        print(f'Marca:{self.__marca}\nColor:{self.__color}\nTipo:{self.__tipo}')

mouse= Mouse("Hp","Negro","Tipo")
mouse2= Mouse("Steren","Negro","Tipo")

mouse.ImpInfo()
mouse2.ImpInfo()