
from VideoData import VideoData


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
        
        for uuid in self.videodata._files:
            duration = self.videodata.get_duration(uuid)
            
            if min <= int(duration) and int(duration) <= max:
                uuids.append(uuid)
                
        return uuids
    

    def title(self, sub: str) -> list:
        uuids = []
        
        for uuid in self.videodata._files:
            title = self.videodata.get_title(uuid)

            if title and sub.lower() in str(title).lower():   # comprobem també que existeix un titol
                uuids.append(uuid)
                
        return uuids
    

    def album(self, sub: str) -> list:
        uuids = []
        
        for uuid in self.videodata._files:
            album = self.videodata.get_album(uuid)
            
            if album and sub.lower() in album.lower():
                uuids.append(uuid)
                
        return uuids
    

    def artist(self, sub: str) -> list:
        uuids = []
        
        for uuid in self.videodata._files:
            artist = self.videodata.get_artist(uuid)
            
            if artist and sub.lower() in str(artist).lower():
                uuids.append(uuid)
                
        return uuids


    def composer(self, sub: str) -> list:
        uuids = []
        
        for uuid in self.videodata._files:
            composer = self.videodata.get_composer(uuid)
            
            if composer and sub.lower() in composer.lower():
                uuids.append(uuid)
                
        return uuids
    

    def genre(self, sub: str) -> list:
        uuids = []
        
        for uuid in self.videodata._files:
            genre = self.videodata.get_genre(uuid)
            
            if genre and sub.lower() in genre.lower():
                uuids.append(uuid)
                
        return uuids
    

    def date(self, sub: str) -> list:
        uuids = []
        
        for uuid in self.videodata._files:
            date = self.videodata.get_date(uuid)
            
            if date and sub.lower() in str(date).lower():
                uuids.append(uuid)
                
        return uuids
    

    def comment(self, sub: str) -> list:
        uuids = []
        
        for uuid in self.videodata._files:
            comment = self.videodata.get_comment(uuid)
            
            if comment and sub.lower() in comment.lower():
                uuids.append(uuid)
                
        return uuids
    
    
    # OPERADORS AND I OR
    
    def and_operator(self, list1: list, list2: list)  -> list:
        return list(set(list1) and set(list2))
    
                    
    def or_operator(self, list1: list, list2: list)  -> list:
        return list(set(list1) or set(list2))
    
    

def main():

    # Classe VideData 
    vd = VideoData()
    uuid = '5f665e9e-16ea-5e5f-9d93-91c802c81618'
    
    # Afegir el vídeo
    print('Afegint video...')
    vd.add_video(uuid, '/Users/clara/Documentos/2º GED/ED/projecte/corpus/Beyond/2575_galaxy_Space_Milky_Way_GalaxyWithCustomization720p5000br.mp4')
    # Carregar les metadades
    print('\nCarregant metadades del video...')
    vd.load_metadata(uuid)

    s = SearchMetadata(vd)
    # searcmetadata
    print("Provant SearchMetadata:")
    print("duracio: ", s.duration(0, 10))
    print("title: ", s.title("il"))
    print("date:", s.date("5"))

main()

