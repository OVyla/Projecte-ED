
# CLASSE PLAYLIST

from VideoID import VideoID
from VideoFIles import VideoFiles
import uuid
from VideoPlayer import VideoPlayer
from VideoData import *
import cfg
import vlc
import os

class PlayList():
    """
    OBJECTIU: Guardar una llista de vídeos.
    
    RESPONSABILITAT: Crear una llista de vídeos i guardar els UUID d’aquests.
    També es poden reproduir els arxius que hi ha dins la llista.
    
    """

    def __init__(self, videos=None):
        if videos is None:
            self.videos = []
        else:
            self.videos = videos

        self._root = cfg.get_root()
    
        self._v_files = VideoFiles(self._root)
        self._v_id = VideoID()
        self._v_data = VideoData()
    
        videos_afegits = self._v_files.files_added()
        for path in videos_afegits:
            self._v_id.generate_uuid(path)
            uuid = self._v_id.get_uuid(path)
            self._v_data.add_video(uuid, path)
            self._v_data.load_metadata(uuid)
        self._v_files.reload_fs(self._root)
    
        self._v_player = VideoPlayer(self._v_data, self._v_id)
                
        #enllaçar llistes
        self._next = None

    def load_file(self, file: str) -> None:
        f = open(file, 'r')
        
        for linia in f:
                
            if not linia.startswith("#") and linia.endswith(".mp4"):   # saltar linies que son comentaris
                self._v_id.generate_uuid(linia)
                uuid_video = self._v_id.get_uuid(linia)
                self._v_data.add_video(uuid_video, linia)
                self._v_data.load_metadata(uuid_video)
                self._v_files.reload_fs(self._root)
                    
                if uuid_video:
                    self.videos.append(uuid_video)


    def play(self) -> None:
        for video in self.videos:
            self._v_player.play_video(video, cfg.PLAY_MODE)
            
        # playlist enllaçada
        if self._next is not None:
            self._next.play()
        

    def add_video_at_end(self, uuid: str) -> None:
        self.videos.append(uuid)

    def remove_first_video(self) -> None:
        self.videos.pop(0)

    def remove_last_video(self) -> None:
        self.videos.pop(-1)
    
    # enllaçar llistes
    def next_playlist(self, playlist):
        self._next = playlist
        


def main():
    # Crear una instancia de PlayList
    print("Creant playlist...")
    playlist = PlayList()
    print("Load_file...")
    #playlist.load_file("/Users/clara/Documentos/2º GED/ED/projecte/#EXTM3U.txt")
    
    root = cfg.get_root()

    v_files = VideoFiles(root)
    v_id = VideoID()
    v_data = VideoData()
    
    
    videos_afegits = v_files.files_added()
    for path in videos_afegits:
        v_id.generate_uuid(path)
        uuid = v_id.get_uuid(path)
        v_data.add_video(uuid, path)
        v_data.load_metadata(uuid)
    v_files.reload_fs(root)
    
    print("Afegint videos a la playlist...")
    uuid = v_id.get_uuid('/Users/clara/Documentos/2º GED/ED/projecte/corpus/Big data/_Cyberpunk55.mp4')
    playlist.add_video_at_end(uuid)
    uuid2 = v_id.get_uuid('/Users/clara/Documentos/2º GED/ED/projecte/corpus/Big data/579180_matrix_computer_cyber_DataStardustBinaryLoop4K720p5000br.mp4')
    playlist.add_video_at_end(uuid2)


    # Reproducció
    print("Reproduint videos...")
    playlist.play()

    print("Enllaçant amb una segona playlist...")
    p = PlayList([uuid, uuid2])
    playlist.next_playlist(p)

    print("Reproduint amb l'enllaç...")
    playlist.play()

    print("Final!")

if __name__ == "__main__":
    main()
        
