# -*- coding: utf-8 -*-
import cfg
import os
import sys
import numpy
import tinytag
import PlayList
import GrafHash
import ElementData
import os.path

class VideoData:
    __slots__ = ['_graf']

    def __init__(self):
        self._graf = GrafHash.GrafHash()

    def add_video(self, uuid, file):
        if not self._graf._contains_file(file):
            obj_elementdata = ElementData.ElementData(filename=file)
            self._graf.insert_vertex(uuid, obj_elementdata)
    
    def remove_video(self, uuid):
        if uuid in self._graf:
            del self._graf[uuid]

    def load_metadata(self, uuid):
        if uuid in self._graf:
            path = self._graf.get(uuid).path

            metadata = tinytag.TinyTag.get(path)
            
            if metadata is None:
                print("ERROR: Arxiu MP4 erroni!")
                sys.exit(1)
            
            self._graf.get(uuid).duration = int(numpy.ceil(metadata.duration))
            self._graf.get(uuid).title = metadata.title
            self._graf.get(uuid).album = metadata.album
            self._graf.get(uuid).artist = metadata.artist
            self._graf.get(uuid).composer = metadata.composer
            self._graf.get(uuid).genre = metadata.genre
            self._graf.get(uuid).date = metadata.year
            self._graf.get(uuid).comment = metadata.comment
    def __len__(self):
        return len(self._graf)

    def get_filename(self,uuid):
        if uuid in self._graf:
            return self._graf.get(uuid).filename
   
    def get_path(self,uuid):
        if uuid in self._graf:
            return self._graf.get(uuid).path
        
   
    def get_duration(self,uuid):
        if uuid in self._graf:
            val = self._graf.get(uuid).duration
            if val:
                return val
            else:
                print('dades esperant a ser carregades')
        
       
    def get_title(self,uuid):
        if uuid in self._graf:
            val = self._graf.get(uuid).title
            if val:
                return val
            else:
                print('dades esperant a ser carregades')
        
    def get_album(self,uuid):
        if uuid in self._graf:
            val =  self._graf.get(uuid).album
            if val:
                return val
            else:
                print('dades esperant a ser carregades')
       
    def get_artist(self,uuid):
        if uuid in self._graf:
            val = self._graf.get(uuid).artist
            if val:
                return val
            else:
                print('dades esperant a ser carregades')
       
    def get_composer(self,uuid):
        if uuid in self._graf:
            val = self._graf.get(uuid).composer
            if val:
                return val
            else:
                print('dades esperant a ser carregades')
       
    def get_genre(self,uuid):
        if uuid in self._graf:
            val = self._graf.get(uuid).genre
            if val:
                return val
            else:
                print('dades esperant a ser carregades')
       
    def get_date(self,uuid):
        if uuid in self._graf:
            val = self._graf.get(uuid).date
            if val:
                return val
            else:
                print('dades esperant a ser carregades')

    def get_comment(self,uuid):
        if uuid in self._graf:
            val = self._graf.get(uuid).comment
            if val:
                return val
            else:
                print('dades esperant a ser carregades')
    
    def _get_uuids(self) -> list:
        """Retorna tots els UUIDs disponibles."""
        return list(self._graf)

    def __repr__(self):
        return f"VideoData({len(self._graf)} vídeos)"

    def __iter__(self):
        for uuid in self._graf:
            yield self._graf.get(uuid).path
        #return iter(self._graf)

    def __eq__(self, other):
        if not isinstance(other, VideoData):
            return NotImplemented
        return self._graf == other._graf
    
    def __hash__(self, other):
        return hash(tuple(self._graf))
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __lt__(self, other):
        return len(self) < len(other)
    
    def read_playlist(self, obj_playlist: PlayList):
        n_arestes = len(obj_playlist)-1
        for i in range(n_arestes):
            uuid_1 = obj_playlist[i]
            uuid_2 = obj_playlist[i+1]
            veins_1 = list(self._graf.edges(uuid_1))
            if uuid_2 in veins_1:
                self._graf.augmentaPes(uuid_1,uuid_2)
            else:
                self._graf.insert_edge(uuid_1, uuid_2)
    
    def get_video_rank(self, uuid: str) -> int:
        return self._graf.rank(uuid)
    
    def get_next_videos(self, uuid: str):
        for nod_post, pes in self._graf.next_videos(uuid):
            yield (nod_post, pes)
    
    def get_previous_videos(self,uuid: str):
        for nod_post, pes in self._graf.previous_videos(uuid):
            yield (nod_post, pes)
    
    def get_video_distance(self,uuid1:str,uuid2:str):
        cami = self._graf.camiMesCurt(uuid1, uuid2)
        if cami:
            valor = 0
            for i in range(len(cami)-1):
                valor += self._graf.get_pes_aresta(cami[i], cami[i+1])
            return (len(cami)-1, valor)
        else:
            return (0,0)