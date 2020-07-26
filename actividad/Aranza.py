class mouse:
    def __int__(self,marca,color,tipo):
        self.__marca= marca
        self.__color= color
        self.__tipo= tipo

    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self,valor):
        return self.__marca = valor

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self,valor):
        return self.__color = valor

     @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self,valor):
        return self.__tipo = valor

    def imprimir(self):
        print(f"marca: {self.__marca},color: {self.__color},tipo: {self.__tipo}")

mouse = Mouse("Vochito","Rojo","Pretzel")
mouse = imprimir()