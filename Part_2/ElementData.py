import cfg
import os

class ElementData:
    __slots__ = ['__title', '__artist', '__album', '__composer', '__genre', '__date', '__comment', '__duration', '__filename', '__path']

    def __init__(self, title="", artist="", album="", composer="", genre="", date="", comment="", duration="", filename=""):
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
        return self.__duration

    @duration.setter
    def duration(self, value):
        #if not value:
         #   value = -1
        self.__duration = value

    @property
    def filename(self):
        return self.__filename

    @filename.setter
    def filename(self, value):
        if value != self.__filename:
            raise ValueError
    
    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        #if not value:
         #   value = "None"
        self.__title = value

    @property
    def artist(self):
        return self.__artist

    @artist.setter
    def artist(self, value):
        #if not value:
         #   value = "None"
        self.__artist = value

    @property
    def album(self):
        return self.__album

    @album.setter
    def album(self, value):
        #if not value:
         #   value = "None"
        self.__album = value

    @property
    def composer(self):
        return self.__composer

    @composer.setter
    def composer(self, value):
        #if not value:
         #   value = "None"
        self.__composer = value

    @property
    def genre(self):
        return self.__genre

    @genre.setter
    def genre(self, value):
        #if not value:
         #   value = "None"
        self.__genre = value

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, value):
        #if not value:
         #   value = "None"
        self.__date = value

    @property
    def comment(self):
        return self.__comment

    @comment.setter
    def comment(self, value):
        #if not value:
         #   value = "None"
        self.__comment = value
        
    @property
    def path(self):
        return self.__path

    @path.setter
    def path(self, value):
        self.__path = value

    def __hash__(self):
        return hash(self.__filename)

    def __eq__(self, other):
        if not isinstance(other, ElementData):
            return NotImplemented
        return self.__filename == other.__filename
    
    def __ne__(self, other):
        return not self == other
    
    def __lt__(self, other):
        if not isinstance(other, ElementData):
            return NotImplemented
        return self.__filename < other.__filename

    def __repr__(self):
        return f"ElementData(filename={self.__filename})"
