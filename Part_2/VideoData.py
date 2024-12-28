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
    __slots__ = ['__graf']

    def __init__(self):
        self.__graf = GrafHash.GrafHash()

    def add_video(self, uuid, file):
        if not self.__graf._contains_file(file):
            if uuid not in self.__graf:
                obj_elementdata = ElementData.ElementData(filename=file)
                self.__graf.insert_vertex(uuid, obj_elementdata)
    
    def remove_video(self, uuid):
        if uuid in self.__graf:
            del self.__graf[uuid]

    def load_metadata(self, uuid):
        if uuid in self.__graf:
            path = self.__graf.get(uuid).path
            
            metadata = tinytag.TinyTag.get(path)
            
            if metadata is None:
                print("ERROR: Arxiu MP4 erroni!")
                sys.exit(1)
            
            self.__graf.get(uuid).duration = numpy.ceil(getattr(metadata, 'duration', -1))
            self.__graf.get(uuid).title = getattr(metadata, 'title', "None")
            self.__graf.get(uuid).album = getattr(metadata, 'album', "None")
            self.__graf.get(uuid).artist = getattr(metadata, 'artist', "None")
            self.__graf.get(uuid).composer = getattr(metadata, 'composer', "None")
            self.__graf.get(uuid).genre = getattr(metadata, 'genre', "None")
            self.__graf.get(uuid).date = getattr(metadata, 'year', "None")
            self.__graf.get(uuid).comment = getattr(metadata, 'comment', "None")
                
    def __len__(self):
        return len(self.__graf)

    def get_filename(self,uuid):
        if uuid in self.__graf:
            return self.__graf.get(uuid).filename
   
    def get_path(self,uuid):
        if uuid in self.__graf:
            return self.__graf.get(uuid).path
        
   
    def get_duration(self,uuid):
        if uuid in self.__graf:
            return self.__graf.get(uuid).duration
        
       
    def get_title(self,uuid):
        if uuid in self.__graf:
            return self.__graf.get(uuid).title
        
    def get_album(self,uuid):
        if uuid in self.__graf:
            return  self.__graf.get(uuid).album

    def get_artist(self,uuid):
        if uuid in self.__graf:
            return self.__graf.get(uuid).artist
            
    def get_composer(self,uuid):
        if uuid in self.__graf:
            return self.__graf.get(uuid).composer
            
    def get_genre(self,uuid):
        if uuid in self.__graf:
            return self.__graf.get(uuid).genre

    def get_date(self,uuid):
        if uuid in self.__graf:
            return self.__graf.get(uuid).date

    def get_comment(self,uuid):
        if uuid in self.__graf:
            return self.__graf.get(uuid).comment

    def _get_uuids(self) -> list:
        """Retorna tots els UUIDs disponibles."""
        return list(self.__graf)

    def __repr__(self):
        return f"VideoData({len(self.__graf)} vídeos)"
    
    def __contains__(self, uuid):
        return uuid in self.__graf

    def __iter__(self):
        for uuid in self.__graf:
            yield self.__graf.get(uuid).path
        #return iter(self.__graf)

    def __eq__(self, other):
        if not isinstance(other, VideoData):
            return NotImplemented
        return self.__graf == other.__graf
    
    def __hash__(self):
        return hash(tuple(self.__graf))
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __lt__(self, other):
        return len(self) < len(other)
    
    def read_playlist(self, obj_playlist: PlayList):
        pass
        """n_arestes = len(obj_playlist)-1
        for i in range(n_arestes):
            uuid_1 = obj_playlist[i]
            uuid_2 = obj_playlist[i+1]
            veins_1 = list(self.__graf.edges(uuid_1))
            if uuid_2 in veins_1:
                self.__graf.augmentaPes(uuid_1,uuid_2)
            else:
                self.__graf.insert_edge(uuid_1, uuid_2)"""
    
    def get_video_rank(self, uuid: str) -> int:
        pass
        #return self.__graf.rank(uuid)
    
    def get_next_videos(self, uuid: str):
        pass
        #for nod_post, pes in self.__graf.next_videos(uuid):
         #   yield (nod_post, pes)
    
    def get_previous_videos(self,uuid: str):
        pass
        #for nod_post, pes in self.__graf.previous_videos(uuid):
         #   yield (nod_post, pes)
    
    def get_video_distance(self,uuid1:str,uuid2:str):
        pass
        """cami = self.__graf.camiMesCurt(uuid1, uuid2)
        if cami:
            valor = 0
            for i in range(len(cami)-1):
                valor += self.__graf.get_pes_aresta(cami[i], cami[i+1])
            return (len(cami)-1, valor)
        else:
            return (0,0)"""