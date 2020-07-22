class Video:

    def __init__(self, idVideo, nombre, url, fechaPublicacion):
        self.__idVideo = idVideo
        self.__nombre = nombre
        self.__url = url
        self.__fechaPublicacion = fechaPublicacion

    @property
    def idVideo(self):
        return self.__idVideo

    @idVideo.setter
    def idVideo(self, valor):
        self.__idVideo = valor

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, valor):
        self.__url = valor

    @property
    def fechaPublicacion(self):
        return self.__fechaPublicacion

    @fechaPublicacion.setter
    def fechaPublicacion(self, valor):
        self.__fechaPublicacion = valor