# -*- coding: utf-8 -*-
"""
VideoFiles.py : ** REQUIRED ** El vostre codi de la classe VideoFiles.
"""
import cfg
import os
#import shutil


class VideoFiles:
    """
    OBJECTIU: Guardar la col·lecció dels arxius MP4.
    RESPONSABILITAT: Revisar el contingut del disc per obtenir les localitzacions
                    dels MP4 existents dins la col·lecció de vídeos.
    """

    def __init__(self, root:cfg.get_root()):
        self._root = root
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
    
    def __str__(self) -> str:
        cad = '________VIDEO FILES_____\n'
        cad += 'Num fitxers llegits: '+str(len(self._files))
        return cad