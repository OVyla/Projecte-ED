import tinytag
import numpy as np
import os
import cfg


class VideoData:
    def __init__(self):
        self._files = {}

    def add_video(self, uuid: str, file: str) -> None:
        """Afegeix un nou vídeo amb el seu path al diccionari, sense metadades."""
        if uuid in self._files:
            print(f"El vídeo amb UUID {uuid} ja existeix.")
            return 

        if not os.path.isfile(file):
            print(f"El fitxer {file} no existeix.")
            return 
            
        if not file.lower().endswith('.mp4'):
            print("El fitxer no és compatible.")
            return 

        self._files[uuid] = {'path': file, 'metadata': None}

    def remove_video(self, uuid: str) -> None:
        """Elimina un vídeo pel seu UUID."""
        if uuid in self._files:
            del self._files[uuid]
        else:
            print(f"El vídeo amb UUID {uuid} no existeix.")

    def load_metadata(self, uuid: str) -> None:
        """Carrega les metadades d'un arxiu MP4 i les guarda al diccionari."""
        
        if uuid not in self._files:
            print(f"UUID {uuid} no trobat.")
            return
        
        path = self._files[uuid]['path']
        
        try:
            metadata = tinytag.TinyTag.get(path)
            self._files[uuid]['metadata'] = metadata
            
        except Exception as e:
            print(f"No s'han pogut carregar les metadades per {path}: {e}")
            return
        

    def _get_metadata_field(self, uuid: str, field: str, default="None"):
        """Funció interna per obtenir un camp de les metadades."""
        if uuid not in self._files:
            print(f"UUID {uuid} no trobat.")
            return 

        metadata = self._files[uuid]['metadata']
        if metadata is None:
            print("Les metadades no s'han carregat")
            return 

        return getattr(metadata, field, default)

    def get_duration(self, uuid: str) -> int:
        if uuid not in self._files:
            print(f"UUID {uuid} no trobat.")
            return None

        metadata = self._files[uuid]['metadata']
        if not metadata:
            print("Les metadades no s'han carregat.")
            return None

        return int(np.ceil(metadata.duration))

    def get_title(self, uuid: str) -> str:
        return self._get_metadata_field(uuid, 'title')

    def get_album(self, uuid: str) -> str:
        return self._get_metadata_field(uuid, 'album')

    def get_artist(self, uuid: str) -> str:
        return self._get_metadata_field(uuid, 'artist')

    def get_composer(self, uuid: str) -> str:
        return self._get_metadata_field(uuid, 'composer')

    def get_genre(self, uuid: str) -> str:
        return self._get_metadata_field(uuid, 'genre')

    def get_date(self, uuid: str) -> str:
        return self._get_metadata_field(uuid, 'year')  # tinytag usa 'year' en lloc de 'date'

    def get_comment(self, uuid: str) -> str:
        return self._get_metadata_field(uuid, 'comment')

    def get_filename(self, uuid: str) -> str:
        """"retorna el string del filename guardat"""
        if uuid not in self._files:
            print(f"UUID {uuid} no trobat.")
            return None
        return self._files[uuid]['path']

    def __len__(self):
        return len(self._files) 
        
    def __str__(self):
        pass

