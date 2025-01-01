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
    """
    OBJECTIU: Gestionar la col·lecció de vídeos i les seves metadades.
    RESPONSABILITAT: Proporcionar funcionalitats per afegir, eliminar i carregar metadades
                     dels vídeos, així com gestionar les relacions entre ells.
    """
    __slots__ = ['__graf']

    def __init__(self):
        """
        Inicialitza la classe VideoData.
        """
        self.__graf = GrafHash.GrafHash()

    def add_video(self, uuid, file):
        """
        Afegeix un vídeo al graf si no existeix.
        """
        if not self.__graf._contains_file(file):  # Comprova si el fitxer ja està en el graf
            if uuid not in self.__graf:  # Comprova si l'UUID no existeix
                obj_elementdata = ElementData.ElementData(filename=file)  # Crea un objecte ElementData
                self.__graf.insert_vertex(uuid, obj_elementdata)  # Afegeix el vídeo al graf
    
    def remove_video(self, uuid):
        """
        Elimina un vídeo del graf.
        """
        if uuid in self.__graf:
            del self.__graf[uuid]

    def load_metadata(self, uuid):
        """
        Carrega les metadades d'un vídeo a partir del seu UUID.
        """
        if uuid in self.__graf:  # Comprova si l'UUID existeix
            path = self.__graf.get(uuid).path  # Obté el camí del fitxer
            
            metadata = tinytag.TinyTag.get(path)  # Llegeix les metadades del fitxer amb la funció de TiniTag importat al principi
            
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
        """
        Retorna el nombre de vídeos en el graf.
        """
        return len(self.__graf)

    def get_filename(self,uuid):
        """
        Retorna el nom del fitxer associat a un UUID.
        """
        if uuid in self.__graf:
            return self.__graf.get(uuid).filename
            
    def get_duration(self,uuid):
        """
        Retorna la durada del vídeo associat a un UUID.
        """
        if uuid in self.__graf:
            return self.__graf.get(uuid).duration
         
    def get_path(self,uuid):
        """
        Retorna el camí del fitxer associat a un UUID.
        """
        if uuid in self.__graf:
            return self.__graf.get(uuid).path    
       
    def get_title(self,uuid):
        """
        Retorna el títol del vídeo associat a un UUID.
        """
        if uuid in self.__graf:
            return self.__graf.get(uuid).title
        
    def get_album(self,uuid):
        """
        Retorna l'àlbum del vídeo associat a un UUID.
        """
        if uuid in self.__graf:
            return  self.__graf.get(uuid).album

    def get_artist(self,uuid):
        """
        Retorna l'artista del vídeo associat a un UUID.
        """
        if uuid in self.__graf:
            return self.__graf.get(uuid).artist
            
    def get_composer(self,uuid):
        """
        Retorna el compositor del vídeo associat a un UUID.
        """
        if uuid in self.__graf:
            return self.__graf.get(uuid).composer
            
    def get_genre(self,uuid):
        """
        Retorna el gènere del vídeo associat a un UUID.
        """
        if uuid in self.__graf:
            return self.__graf.get(uuid).genre

    def get_date(self,uuid):
        """
        Retorna la data del vídeo associat a un UUID.
        """
        if uuid in self.__graf:
            return self.__graf.get(uuid).date

    def get_comment(self,uuid):
        """
        Retorna el comentari del vídeo associat a un UUID.
        """
        if uuid in self.__graf:
            return self.__graf.get(uuid).comment

    def _get_uuids(self) -> list:
        """Retorna tots els UUIDs disponibles."""
        return list(self.__graf)

    def __repr__(self):
        """
        Retorna una representació formal de la classe VideoData.
        """
        return f"VideoData({len(self.__graf)} vídeos)"
    
    def __contains__(self, uuid):
        """
        Comprova si un UUID està en el graf.
        """
        return uuid in self.__graf

    def __iter__(self):
        """
        Permet la iteració sobre els vídeos.
        """
        return iter(self.__graf)

    def __eq__(self, other):
        """
        Comprova si dues instàncies de VideoData són iguals.
        """
        if not isinstance(other, VideoData):
            return NotImplemented
        return self.__graf == other.__graf
    
    def __hash__(self):
        """
        Retorna el hash de l'objecte VideoData.
        """
        return hash(tuple(self.__graf))
    
    def __ne__(self, other):
        """
        Comprova si dues instàncies de VideoData no són iguals.
        """
        return not self.__eq__(other)
    
    def __lt__(self, other):
        """
        Comprova si l'objecte actual és menor que un altre.
        """
        return len(self) < len(other)
    
    def read_playlist(self, obj_playlist: PlayList):
        """
        Llegeix una llista (de tipus Playlist) i actualitza el graf amb les connexions.
        """
        n_arestes = len(obj_playlist) - 1  # Obté el nombre d'arestes de la llista
        for i in range(n_arestes):  # Itera sobre les arestes
            uuid_1 = obj_playlist[i]  # Obté el primer UUID de la playlist
            uuid_2 = obj_playlist[i + 1]  # Obté el segon UUID de la playlist
            if uuid_1 in self.__graf and uuid_2 in self.__graf:  # Comprova si els UUIDs existeixen
                out_1 = list(self.__graf.edges_out(uuid_1))  # Llista les arestes sortints del primer UUID (com que és un iterador l'encapsulem en una llista)
                if uuid_2 in out_1: 
                    self.__graf.augmentaPes(uuid_1, uuid_2)  # Si ja existia aresta augmenta el seu pes
                else:
                    self.__graf.insert_edge(uuid_1, uuid_2)  # Si no hi ha aresta crea una nova aresta
    
    def get_video_rank(self, uuid: str) -> int:
        """
        Retorna el rang d'un vídeo associat a un UUID.
        """
        if uuid in self.__graf:
            return self.__graf.rank(uuid)
    
    def get_next_videos(self, uuid: str):
        """
        Retorna un iterador sobre els vídeos següents d'un node.
        """
        return iter(self.__graf.next_videos(uuid))
    
    def get_previous_videos(self,uuid: str):
        """
        Retorna un iterador sobre els vídeos anteriors d'un node.
        """
        return iter(self.__graf.previous_videos(uuid))
    
    def get_video_distance(self,uuid1:str,uuid2:str):
        """
        Retorna la distància entre dos vídeos.
        """
        if uuid1 in self.__graf and uuid2 in self.__graf:  # Comprova si els UUIDs existeixen
            if uuid1 != uuid2:  # Comprova que no siguin el mateix UUID
                cami = self.__graf.camiMesCurt(uuid1, uuid2)  # Obté el camí més curt
                if cami:  # Comprova si hi ha un camí
                    valor = 0  # Inicialitza el valor de la distància
                    for i in range(len(cami) - 1):  # Itera sobre el camí
                        valor += self.__graf.get_pes_aresta(cami[i], cami[i + 1])  # Suma els pesos de les arestes
                    return (len(cami) - 1, valor)  # Retorna la longitud del camí i el valor total
        return (0, 0)  # Retorna (0, 0) si no hi ha distància
            
            
            
            
            
            
            
            
            
            
            