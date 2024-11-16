import cfg
import VideoFIles


class VideoID:
    """
    OBJECTIU: Gestionar el parell file-path <-> UUID.
    RESPONSABILITAT: Generar identificadors únics (UUID) per a cada arxiu MP4 individual de vídeo.
    """

    def __init__(self):
        self._files = {}  # clau: path, valor: uuid

    def generate_uuid(self, file: str) -> str:
        try:
            if file in self._files:
                resposta = 'Ja existeix un uuid pel fitxer: '+file
                return resposta
            else:
                uuid = cfg.get_uuid(cfg.get_canonical_pathfile(file))
                if uuid in self._files.values():
                    resposta = "L'uuid generat ha colisionat amb un uuid creat anteriorment. Operació cancelada."
                    return resposta
                else:
                    self._files[file] = uuid
                    return uuid
        except Exception as e:
            return("VideoID, generate_uuid error: ", e)

    def get_uuid(self, file: str) -> str:
        try:
            return self._files[file]

        except Exception:
            resposta = "No s'ha trobat cap uuid pel fitxer: "+file
            return resposta
    
    def get_path(self, uuid: str) -> str:
        try:
            for key, val in self._files.items():
                if val == uuid:
                    return key
            return None

        except Exception:
            resposta = "uuid no trobat"
            return resposta

    def remove_uuid(self, uuid: str) -> None:
        try:
            for key, val in self._files.items():
                if val == uuid:
                    path = self.get_path(uuid)
                    del self._files[path]
                    return None
            raise Exception()
        except:
            resposta = "No es pot eliminar uuid si no es troba"
            return resposta
    
    def __str__(self):
        pass


"""def main():
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
    main()"""