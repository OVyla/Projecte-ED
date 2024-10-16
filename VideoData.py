import tinytag
import numpy as np

class VideoData:
    def __init__(self):
        self._files = {}

    def add_video(self, uuid: str, file: str) -> None:
        """Afegeix un nou vídeo amb el seu path al diccionari, sense metadades."""
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

    def _get_metadata_field(self, uuid: str, field: str, default="None"):
        """Funció interna per obtenir un camp de les metadades."""
        if uuid not in self._files:
            return "UUID no trobat"
        
        metadata = self._files[uuid]['metadata']
        if metadata is None:
            return "Les metadades no s'han carregat"
        
        return getattr(metadata, field, default)

    def get_duration(self, uuid: str) -> int:
        """Retorna la duració en segons, o -1 si no es pot obtenir."""
        try:
            metadata = self._files[uuid]['metadata']
            return int(np.ceil(metadata.duration)) if metadata else -1
        except (KeyError, AttributeError):
            return -1

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


def main():
    vd = VideoData()
    uuid = '5f665e9e-16ea-5e5f-9d93-91c802c81618'
    
    # Afegir el vídeo
    print('Afegint video...')
    vd.add_video(uuid, '/Users/aliciamartilopez/Desktop/ED/PROJECTE/P0/Videos/Uh, oh, no tinc por! (720p).mp4')

    # Provar sense carregar les metadades
    print('Duració (sense metadades):', vd.get_duration(uuid))
    print('Titol (sense metadades):', vd.get_title(uuid))

    # Carregar les metadades
    print('\nCarregant metadades del video...')
    vd.load_metadata(uuid)

    # Provar amb les metadades carregades
    print('Duració:', vd.get_duration(uuid))
    print('Titol:', vd.get_title(uuid))
    print('Album:', vd.get_album(uuid))
    print('Artista:', vd.get_artist(uuid))
    print('Compositor:', vd.get_composer(uuid))
    print('Gènere:', vd.get_genre(uuid))
    print('Data:', vd.get_date(uuid))
    print('Comentari:', vd.get_comment(uuid))

    # Eliminar el vídeo
    print('\nEliminant dades del vídeo...')
    vd.remove_video(uuid)
    print('Vídeo eliminat.')
    print()
    print('Finalitzat!')

if __name__ == "__main__":
    main()
