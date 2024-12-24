# -*- coding: utf-8 -*-
import cfg
from GrafHash import GrafHash
from ElementData import ElementData

import tinytag
import numpy
import os

class VideoData:

    __slots__ = ['_files']


    def __init__(self):
        self._files = GrafHash()


    def add_video(self, uuid: str, file: str):
        if uuid not in self._files:
            try:
               
                path = os.path.join(cfg.get_root(), file)
                if os.path.isfile(path):
                    element = ElementData(filename=file)
                    self._files.insert_vertex(uuid, element)

            except FileNotFoundError:
                print("ERROR")


    def load_metadata(self, uuid):
        if uuid in self._files:
            element = self._files.get(uuid)
            try:

                path = os.path.join(cfg.get_root(), element.filename)
                metadata = tinytag.TinyTag.get(path)

                if metadata is None:
                    print(f'Error al afegir el video {uuid}')

                else:
                    element.title=metadata.title or None,
                    element.artist=metadata.artist or None,
                    element.album=metadata.album or None,
                    element.composer=metadata.composer or None,
                    element.genre=metadata.genre or None,
                    element.date=metadata.year or None,
                    element.comment=metadata.comment or None,
                    element.duration=int(numpy.ceil(metadata.duration)) if metadata.duration else -1,
                    
                
            except AttributeError:
                print(f'ERROR al carregar les dades: {e}')



    def remove_video(self, uuid: str):
        if uuid in self._files:
            del self._files[uuid]


    def get_metadata(self, uuid):
        if uuid in self._files:
            return self._files[uuid]
        return None

    def get_all_videos(self):
        return self._files.get_uuids()
    
    
    def existeix_meta(self, uuid):
        return self._files.get(uuid).title is not None
    
    def get_filename(self, uuid):
        if self.existeix_meta(uuid):
            return self._files.get(uuid).filename
        return None


    def get_path(self, uuid):
        if self.existeix_meta(uuid):
            return os.path.join(cfg.get_root(), self._files[uuid].uuid())
        return None

    def get_duration(self, uuid):
        if self.existeix_meta(uuid):
            return self._files.get(uuid).duration
        return None
        
    def get_title(self, uuid):
        if self.existeix_meta(uuid):
            return self._files.get(uuid).title
        return None
        
    def get_album(self, uuid):
        if self.existeix_meta(uuid):
            return self._files.get(uuid).album
        return None
        
    def get_artist(self, uuid):
        if self.existeix_meta(uuid):
            return self._files.get(uuid).artist
        return None
        
    def get_composer(self, uuid):
        if self.existeix_meta(uuid):
            return self._files.get(uuid).composer
        return None
        
    def get_genre(self, uuid):
        if self.existeix_meta(uuid):
            return self._files.get(uuid).genre
        return None
        
    def get_date(self, uuid):
        if self.existeix_meta(uuid):
            return self._files.get(uuid).date
        return None
        
    def get_comment(self, uuid):
        if self.existeix_meta(uuid):
            return self._files.get(uuid).comment
        return None
        
    def files(self):
        return {uuid: self._files.get(uuid) for uuid in self._files}

    def get_uuids(self) -> list:
        return list(self._files.vertices())

    

    def __len__(self):
        return len(self._files)

    def __repr__(self):
        return f"VideoData({len(self)} videos)"

    def __iter__(self):
        return iter(self._files)

    def __eq__(self, other):
        if not isinstance(other, VideoData):
            return NotImplemented
        return self._files == other._files

    def __hash__(self):
        return hash(self._files)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return len(self._files) < len(other._files)

    def __str__(self):
        return str(self._files)
    
    def read_playlist(self, playlist):
        pass

    def get_video_rank(self, uuid):
        pass

    def get_next_videos(self, uuid):
        pass

    def get_previous_videos(self, uuid):
        pass

    def get_video_distance(self, uuid1, uuid2):
        pass
    
    def get_previous_videos(self,uuid: str):
        pass
    
    def get_video_distance(self,uuid1:str,uuid2:str):
        pass
