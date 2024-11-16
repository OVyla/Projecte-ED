import cfg
import os
import shutil


class VideoFiles:
    """
    OBJECTIU: Guardar la col·lecció dels arxius MP4.
    RESPONSABILITAT: Revisar el contingut del disc per obtenir les localitzacions
                    dels MP4 existents dins la col·lecció de vídeos.
    """

    def __init__(self):
        self._root = ''
        self._files = []
        self._added = []
        self._removed = []
    
    def get_files(self) -> list:
        return self._files
    
    def __getitem__(self, item: int) -> str:
        return self._files[item]
    
    def reload_fs(self, path: str) -> None:
        """
        Carrega el sistema de fitxers i actualitza la llista d'arxius MP4.
        """
        self._root = path
        self._files = []
        self._added = []
        self._removed = []

        for root, dirs, files in os.walk(path):
            for filename in files:
                if filename.lower().endswith('.mp4'):
                    self._files.append(os.path.join(root, filename))

    def files_added(self) -> list:
        """
        Retorna una llista dels arxius MP4 que han estat afegits des de l'últim reload.
        """
        for root, dirs, files in os.walk(self._root):
            for filename in files:
                if filename.lower().endswith('.mp4'):
                    full_path = os.path.join(root, filename)
                    if full_path not in self._files and full_path not in self._added:
                        self._added.append(full_path)
        return self._added

    def files_removed(self) -> list:
        """
        Retorna una llista dels arxius MP4 que han estat eliminats des de l'últim reload.
        """
        for file in self._files:
            if not os.path.isfile(file) and file not in self._removed:
                self._removed.append(file)

        return self._removed
    
    def __str__(self):
        pass


def main():
    # Inicialitzem la classe VideoFiles
    vf = VideoFiles()

    # Carreguem el directori arrel
    root_dir = cfg.get_root()
    vf.reload_fs(root_dir)

    # Mostrar la llista d'arxius afegits
    print('Primer reload fet...')
    print()
    
    # Afegir un nou fitxer (heb_2.mp4)
    print('Afegint heb_2.mp4...')
    shutil.copyfile('/Users/aliciamartilopez/Desktop/ED/PROJECTE/P0/Videos/heb3070b1_1241630.mp4',
                    '/Users/aliciamartilopez/Desktop/ED/PROJECTE/P0/Videos/heb_2.mp4')
    print('Fitxers afegits (vf.files_added()):', vf.files_added())
    print()

    # Eliminar un fitxer (Doraemon Opening)
    print('Eliminant Doraemon Opening 1 (Català) (360p).mp4...')
    with open('/Users/aliciamartilopez/Desktop/ED/PROJECTE/P0/Videos/Doraemon Opening 1 (Català) (360p).mp4', 'rb') as video_file:
        video_eliminat = video_file.read()
    os.remove('/Users/aliciamartilopez/Desktop/ED/PROJECTE/P0/Videos/Doraemon Opening 1 (Català) (360p).mp4')
    print('Fitxers eliminats (vf.files_removed()):', vf.files_removed())
    print()

    # Tornem a carregar el sistema de fitxers i comprovem canvis
    print('Nou reload...')
    vf.reload_fs(root_dir)
    print('Fitxers afegits després del reload:', vf.files_added())
    print('Fitxers eliminats després del reload:', vf.files_removed())
    print()
    print()
    
    # Tornem a deixar tot com estava (eliminar heb_2.mp4 i recrear Doraemon i finalment carregar el reload)
    print('Tornant tot a l\'estat original...')
    os.remove('/Users/aliciamartilopez/Desktop/ED/PROJECTE/P0/Videos/heb_2.mp4')
    print('Eliminat heb_2.mp4 (vf.files_removed()):', vf.files_removed())

    with open('/Users/aliciamartilopez/Desktop/ED/PROJECTE/P0/Videos/Doraemon Opening 1 (Català) (360p).mp4', 'wb') as new_video_file:
        new_video_file.write(video_eliminat)
    print('Recreat Doraemon (vf.files_added()):', vf.files_added())
    print('Carregant els canvis fent reload...')
    vf.reload_fs(root_dir)
    print('Fitxers afegits després del reload:', vf.files_added())
    print('Fitxers eliminats després del reload:', vf.files_removed())
    print()
    print("Finalitzat!")


if __name__ == "__main__":
    main()

