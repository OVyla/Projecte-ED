import cfg
import VideoFIles


class VideoID:
    """
    OBJECTIU: Gestionar el parell file-path <-> UUID.
    RESPONSABILITAT: Generar identificadors únics (UUID) per a cada arxiu MP4 individual de vídeo.
    """

    def __init__(self):
        self._uuid = {}  # clau: uuid, valor: file

    def generate_uuid(self, file: str) -> str:
        try:
            uuid = cfg.get_uuid(cfg.get_canonical_pathfile(file))
            if uuid in self._uuid:
                print("VideoID, generate_uuid: UUID already exists! ", file, "Will not be used.")
                return None
            else:
                self._uuid[uuid] = file
                return uuid

        except Exception as e:
            print("VideoID, generate_uuid error: ", e)

    def get_uuid(self, file: str) -> str:
        try:
            return self._uuid[cfg.get_uuid(cfg.get_canonical_pathfile(file))]

        except Exception as e:
            print("VideoID, get_uuid error: ", e)

    def get_path(self, uuid: str) -> str:
        try:
            return self._uuid[uuid]
        except Exception:
            resposta = "uuid no trobat"
            return resposta

    def remove_uuid(self, uuid: str) -> None:
        try:
            del self._uuid[uuid]

        except Exception as e:
            print("VideoID, remove_uuid error: ", e)
    
    def __str__(self):
        pass


def main():
    print('Generant VideoId')
    v_id = VideoID()
    print()
    
    path_file = '/Users/aliciamartilopez/Desktop/ED/PROJECTE/P0/Videos/Doraemon Opening 1 (Català) (360p).mp4'
    
    print('Generant uuid pel video Doraemon.mp4:', v_id.generate_uuid(path_file))
    print()
    uuid = v_id.get_uuid(path_file)
    print('Tornant a generar uuid pel video Doraemon.mp4:', v_id.generate_uuid(path_file))
    print()
    
    print('Comprovant mètode get_uuid pel video Doraemon.mp4:',v_id.get_uuid(path_file))
    print()
    
    v_id.remove_uuid(uuid)
    print('Esborrant uuid pel video Doraemon.mp4:',v_id.get_uuid(path_file))
    print()
    print('Tornant a esborrar Doraemon.mp4: '+v_id.remove_uuid(uuid))
    print()
    
    print('Fet!')
    
    


if __name__ == "__main__":
    main()