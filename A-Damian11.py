class Mouse:

    def __init__(self,marca,tipo,color):
        self.__marca = marca
        self.__tipo = tipo
        self.__color = color

    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, valor):
        self.__marca = valor

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self,valor):
        self.__tipo = valor

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self,valor):
        self.__color = valor

    def imprimir(self):
        print(f"Marca: {self.marca}\nColor: {self.color }\nTipo: {self.tipo}\n")


m1 = Mouse('HP','ROJO','INHALAMBRICO')
m2 = Mouse('SONY','NEGRO','ALAMBRICO')

m1.imprimir()
m2.imprimir()
