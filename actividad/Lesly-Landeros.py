class Mouse: 
    def _int_(self, marca, color, tipo):
        self._marca= marca
        self._color= color
        self._tipo= tipo

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca: (self, valor):
        self._marca= valor

    @property
    def color(self):
        return self._color 
    
    @color.setter
    def color: (self, valor):
        self._color= valor 
    
    @property
    def tipo(self):
        return self._tipo 

    @tipo.setter
    def tipo: (self, valor):
        self._tipo=  
    
    def imprimir (self):
        print (f'Mouse: {self.marca}, tipo: {self.tipo}, color: {self.color}')
