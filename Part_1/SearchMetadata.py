import VideoData
import cfg

class SearchMetadata:
    def __init__(self, videodata: VideoData):
        self._videodata = videodata

    def search_by_attribute(self, attribute: str, sub: str) -> list:
        if not sub or not isinstance(sub, str):
            print("ValueError: Valor de cerca necessari i ha de ser un string.")
            return []

        uuids = []
        for uuid in self._videodata.files():
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
        if min < 0 or max < 0 or min > max:
            print("ValueError: Valors de durada incorrectes")
            return []

        uuids = []
        for uuid in self._videodata.files():
            duration = self._videodata.get_duration(uuid)
            if duration is not None and min <= duration <= max:
                uuids.append(uuid)
        return uuids

    def title(self, sub="") -> list:
        return self.search_by_attribute("title", sub)

    def album(self, sub="") -> list:
        return self.search_by_attribute("album", sub)

    def artist(self, sub="") -> list:
        return self.search_by_attribute("artist", sub)

    def composer(self, sub="") -> list:
        return self.search_by_attribute("composer", sub)

    def genre(self, sub="") -> list:
        return self.search_by_attribute("genre", sub)

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