class mouse:
    def __int__(self,marca,color,tipo):
        self._marca= marca
        self._color= color
        self._tipo= tipo

    @property
    def marca(self):
        return self._marca