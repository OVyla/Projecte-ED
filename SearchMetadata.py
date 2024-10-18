
import VideoData


class SearchMetadata:
    """
    OBJECTIU: Realitzar cerques que generen llistes de vídeos.
    
    RESPONSABILITAT: Consulta les metadades dins la col·lecció de vídeos
    i proporciona funcions per a manipular llistes d’arxius de vídeo.
    
    """
    
    def __init__(self, videodata):
        self.videodata = videodata   # objecte VideoData

    def duration(self, min: int, max: int) -> None:
        uuids = []
        
        for uuid in self.videodata.keys():
            duration = self.video_data.get_duration(uuid)
            
            if min <= duration and duration <= max:
                uuids.append(uuid)
                
        return uuids
    

    def title(self, sub: str) -> list:
        uuids = []
        
        for uuid in self.videodata.keys():
            title = self.video_data.get_title(uuid)
            
            if sub.lower() in title.lower():
                uuids.append(uuid)
                
        return uuids
    

    def album(self, sub: str) -> list:
        uuids = []
        
        for uuid in self.videodata.keys():
            album = self.video_data.get_album(uuid)
            
            if sub.lower() in album.lower():
                uuids.append(uuid)
                
        return uuids
    

    def artist(self, sub: str) -> list:
        uuids = []
        
        for uuid in self.videodata.keys():
            artist = self.video_data.get_artist(uuid)
            
            if sub.lower() in artist.lower():
                uuids.append(uuid)
                
        return uuids


    def composer(self, sub: str) -> list:
        uuids = []
        
        for uuid in self.videodata.keys():
            composer = self.video_data.get_composer(uuid)
            
            if sub.lower() in composer.lower():
                uuids.append(uuid)
                
        return uuids
    

    def genre(self, sub: str) -> list:
        uuids = []
        
        for uuid in self.videodata.keys():
            genre = self.video_data.get_genre(uuid)
            
            if sub.lower() in genre.lower():
                uuids.append(uuid)
                
        return uuids
    

    def date(self, sub: str) -> list:
        uuids = []
        
        for uuid in self.videodata.keys():
            date = self.video_data.get_date(uuid)
            
            if sub.lower() in date.lower():
                uuids.append(uuid)
                
        return uuids
    

    def comment(self, sub: str) -> list:
        uuids = []
        
        for uuid in self.videodata.keys():
            comment = self.video_data.get_comment(uuid)
            
            if sub.lower() in comment.lower():
                uuids.append(uuid)
                
        return uuids
    
    
    # OPERADORS AND I OR
    
    def and_operator(self, list1: list, list2: list)  -> list:
        return list(set(list1) and set(list2))
    
                    
    def or_operator(self, list1: list, list2: list)  -> list:
        return list(set(list1) or set(list2))
    
    
