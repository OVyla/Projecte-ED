import VideoID 
import VideoPlayer 
import VideoData 
import cfg
import vlc
import os
from pathlib import Path

class PlayList:
    
    __slots__ = ['__v_id','__v_player','__videos']

    def __init__(self, *args):
        if len(args) != 2 or not isinstance(args[0], VideoID.VideoID) or not isinstance(args[1], VideoPlayer.VideoPlayer):
            raise NotImplementedError
        self.__v_id = args[0]
        self.__v_player = args[1]
        self.__videos = []
    
    def load_file(self, file:str):
        self.__videos = []
        
        if not file.endswith(".m3u"):
            return
        
        try:    
            with open(file, "r", encoding='utf-8', errors = 'ignore') as fitxer:
                for linia in fitxer:
                    linia = linia.strip()
                    if linia and not linia.startswith("#") and linia.endswith(".mp4"):
                        uuid = self.__v_id.get_uuid(linia)
                        if uuid and uuid not in self.__videos:
                            self.__videos.append(uuid)
        except:
            raise FileNotFoundError
        #return self.__videos

    def play(self, mode=1) -> None:
        """Reprodueix tots els videos de la llista"""
        for uuid in self.__videos:
            try:
                self.__v_player.play_video(uuid, mode)
            except Exception:
                print("ERROR en la reproduccio del video")
                continue

    def add_video_at_end(self, uuid: str) -> None:
        """Afegeix video al final de la llista"""
        self.__videos.append(uuid)
            
    def remove_first_video(self) -> None:
        """Elimina el primer vídeo de la llista."""
        if self.__videos:
            self.__videos.pop(0)
        #else:
         #   print("ERROR: No hi ha vídeos a eliminar.")


    def remove_last_video(self) -> None:
        """Elimina ultim vídeo de la llista"""
        if self.__videos:
            self.__videos.pop()
        #else:
         #   print("ERROR: No hi ha vídeos a eliminar.")
        
    def __contains__(self, uuid):
        return uuid in self.__videos
        
    def __len__(self):
        return len(self.__videos)
        
    def __str__(self):
        """Representació de la playlist"""
        if not self.__videos:
            return str([])
        return str(self.__videos)

    def __repr__(self):
        return f"PlayList({len(self.__videos)} videos)"

    def __iter__(self):
        for uuid in self.__videos:
            yield uuid
    
    def __getitem__(self, num:int) -> str:
        return self.__videos[num]
        
    def __eq__(self, other):
        if not isinstance(other, PlayList):
            return NotImplemented
        return self._videos == other.__videos

    def __hash__(self):
        return hash(tuple(self.__videos))
    
    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return len(self.__videos) < len(other.__videos)
    
    def read_list(self, p_llista: list):
        if p_llista:
            self.__videos = []
            for uuid in p_llista:
                if uuid and not uuid in self.__videos:
                    self.add_video_at_end(uuid)