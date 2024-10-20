
# CLASSE PLAYLIST


from VideoID import VideoID
import uuid
from VideoPlayer import VideoPlayer
from VideoData import *
import cfg
import vlc

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


        

        #enllaçar llistes
        self.next = None

    def load_file(self, file: str) -> None:
        f = open(file, 'r')
        
        for linia in f:
                
            if not linia.startswith("#") and linia.endswith(".mp4"):   # ignorar les linies
                uuid_video = VideoID.get_uuid(linia)
                    
                if uuid:
                    self.videos.append(uuid_video)


    def play(self, videodata, video_id) -> None:
        for video in self.videos:
            player = VideoPlayer(videodata, video_id)
            player.play_video(str(video), cfg.PLAY_MODE)
            
        # playlist enllaçada
        if self.next is not None:
            self.next.play()
        

    def add_video_at_end(self, uuid: str) -> None:
        self.videos.append(uuid)

    def remove_first_video(self) -> None:
        self.videos.pop(0)

    def remove_last_video(self) -> None:
        self.videos.pop(-1)
    
    
    # enllaçar llistes
    def next(self, playlist):
        self.next = playlist
        


def main():
    # Crear una instancia de PlayList
    playlist = PlayList()
    
    print("Generant UUIDs...")
    video1_path = "/Users/clara/Documentos/2º GED/ED/projecte/corpus/Beyond/2575_galaxy_Space_Milky_Way_GalaxyWithCustomization720p5000br.mp4"
    video2_path = "/Users/clara/Documentos/2º GED/ED/projecte/videos/Doraemon Opening 1 (Català) (360p).mp4"
   
    video_id = VideoID()
    # Generar UUIDs
    uuid1 = video_id.generate_uuid(video1_path)
    uuid2 = video_id.generate_uuid(video2_path)

    video_data = VideoData()

    # metadades
    video_data.add_video(uuid1, video1_path)
    video_data.add_video(uuid2, video2_path)

    # Afegir UUIDs a la playlist
    print("Afegint videos a la playlist...")
    playlist.add_video_at_end(uuid1)
    playlist.add_video_at_end(uuid2)

    # Reproducció
    print("Reproduint videos...")
    playlist.play(video_data, video_id)

    print("Final!")

main()

