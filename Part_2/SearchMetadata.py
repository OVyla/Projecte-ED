import VideoData
import cfg
import heapq
import ElementData

class SearchMetadata:
    """
    OBJECTIU: Proporcionar funcionalitats per cercar metadades de vídeos i crear llistes de python amb identificadors de videos.
    RESPONSABILITAT: Permetre la cerca de vídeos per atributs específics i gestionar operacions de cerca.
    """

    __slots__ = ['__videodata']
    
    def __init__(self, *args):
        """
        Inicialitza la classe SearchMetadata.
        """
        if len(args) != 1 or not isinstance(args[0], VideoData.VideoData):
            raise NotImplementedError
        self.__videodata = args[0]
        
    def search_by_attribute(self, attribute: str, sub: str) -> list:
        """
        Cerca vídeos per un atribut específic i un substring.
        """
        if not isinstance(sub, str):
            return []
        if sub == "":
            return self.__videodata._get_uuids()
        uuids = []   # Inicialitza la llista que retornarem
        for uuid in self.__videodata._get_uuids():  # Itera sobre cada UUID
            try:
                method = getattr(self.__videodata, f"get_{attribute}", None)  # Obté el mètode corresponent a l'atribut
                if method is None or not callable(method):  # Comprova si el mètode és vàlid
                    print(f"L'atribut '{attribute}' no es pot cridar.")  # Missatge d'error
                    return []  # Retorna una llista buida

                value = method(uuid)  # Obté el valor de l'atribut
                if sub.lower() in str(value).lower():  # Comprova si el substring està en el valor
                    if uuid not in uuids:  # Comprova si l'UUID no està duplicat
                        uuids.append(uuid)  # Afegeix l'UUID a la llista de resultats
            except Exception:
                print(f"Error amb UUID {uuid}")  # Missatge d'error si hi ha un problema amb l'UUID
        return uuids  # Retorna la llista d'UUIDs trobats
    
    def duration(self, min: int, max: int) -> list:
        """
        Cerca vídeos per durada dins d'un rang especificat.
        """
        if not isinstance(min, int) or not isinstance(max, int):
            return []
        if min < -1 or max < -1 or min > max:
            return []

        uuids = []  # Inicialitza la llista que retornaerm
        for uuid in self.__videodata._get_uuids():  # Itera sobre cada UUID
            duration = self.__videodata.get_duration(uuid)  # Obté la durada del vídeo
            if duration is not "" and min <= duration <= max:  # Comprova si la durada està dins del rang
                if uuid not in uuids:  # Comprova si l'UUID no està duplicat
                    uuids.append(uuid)  # Afegeix l'UUID a la llista de resultats
        return uuids  # Retorna la llista d'UUIDs trobats
        
    def genre(self, sub="") -> list:
        """
        Cerca vídeos per gènere.
        """
        return self.search_by_attribute("genre", sub)

    def title(self, sub="") -> list:
        """
        Cerca vídeos per títol.
        """
        return self.search_by_attribute("title", sub)

    def album(self, sub="") -> list:
        """
        Cerca vídeos per àlbum.
        """
        return self.search_by_attribute("album", sub)

    def artist(self, sub="") -> list:
        """
        Cerca vídeos per artista.
        """
        return self.search_by_attribute("artist", sub)

    def composer(self, sub="") -> list:
        """
        Cerca vídeos per compositor.
        """
        return self.search_by_attribute("composer", sub)

    def date(self, sub="") -> list:
        """
        Cerca vídeos per data.
        """
        return self.search_by_attribute("date", sub)

    def comment(self, sub="") -> list:
        """
        Cerca vídeos per comentari.
        """
        return self.search_by_attribute("comment", sub)
    
    def and_operator(self, list1: list, list2: list) -> list:
        """
        Retorna la intersecció de dues llistes.
        """
        return list(set(list1) & set(list2))

    def or_operator(self, list1: list, list2: list) -> list:
        """
        Retorna la unió de dues llistes.
        """
        return list(set(list1) | set(list2))

    def __str__(self):
        """
        Retorna una representació en cadena de la classe SearchMetadata.
        """
        return f"SearchMetadata(videodata={repr(self.__videodata)})"

    def __repr__(self):
        """
        Retorna una representació formal de la classe SearchMetadata.
        """
        return f"SearchMetadata(videodata={repr(self.__videodata)})"
    
    def get_similar(self, A: str, max_list: int = 25) -> list:
        """
        Retorna una llista de vídeos similars a un vídeo donat.
        """
        if max_list > 25: # Limita el nombre màxim de resultats
            max_list = 25
        semblances = {} # Diccionari per emmagatzemar semblances: uuid: semblança
        
        if not isinstance(A,str):
            return []
       
        for B in self.__videodata:
            AB_nodes, AB_value = self.__videodata.get_video_distance(A,B) # Obté la distància entre A i B
            BA_nodes, BA_value = self.__videodata.get_video_distance(B,A) # Obté la distància entre B i A
            
            AB = 0  # Inicialitza la semblança
            BA = 0
            
            if (AB_nodes != 0): # Comprova si hi ha nodes
                AB = (AB_value / AB_nodes) * (self.__videodata.get_video_rank(A) / 2)  # Calcula la semblança
            if (BA_nodes != 0):
                BA = (BA_value / BA_nodes) * (self.__videodata.get_video_rank(B) / 2)
            semblances[B] = AB + BA # Assigna la semblança al diccionari
            
        
        uuids_ordenats = sorted(semblances.items(), key=lambda item: (-item[1], item[0])) # Ordena les semblances en ordre decreixent, 
                                                                                          # i si coincideixen semblançes ordena per identificador 
                                                                                          # més petit
        ll = [uuid for uuid, _ in uuids_ordenats[:max_list]] # Obté els UUIDs dels vídeos similars
        return ll
    
    def get_auto_play(self, N: int = 25) -> list:
        """
        Retorna una llista de vídeos per reproduir automàticament.
        """
        if not isinstance(N, int):
            return []
        
        if N > 25 or N > len(self.__videodata):  # Limita el nombre de vídeos a 25 (o al maxim de videos carregats)
            if len(self.__videodata) < 25:
                N = len(self.__videodata)
            else:
                N = 25
        ranks = {}  # Diccionari per emmagatzemar els rànquings: uuid: rank 
        for uuid in self.__videodata:  # Itera sobre cada vídeo
            ranks[uuid] = self.__videodata.get_video_rank(uuid) # Assigna el rànquing al diccionari
        
        ranks_ordenats = sorted(ranks.items(), key=lambda item: (-item[1], item[0])) # Ordena els ranks

        auto_play_list = [uuid for uuid, _ in ranks_ordenats[:N]]# Obté la llista de vídeos per reproduir automàticament

        simil_list = {}  # Diccionari per emmagatzemar vídeos similars: uuid: [similar_uuids]
        for uuid in auto_play_list: # Itera sobre cada vídeo de la llista de reproducció automàtica
            simil_list[uuid] = self.get_similar(uuid, N // 2) # Obté vídeos similars

        total_simil_25_set = set(auto_play_list)  # Conjunt per emmagatzemar vídeos similars
        for similar_videos in simil_list.values():  # Itera sobre els vídeos similars
            total_simil_25_set.update(similar_videos)    # Afegeix els vídeos similars al conjunt
            
        total_simil_25_list = sorted(
            total_simil_25_set,
            key=lambda uuid: (-self.__videodata.get_video_rank(uuid), uuid)
        )[:25]  # Ordena i limita la llista de vídeos similars

        idv_semblanca = {uuid: 0 for uuid in total_simil_25_list}  # Diccionari per emmagatzemar semblances
        for i in total_simil_25_list:  # Itera sobre cada vídeo
            for j in total_simil_25_list:  # Itera sobre cada vídeo per calcular semblances
                if i != j:
                    idv_semblanca[i] += self.get_semblanca(i, j)  # Afegeix la semblança

        ordered_simil = sorted(
            idv_semblanca.items(),
            key=lambda item: (-item[1], item[0])
        ) # Ordena les semblances

        result = [uuid for uuid, _ in ordered_simil[:N]] # Obté els vídeos ordenats per semblança

        result.extend([None] * (N - len(result))) # Completa la llista amb None si és necessari
        
        return result
        
                
            