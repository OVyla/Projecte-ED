import cfg
import os

class ElementData:
    __slots__ = ['_title', '_artist', '_album', '_composer', '_genre', '_date', '_comment', '_duration', '_filename', '_path']

    def __init__(self, title="", artist="", album="", composer="", genre="", date="", comment="", duration="", filename=""):
        if not filename:
            raise Exception()
        self._title = title
        self._artist = artist
        self._album = album
        self._composer = composer
        self._genre = genre
        self._date = date
        self._comment = comment
        self._duration = duration
        self._filename = filename
        self._path = os.path.join(cfg.get_root(), filename)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        #if not value:
         #   value = "None"
        self._title = value

    @property
    def artist(self):
        return self._artist

    @artist.setter
    def artist(self, value):
        #if not value:
         #   value = "None"
        self._artist = value

    @property
    def album(self):
        return self._album

    @album.setter
    def album(self, value):
        #if not value:
         #   value = "None"
        self._album = value

    @property
    def composer(self):
        return self._composer

    @composer.setter
    def composer(self, value):
        #if not value:
         #   value = "None"
        self._composer = value

    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, value):
        #if not value:
         #   value = "None"
        self._genre = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        #if not value:
         #   value = "None"
        self._date = value

    @property
    def comment(self):
        return self._comment

    @comment.setter
    def comment(self, value):
        #if not value:
         #   value = "None"
        self._comment = value

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        #if not value:
         #   value = -1
        self._duration = value

    @property
    def filename(self):
        return self._filename

    @filename.setter
    def filename(self, value):
        if value != self._filename:
            raise ValueError
        
    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        self._path = value

    def __hash__(self):
        return hash(self._filename)

    def __eq__(self, other):
        if not isinstance(other, ElementData):
            return NotImplemented
        return self._filename == other._filename
    
    def __ne__(self, other):
        return not self == other
    
    def __lt__(self, other):
        if not isinstance(other, ElementData):
            return NotImplemented
        return self._filename < other._filename

    def __repr__(self):
        return f"ElementData(filename={self._filename})"
