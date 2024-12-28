import VideoData
import cfg
import heapq

class SearchMetadata:

    __slots__ = ['__videodata']
    
    def __init__(self, *args):
        if len(args) != 1 or not isinstance(args[0], VideoData.VideoData):
            raise NotImplementedError
        self.__videodata = args[0]
        
    def search_by_attribute(self, attribute: str, sub: str) -> list:
        uuids = []
        if not isinstance(sub, str):
            return []
        
        for uuid in self.__videodata._get_uuids():
            try:
                method = getattr(self.__videodata, f"get_{attribute}", None)
                if method is None:
                    print(f"L'atribut '{attribute}' no es pot cridar.")
                    return []

                value = method(uuid)
                if sub.lower() in str(value).lower():
                    if uuid not in uuids:
                        uuids.append(uuid)
            except Exception:
                print(f"Error amb UUID {uuid}")
        return uuids

    def duration(self, min: int, max: int) -> list:
        if not isinstance(min, int) or not isinstance(max, int):
            return []
        if min < -1 or max < -1 or min > max:
            return []

        uuids = []
        for uuid in self.__videodata._get_uuids():
            duration = self.__videodata.get_duration(uuid)
            if duration is not "" and min <= duration <= max:
                if uuid not in uuids:
                    uuids.append(uuid)
        return uuids

    def genre(self, sub="") -> list:
        return self.search_by_attribute("genere", sub)

    def title(self, sub="") -> list:
        return self.search_by_attribute("title", sub)

    def album(self, sub="") -> list:
        return self.search_by_attribute("album", sub)

    def artist(self, sub="") -> list:
        return self.search_by_attribute("artist", sub)

    def composer(self, sub="") -> list:
        return self.search_by_attribute("composer", sub)

    def date(self, sub="") -> list:
        return self.search_by_attribute("date", sub)

    def comment(self, sub="") -> list:
        return self.search_by_attribute("comment", sub)
    
    def and_operator(self, list1: list, list2: list) -> list:
        #if not isinstance(list1, list) or not isinstance(list2, list):
         #   return []
        return list(set(list1) & set(list2))

    def or_operator(self, list1: list, list2: list) -> list:
        #if not isinstance(list1, list) or not isinstance(list2, list):
         #   return []
        return list(set(list1) | set(list2))

    def __str__(self):
        return str(self.__videodata)

    def __repr__(self):
        return f"SearchMetadata(videodata={repr(self.__videodata)})"
    
    def __len__(self):
        return len(self.__videodata)
    
    def __iter__(self):
        return iter(self.__videodata)
    
    #def __eq__(self, other):
     #   if not isinstance(other, SearchMetadata):
      #      return
       # return self.__videodata == other.__videodata
    
    #def __hash__(self):
     #   return hash(tuple(self.__videodata))
    
    #def __ne__(self, other):
     #   return not self.__eq__(other)
    
    #def __lt__(self, other):
     #   return len(self.__videodata) < len(other.__videodata)
    
    def get_similar(self, A: str, max_list: int = 25) -> list:
        pass
        """assert max_list <= 25
        semblances = {} # uuid: semblança
        for path in self.__videodata:
            B = str(cfg.get_uuid(cfg.get_canonical_pathfile(path)))
            
            AB_nodes, AB_value = self.__videodata.get_video_distance(A,B)
            BA_nodes, BA_value = self.__videodata.get_video_distance(B,A)
            AB = 0
            BA = 0
            
            if (AB_nodes != 0):
                AB = (AB_value / AB_nodes) * (self.__videodata.get_video_rank(A) / 2)
            if (BA_nodes != 0):
                BA = (BA_value / BA_nodes) * (self.__videodata.get_video_rank(B) / 2)
            semblances[B] = AB + BA
        
        uuids_ordenats = sorted(semblances.items(), key=lambda item: (-item[1], item[0]))
        return [uuid for uuid, _ in uuids_ordenats[:max_list]]"""
    
    def get_auto_play(self, N: int = 25) -> list:
        pass
        
        """ranks = {}  # uuid: rank
        for path in self.__videodata:
            uuid = str(cfg.get_uuid(cfg.get_canonical_pathfile(path)))
            ranks[uuid] = self.__videodata.get_video_rank(uuid)
        
        ranks_ordenats = sorted(ranks.items(), key=lambda item: (-item[1], item[0]))

        auto_play_list = [uuid for uuid, _ in ranks_ordenats[:N]]

        simil_list = {}  # uuid: [similar_uuids]
        for uuid in auto_play_list:
            simil_list[uuid] = self.get_similar(uuid, N // 2)

        total_simil_25_set = set(auto_play_list)  
        for similar_videos in simil_list.values():
            total_simil_25_set.update(similar_videos)  

        total_simil_25_list = sorted(
            total_simil_25_set,
            key=lambda uuid: (-ranks.get(uuid, 0), uuid)
        )[:25]

        idv_semblanca = {uuid: 0 for uuid in total_simil_25_list}
        for i in total_simil_25_list:
            for j in total_simil_25_list:
                if i != j:
                    idv_semblanca[i] += self.get_semblanca(i, j)

        ordered_simil = sorted(
            idv_semblanca.items(),
            key=lambda item: (-item[1], item[0])
        )

        result = [uuid for uuid, _ in ordered_simil[:N]]

        result.extend([None] * (N - len(result)))
        
        return result"""

                
            