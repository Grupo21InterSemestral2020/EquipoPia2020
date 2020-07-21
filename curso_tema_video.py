class CursoTV:
    def __init__(self,idCursoTV,idCurso_Tema,idVideo):
        self.__idCursoTV=idCursoTV
        self.__idCurso_Tema=idCurso_Tema
        self.__idVideo=idVideo
    
    @property
    def idCursoTV(self):
        return self.__idCursoTV
    
    @idCursoTV.setter
    def idCursoTV(self,valor):
        self.__idCursoTV=valor
    
    @property
    def idCurso_Tema(self):
        return self.__idCurso_Tema
    
    @idCurso_Tema.setter
    def idCurso_Tema(self,valor):
        self.__idCurso_Tema=valor
    
    @property
    def idVideo (self):
        return self.__idVideo
    
    @idVideo.setter
    def idVideo(self,valor):
        self.__idVideo=valor