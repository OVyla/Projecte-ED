import cfg
import os

class ElementData:
    __slots__ = ['__title', '__artist', '__album', '__composer', '__genre', '__date', '__comment', '__duration', '__filename', '__path']

    def __init__(self, title="", artist="", album="", composer="", genre="", date="", comment="", duration="", filename=""):
        """
        Inicialitza les metadades de l'element a un string buit "" per defecte. Necessariament haura de tenir filename.
        """
        if not filename:
            raise Exception()
        self.__title = title
        self.__artist = artist
        self.__album = album
        self.__composer = composer
        self.__genre = genre
        self.__date = date
        self.__comment = comment
        self.__duration = duration
        self.__filename = filename
        self.__path = os.path.join(cfg.get_root(), filename)

    @property
    def duration(self):
        """
        Retorna la durada del vídeo.
        """
        return self.__duration

    @duration.setter
    def duration(self, value):
        """
        Estableix la durada del vídeo.
        """
        self.__duration = value

    @property
    def filename(self):
        """
        Retorna el nom del fitxer del vídeo.
        """
        return self.__filename

    @filename.setter
    def filename(self, value):
        """
        Estableix el nom del fitxer del vídeo.
        """
        if value != self.__filename:
            raise ValueError
    
    @property
    def title(self):
        """
        Retorna el títol del vídeo.
        """
        return self.__title

    @title.setter
    def title(self, value):
        """
        Estableix el títol del vídeo.
        """
        self.__title = value

    @property
    def artist(self):
        """
        Retorna l'artista del vídeo.
        """
        return self.__artist

    @artist.setter
    def artist(self, value):
        """
        Estableix l'artista del vídeo.
        """
        self.__artist = value

    @property
    def album(self):
        """
        Retorna l'àlbum del vídeo.
        """
        return self.__album

    @album.setter
    def album(self, value):
        """
        Estableix l'àlbum del vídeo.
        """
        self.__album = value

    @property
    def composer(self):
        """
        Retorna el compositor del vídeo.
        """
        return self.__composer

    @composer.setter
    def composer(self, value):
        """
        Estableix el compositor del vídeo.
        """
        self.__composer = value

    @property
    def genre(self):
        """
        Retorna el gènere del vídeo.
        """
        return self.__genre

    @genre.setter
    def genre(self, value):
        """
        Estableix el gènere del vídeo.
        """
        self.__genre = value

    @property
    def date(self):
        """
        Retorna la data del vídeo.
        """
        return self.__date

    @date.setter
    def date(self, value):
        """
        Estableix la data del vídeo.
        """
        self.__date = value

    @property
    def comment(self):
        """
        Retorna el comentari sobre el vídeo.
        """
        return self.__comment

    @comment.setter
    def comment(self, value):
        """
        Estableix un comentari sobre el vídeo.
        """
        self.__comment = value
        
    @property
    def path(self):
        """
        Retorna el camí absolut del fitxer del vídeo.
        """
        return self.__path

    @path.setter
    def path(self, value):
        """
        Estableix el camí absolut del fitxer del vídeo.
        """
        self.__path = value

    def __hash__(self):
        """
        Retorna el hash de l'element basat en el nom del fitxer.
        """
        return hash(self.__filename)

    def __eq__(self, other):
        """Compara la igualtat del hash amb un altre objecte hash"""
        if not isinstance(other, ElementData):
            return NotImplemented
        return self.__filename == other.__filename
    
    def __ne__(self, other):
        """Compara la desigualtat del hash amb un altre objecte hash"""
        return not self == other
    
    def __lt__(self, other):
        """Compara la mida del hash amb un altre objecte hash"""
        if not isinstance(other, ElementData):
            return NotImplemented
        return self.__filename < other.__filename

    def __repr__(self):
        """
        Retorna una representació formal de l'element de vídeo.
        """
        return f"ElementData(filename={self.__filename})"
