import VideoData
import cfg

class SearchMetadata:

    __slots__ = ['_videodata']
    
    def __init__(self, *args):
        if len(args) != 1 or not isinstance(args[0], VideoData.VideoData):
            raise NotImplementedError
        self._videodata = args[0]
        
    def search_by_attribute(self, attribute: str, sub: str) -> list:
        if not sub or not isinstance(sub, str):
            print("ValueError: Valor de cerca necessari i ha de ser un string.")
            return []

        uuids = []
        for uuid in self._videodata._get_uuids():
            try:
                method = getattr(self._videodata, f"get_{attribute}", None)
                if method is None or not callable(method):
                    print(f"Attribute '{attribute}' does not exist or is not callable.")
                    return []

                value = method(uuid)
                if value is not None and isinstance(value, (str, int, float)):
                    if sub.lower() in str(value).lower():
                        uuids.append(uuid)
            except Exception as e:
                print(f"Error amb UUID {uuid}: {e}")
        return uuids

    def duration(self, min: int, max: int) -> list:
        if not isinstance(min, int) or not isinstance(max, int):
            raise TypeError("Els valors de durada han de ser números.")
        if min < 0 or max < 0 or min > max:
            print("ValueError: Valors de durada incorrectes")
            return []

        uuids = []
        for uuid in self._videodata:
            duration = self._videodata.get_duration(uuid)
            if duration is not None and min <= duration <= max:
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
        return list(set(list1) & set(list2))

    def or_operator(self, list1: list, list2: list) -> list:
        return list(set(list1) | set(list2))

    def __str__(self):
        return str(self._videodata)

    def __repr__(self):
        return f"SearchMetadata(videodata={repr(self._videodata)})"
    
    def __len__(self):
        return len(self._videodata)
    
    def __iter__(self):
        return iter(self._videodata)
    
    def __eq__(self, other):
        if not isinstance(other, SearchMetadata):
            return NotImplemented
        return self._videodata == other._videodata
    
    def __hash__(self):
        return hash(tuple(self._videodata))
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __lt__(self, other):
        return len(self._videodata) < len(other._videodata)
    
    def get_similar(uuid: str, max_list: int) -> list:
        pass
    
    def get_auto_play(len: int) -> list:
        pass