import cfg
import VideoFIles


class VideoID:
    """
    OBJECTIU: Gestionar el parell file-path <-> UUID.
    RESPONSABILITAT: Generar identificadors únics (UUID) per a cada arxiu MP4 individual de vídeo.
    """

    def __init__(self):
        self._uuid = {}  # clau: valor, valor: file

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

    def remove_uuid(self, file: str) -> None:
        try:
            del self._uuid[cfg.get_uuid(cfg.get_canonical_pathfile(file))]

        except Exception as e:
            print("VideoID, remove_uuid error: ", e)


if __name__ == "__main__":
    print("run")
    vf = VideoFIles.VideoFiles()
    vf.reload_fs(cfg.get_root())
    print(vf)
    vid = VideoID()
    vid.generate_uuid(vf[0])
