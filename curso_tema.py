class Curso_Tema:
    def __init__(self,idCursoTema,idCurso,idTema):
        self.__idCursoTema =idCursoTema
        self.__idCurso=idCurso
        self.__idTema=idTema

    @property
    def idCursoTema(self):
        return self.__idCursoTema
    
    @idCursoTema.setter
    def idCursoTema(self,valor):
        self.__idCursoTema=valor

    @property
    def idCurso(self):
        return self.__idCurso
    
    @idCurso.setter
    def idCurso(self,valor):
        self.__idCurso=valor
    
    @property
    def idTema(self):
        return self.__idTema
    
    @idTema.setter
    def idTema(self,valor):
        self.__idTema=valor