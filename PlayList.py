
# CLASSE PLAYLIST


import VideoID
import uuid
import VideoPlayer
import cfg

class PlayList():
    """
    OBJECTIU: Guardar una llista de vídeos.
    
    RESPONSABILITAT: Crear una llista de vídeos i guardar els UUID d’aquests.
    També es poden reproduir els arxius que hi ha dins la llista.
    
    """

    def __init__(self):
        self.videos = []
        
        #enllaçar llistes
        self.next = None

    def load_file(self, file: str) -> None:
        f = open(file, 'r')
        
        for linia in f:
                
            if not linia.startswith("#") and linia.endswith(".mp4"):   # ignorar les linies
                uuid_video = VideoID.get_uuid(linia)
                    
                if uuid:
                    self.videos.append(uuid_video)


    def play(self) -> None:
        player = VideoPlayer()
        for video in self.videos:
            player.play_video(video, cfg.PLAY_MODE)
            
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
        
        
        