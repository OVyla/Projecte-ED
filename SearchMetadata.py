
from VideoData import VideoData
import cfg


class SearchMetadata:
    def __init__(self, videodata):
        self._videodata = videodata
        
        
    def search_by_attribute(self, attribute: str, sub: str) -> list:
        if not sub:
            print("ValueError: Valor de cerca necessari")
            return []
        if sub is None or not isinstance(sub, str):
            print("Valor invalid de cerca")
            return None
            
        if sub == "":
            print("Valor invalid de cerca")
            return None

            
        uuids = []
        for uuid in self._videodata._files:
            try:
                value = getattr(self._videodata, f"get_{attribute}")(uuid)
            except Exception as e:
                print(f"Error with UUID {uuid}: {e}")
            
            if value and sub.lower() in str(value).lower():
                uuids.append(uuid)
                
        return uuids
            

    def duration(self, min: int, max: int) -> None:
        
            
        if min<0 or max<0 or min>max:
            print("ValueError: Valors invalids")
            return None
        
        uuids = []
        
        for uuid in self._videodata._files:
            duration = self._videodata.get_duration(uuid)
            
            if min <= int(duration) and int(duration) <= max:
                uuids.append(uuid)
                
        return uuids

    def title(self, sub: str) -> list:
        return self.search_by_attribute("title", sub)

    def album(self, sub: str) -> list:
        return self.search_by_attribute("album", sub)

    def artist(self, sub: str) -> list:
        return self.search_by_attribute("artist", sub)

    def composer(self, sub: str) -> list:
        return self.search_by_attribute("composer", sub)

    def genre(self, sub: str) -> list:
        return self.search_by_attribute("genre", sub)

    def date(self, sub: str) -> list:
        return self.search_by_attribute("date", sub)

    def comment(self, sub: str) -> list:
        return self.search_by_attribute("comment", sub)
    
    def __str__(self):
        return str(self._videodata)
    

    
    # OPERADORS AND I OR
    
    def and_operator(self, list1: list, list2: list)  -> list:
        return list(set(list1) & set(list2))
    
                    
    def or_operator(self, list1: list, list2: list)  -> list:
        return list(set(list1) | set(list2))

"""
    

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

"""
