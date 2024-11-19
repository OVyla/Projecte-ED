import VideoID 
import VideoFiles 
import uuid
import VideoPlayer 
import VideoData 
import cfg
import vlc
import os

class PlayList:

    def __init__(self, VideoID, VideoPlayer):

        self._v_id = VideoID
        self._v_data = VideoPlayer._video_data
        self._v_player = VideoPlayer
        
        self.videos = []
        
        #enllaçar llistes
        self._next = None
            

    def load_file(self, file: str) -> None:
        if not isinstance(file,str):
            print(f"arxiu {file} no és correcte")
            
        elif file == "":
            print("Arxiu no valid")
        
        elif not os.path.exists(file):
            raise FileNotFoundError(f"El archivo {file} no existe.")
        
        else:
            with open(file, 'r') as f:
                for line in f:
                    if not line.startswith("#") and line.strip().endswith(".mp4"):  # Ignorar comentarios
                        try:
                            path = cfg.get_canonical_pathfile(line)
                            if not self._v_id.get_uuid(path):
                                self._v_id.generate_uuid(path)
                                uuid = self._v_id.get_uuid(path)
                                if uuid not in self.videos:
                                    self._v_data.add_video(uuid, path)
                                    self._v_data.load_metadata(uuid)
                                    self.videos.append(uuid)
                        
                        except Exception as e:
                            print(f"Error amb el arxiu {line}: {e}")
        

    def load_file2(self, file: str) -> None:
        if not isinstance(file,str):
            print(f"arxiu {file} no és correcte")
            
        elif file == "":
            print("Arxiu no valid")
            
        elif not os.path.exists(file):
            raise FileNotFoundError(f"arxiu {file} no existeix")
        
        else:   
            with open(file, 'r') as f:
                
                for linia in f:
                    
                    if not linia.startswith("#") and linia.endswith(".mp4"):   # saltar linies que son comentaris
                        try:
                            self._v_id.generate_uuid(linia)
                            uuid_video = self._v_id.get_uuid(linia)
                            
                            if uuid_video and uuid_video not in self.videos:
                                self._v_data.add_video(uuid_video, linia)
                                self._v_data.load_metadata(uuid_video)
                                self._v_files.reload_fs(self._root)
                                self.add_video_at_end(uuid_video)
    
                        except Exception as e:
                            print(f"Error al llegir l'arxiu {file}: {e}")
                        

    def play(self, mode=1) -> None:
        if len(self.videos) == 0:
            print("Llista buida")
            
        elif not isinstance(mode, int):
            print("mode incorrcecte")
            
        else:
            for video in self.videos:
                try:
                    self._v_player.play_video(video, mode)
                except Exception:
                    print("ERROR en la reproduccio del video,")
                    continue
                
            # playlist enllaçada
            if self._next:
                self.get_next_playlist.play(mode)


    def add_video_at_end(self, uuid: str) -> None:
        if not isinstance(uuid, str):
            print("uuid no valid")
            
        elif uuid in self._v_data._files:
            self.videos.append(uuid)
        else:    
            print("ERROR: uuid no trobat")


    def remove_first_video(self) -> None:
        """Elimina el primer vídeo de la llista."""
        if self.videos:
            self.videos.pop(0)
        else:
            print("ERROR: No hi ha vídeos a eliminar.")


    def remove_last_video(self) -> None:
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
                    
                if uuid_video:
                    self.videos.append(uuid_video)
"""
