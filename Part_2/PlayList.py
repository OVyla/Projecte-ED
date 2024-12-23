import VideoID 
import VideoPlayer 
import VideoData 
import cfg
import vlc
import os
from pathlib import Path

class PlayList:
    
    #__slots__ = ['_v_id', '_v_player']

    def __init__(self, VideoID, VideoPlayer):
        self._v_id = VideoID
        self._v_data = VideoPlayer._video_data
        self._v_player = VideoPlayer

        self.videos = []   # uuids dels videos
        
        #enllaçar llistes
        self._next = None
            
                            
    def load_file(self, file: str) -> None:
        """Guarda els uuids dels videos continguts en l'arxiu M3U"""
        if not isinstance(file, str) or file.strip() == "":
            print(f"Arxiu no vàlid: {file}")
            return
        
        if not os.path.exists(file):
            raise FileNotFoundError(f"L'arxiu {file} no existeix.")
        
        try:
            with open(file, 'r', encoding="utf-8") as f:
                for linia in f:
                    if not linia.startswith("#") and not linia.startswith("http://") and linia.endswith(".mp4"):
                        path = Path(linia)
                        if not self._v_id.get_uuid(path):
                            self._v_id.generate_uuid(path)
                        
                        uuid = self._v_id.get_uuid(path)
                        self._v_data.add_video(uuid, path)
                        self._v_data.load_metadata(uuid)
                        self.videos.append(uuid)

                            
        except Exception as error:
            print(f"Error en carregar l'arxiu {file}: {error}")


    def play(self, mode=1) -> None:
        """Reprodueix tots els videos de la llista i els de la llista enllaçada"""
        if len(self.videos) == 0:
            print("Llista buida")

        else:
            for video in self.videos:
                try:
                    self._v_player.play_video(video, mode)
                except Exception:
                    print("ERROR en la reproduccio del video")
                    continue
                
        # playlist enllaçada
        if self._next:
            self.get_next_playlist.play(mode)


    def add_video_at_end(self, uuid: str) -> None:
        """Afegeix video al final de la llista"""
        if uuid in self._v_data._files:
            self.videos.append(str(uuid))
        else:    
            print("ERROR: uuid no trobat")
            

    def remove_first_video(self) -> None:
        """Elimina el primer vídeo de la llista."""
        if self.videos:
            self.videos.pop(0)
        else:
            print("ERROR: No hi ha vídeos a eliminar.")


    def remove_last_video(self) -> None:
        """Elimina ultim vídeo de la llista"""
        if self.videos:
            self.videos.pop(-1)
        else:
            print("ERROR: No hi ha vídeos a eliminar.")


    def next_playlist(self, playlist):
        if isinstance(playlist, PlayList):
            self._next = playlist
        
    def get_next_playlist(self):
        return self._next

    def __len__(self):
        return len(self.videos)
        
    def __str__(self):
        """Representació de la playlist"""
        if not self.videos:
            return "Playlist buida"
        
        result = "Playlist:\n"
        for i, video in enumerate(self.videos):
            result += f"{i + 1}. {video}\n"
        return result 

    def __repr__(self):
        return f"PlayList({len(self.videos)} videos)"

    def __iter__(self):
        return iter(self.videos)

    def __eq__(self, other):
        if not isinstance(other, PlayList):
            return NotImplemented
        return self.videos == other.videos

    def __hash__(self):
        return hash(tuple(self.videos))
    
    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return len(self.videos) < len(other.videos)
    
    def read_list(self, p_llista: list):
        pass