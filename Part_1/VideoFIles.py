# -*- coding: utf-8 -*-
"""
VideoFiles.py : ** REQUIRED ** El vostre codi de la classe VideoFiles.
"""
import cfg
import os
import copy

class VideoFiles:
    """
    OBJECTIU: Guardar la col·lecció dels arxius MP4.
    RESPONSABILITAT: Revisar el contingut del disc per obtenir les localitzacions
                    dels MP4 existents dins la col·lecció de vídeos.
    """

    def __init__(self):
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
        files_anterior = copy.deepcopy(self._files)
        added_anterior = copy.deepcopy(self._added)
        removed_anterior = copy.deepcopy(self._removed)
        self._files = []
        self._added = []
        self._removed = []
        
        
        for root, dirs, files in os.walk(path):
            for filename in files:
                if filename.lower().endswith('.mp4'):
                    self._files.append(os.path.join(root, filename))
        
        for file in self._files:
            if file not in files_anterior:
                self._added.append(file)
        
        for file in files_anterior:
            if file not in self._files:
                self._removed.append(file)
                

    def files_added(self) -> list:
        """
        Retorna una llista dels arxius MP4 que han estat afegits des de l'últim reload.
        """
        return self._added

    def files_removed(self) -> list:
        """
        Retorna una llista dels arxius MP4 que han estat eliminats des de l'últim reload.
        """
        return self._removed
    
    def __str__(self):
        cad = '________VIDEO FILES_____\n'
        cad += 'Num fitxers llegits: '+str(len(self._files))
        return cad
                                           
