class video:
    def __int__(self,idVideo,Nombre,url,FechaPublicacion):
        self.__idVideo = idVideo
        self.__Nombre = Nombre
        self.__url = url
        self.__FechaPublicacion = FechaPublicacion

    @property
    def idVideo(self):
        return self.__idVideo

    @idVideo.setter
    def idVideo(self,valor):
        self.__idVideo = valor

    @property
    def Nombre(self):
        return self.__Nombre

    @Nombre.setter
    def Nombre(self,valor):
        self.__Nombre = valor

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self,valor):
        self.__url = valor

    @property
    def FechaPublicacion(self):
        return self.__FechaPublicacion

    @FechaPublicacion.setter
    def FechaPublicacion(self,valor):
        self.__FechaPublicacion = valor