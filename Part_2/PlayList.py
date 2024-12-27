import VideoID 
import VideoPlayer 
import VideoData 
import cfg
import vlc
import os
from pathlib import Path


class PlayList:
    
    __slots__ = ['_v_id', '_v_player', '_videos', '_next']

    def __init__(self, *args):
        if len(args) != 2 or not isinstance(args[0], VideoID.VideoID) or not isinstance(args[1], VideoPlayer.VideoPlayer):
            raise NotImplementedError
        self._v_id = args[0]
        self._v_player = args[1]

        self._videos = []   # uuids dels videos
        
        #enllaçar llistes
        self._next = None
    
                            
    def load_file(self, file: str) -> None:
        """Guarda els uuids dels videos continguts en l'arxiu M3U"""
        if not isinstance(file, str) or file.strip() == "":
            print(f"Arxiu no vàlid: {file}")
            return
        
        if not os.path.exists(file):
            raise FileNotFoundError(f"L'arxiu {file} no existeix.")
        self._videos = []
        
        try:
            with open(file, 'r', encoding="utf-8") as f:
                for linia in f:
                    linia = linia.strip()
                    if not linia.startswith("#") and linia.endswith(".mp4"):
                        if linia.startswith("file://"):
                            linia = linia[7:]
                        path = str(Path(linia))
                        root = os.getcwd()
                        if not path.startswith(root):
                            path = root +'/'+ path
                        uuid = self._v_id.get_uuid(path)
                        if not uuid:
                            uuid = self._v_id.generate_uuid(linia)
                        if uuid not in self._videos:
                            self._videos.append(uuid)
        except Exception as error:
            print(f"Error en carregar l'arxiu {file}: {error}")

    def load_file_1(self, file: str) -> None:
        """Guarda els uuids dels videos continguts en l'arxiu o directori M3U"""
        if not isinstance(file, str) or file.strip() == "":
            print(f"Arxiu no vàlid: {file}")
            return
        
        path = Path(file)
    
        if not path.exists():
            raise FileNotFoundError(f"L'arxiu o directori {file} no existeix.")
        
        # If it's a single M3U file
        if path.is_file() and path.suffix == '.m3u':
            self._load_m3u_file(path)
        
        # If it's a directory containing M3U files
        elif path.is_dir():
            previous_playlist = self
            for m3u_file in sorted(path.glob("*.m3u")):  # Sorted to ensure consistent order
                new_playlist = PlayList(self._v_id, self._v_player)
                new_playlist._load_m3u_file(m3u_file)
                previous_playlist.next = new_playlist
                previous_playlist = new_playlist
        else:
            print(f"ERROR: {file} no és ni un fitxer .m3u ni un directori.")

    def _load_m3u_file(self, path: Path) -> None:
        """Processa un fitxer M3U per carregar els vídeos"""
        self._videos = []
        try:
            with path.open('r', encoding="utf-8") as f:
                for linia in f:
                    linia = linia.strip()
                    if not linia.startswith("#") and linia.endswith(".mp4"):
                        if linia.startswith("file://"):
                            linia = linia[7:]
                        full_path = str(Path(linia).resolve())
                        uuid = self._v_id.get_uuid(full_path)
                        if not uuid:
                            uuid = self._v_id.generate_uuid(full_path)
                        self._videos.append(uuid)
        except Exception as error:
            print(f"Error en carregar l'arxiu {path}: {error}")
    
        
    def play(self, mode=1) -> None:
        """Reprodueix tots els videos de la llista i els de la llista enllaçada"""
        if len(self._videos) == 0:
            print("Llista buida")
        else:
            for video in self._videos:
                try:
                    self._v_player.play_video(video, mode)
                except Exception:
                    print("ERROR en la reproduccio del video")
                    continue

    def add_video_at_end(self, uuid: str) -> None:
        """Afegeix video al final de la llista"""
        if uuid in self._v_player:
            self._videos.append(str(uuid))
        else:    
            print("ERROR: uuid no trobat")
            

    def remove_first_video(self) -> None:
        """Elimina el primer vídeo de la llista."""
        if self._videos:
            self._videos.pop(0)
        else:
            print("ERROR: No hi ha vídeos a eliminar.")


    def remove_last_video(self) -> None:
        """Elimina ultim vídeo de la llista"""
        if self._videos:
            self._videos.pop(-1)
        else:
            print("ERROR: No hi ha vídeos a eliminar.")


    def next_playlist(self, playlist):
        if isinstance(playlist, PlayList):
            self._next = playlist
        
    @property
    def next(self):
        return self._next
    
    @next.setter
    def next(self, value):
        self._next = value

    def __len__(self):
        return len(self._videos)
        
    def __str__(self):
        """Representació de la playlist"""
        if not self._videos:
            return []
        
        return self._videos 

    def __repr__(self):
        return f"PlayList({len(self._videos)} videos)"

    def __iter__(self):
        return iter(self._videos)
    
    def __getitem__(self, num:int) -> str:
        return self._videos[num]
        
    def __eq__(self, other):
        if not isinstance(other, PlayList):
            return NotImplemented
        return self._videos == other._videos

    def __hash__(self):
        return hash(tuple(self._videos))
    
    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return len(self._videos) < len(other._videos)
    
    def read_list(self, p_llista: list):
        pass