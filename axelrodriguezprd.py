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

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, valor):
        self.__tipo = valor

    def imprimir(self):
        print(f"""Marca: {self.marca}
Color: {self.color}
Tipo: {self.tipo}""")

mouse = Mouse("Logitech", "Negro", "NA")
mouse2 = Mouse("Razer", "Verde", "Gamer")

mouse.imprimir()
mouse2.imprimir()