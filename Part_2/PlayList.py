import VideoID 
import VideoPlayer 
import VideoData 
import cfg
import vlc
import os
from pathlib import Path

class PlayList:
    """
    OBJECTIU: Gestionar una llista de reproducció de vídeos.
    RESPONSABILITAT: Proporcionar funcionalitats per carregar, reproduir i gestionar vídeos en una llista.
    """
    __slots__ = ['__v_id','__v_player','__videos']

    def __init__(self, *args):
        """
        Inicialitza la classe PlayList.
        """
        if len(args) != 2 or not isinstance(args[0], VideoID.VideoID) or not isinstance(args[1], VideoPlayer.VideoPlayer):
            raise NotImplementedError
        self.__v_id = args[0]
        self.__v_player = args[1]
        self.__videos = []
        
    def load_file(self, file:str):
        """
        Carrega una llista de vídeos des d'un fitxer M3U.
        """
        self.__videos = []  # Reinicialitza la llista de vídeos
        
        if not file.endswith(".m3u"):  # Comprova si el fitxer és un M3U
            return
        
        try:    
            with open(file, "r", encoding='utf-8', errors='ignore') as fitxer:  # Obre el fitxer
                for linia in fitxer:  # Itera sobre cada línia del fitxer
                    linia = linia.strip()
                    if linia and not linia.startswith("#") and linia.endswith(".mp4"):  # Comprova si la línia és vàlida
                        uuid = self.__v_id.get_uuid(linia)  # Obté l'UUID associat al fitxer
                        
                        if uuid and uuid not in self.__videos:  # Comprova si l'UUID és vàlid i no està duplicat
                            if uuid in self.__v_player:  # Comprova si el vídeo està en el reproductor
                                self.__videos.append(uuid)  # Afegeix l'UUID a la llista de vídeos
        except:
            raise FileNotFoundError
            
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


    def remove_last_video(self) -> None:
        """Elimina ultim vídeo de la llista"""
        if self.__videos:
            self.__videos.pop()
    
    def __getitem__(self, index:int) -> str:
        """
        Retorna el vídeo a la posició especificada.
        """
        return self.__videos[index]
        
    def __len__(self):
        """
        Retorna el nombre de vídeos a la llista.
        """
        return len(self.__videos)
        
    def __str__(self):
        """
        Retorna una representació en cadena de la classe PlayList.
        """
        return f"PlayList({len(self.__videos)} videos)"

    def __repr__(self):
        """
        Retorna una representació formal de la classe PlayList.
        """
        return f"PlayList({len(self.__videos)} videos)"

    def __iter__(self):
        """
        Permet la iteració sobre els vídeos de la llista.
        """
        for uuid in self.__videos:
            yield uuid
    
    def read_list(self, p_llista: list):
        """
        Llegeix una llista de python amb vídeos i els afegeix a PlayList.
        """
        if p_llista:
            self.__videos = []  # Reinicialitza la llista de vídeos
            for uuid in p_llista:
                if uuid and not uuid in self.__videos:  # Comprova si l'UUID és vàlid i no està duplicat
                    self.add_video_at_end(uuid)  # Afegeix l'UUID al final de la llista
        
        
        
        
        