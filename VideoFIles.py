import cfg
import os


class VideoFiles:
    """
    OBJECTIU: Guardar la col·lecció dels arxius MP4.
    RESPONSABILITAT: Revisar el contingut dels disc per a obtenir les localitzacions en l’estructura dels MP4 que
                    actualment existeixen dins la col·lecció de vídeos.

    Físicament els arxius MP4 estaran exclusivament en el disc, per tant la classe només guarda el path dels arxius
    """

    def __init__(self):
        self._files = []
        self._path = ""

    def reload_fs(self, path: str) -> None:

        self._path = path

        for root, dirs, files in os.walk(path):
            for filename in files:
                if filename.lower().endswith(tuple(['.mp4'])):
                    self._files.append(os.path.join(root, filename))

    def get_files(self) -> list:
        return self._files

    def __getitem__(self, item: int) -> str:
        return self._files[item]

    def files_added(self) -> list:

        files_added = []

        try:
            for root, dirs, files in os.walk(self._path):
                for filename in files:
                    if filename.lower().endswith(tuple(['.mp4'])):
                        if os.path.join(root, filename) not in self._files:
                            self._files.append(os.path.join(root, filename))
                            files_added.append(os.path.join(root, filename))

        except Exception as e:
            print("files_added() error: ", e)
            return files_added

        else:
            return files_added

    def files_removed(self) -> list:

        files_removed = []

        try:
            for file in self._files:
                if not os.path.isfile(file):
                    files_removed.append(file)
                    self._files.remove(file)

        except Exception as e:
            print("files_removed() error: ", e)
            return files_removed

        else:
            return files_removed


if __name__ == "__main__":
    vf = VideoFiles()
    vf.reload_fs(cfg.get_root())
    print(vf.get_files())
    print("Number of files: ", len(vf.get_files()))
    print("Done!")