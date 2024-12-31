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
    __slots__ = ['__files', '__added', '__removed']

    def __init__(self):
        self.__files = []
        self.__added = []
        self.__removed = []
        
    
    def get_files(self) -> list:
        return self.__files
    
    def __getitem__(self, item: int) -> str:
        return self.__files[item]
    
    def reload_fs(self, path: str) -> None:
        """
        Carrega el sistema de fitxers i actualitza la llista d'arxius MP4.
        """
        files_anterior = copy.deepcopy(self.__files)
        self.__files = []
        self.__added = []
        self.__removed = []
        
        root = path+'/'
        for root, dirs, files in os.walk(path):
            for filename in files:
                if filename.lower().endswith('.mp4'):
                    absolut = os.path.join(root, filename)
                    if root in absolut:
                        absolut.replace(root,'')
                    self.__files.append(absolut)
        
        for file in self.__files:
            if file not in files_anterior:
                self.__added.append(file)
        
        for file in files_anterior:
            if file not in self.__files:
                self.__removed.append(file)
                

    def files_added(self) -> list:
        """
        Retorna una llista dels arxius MP4 que han estat afegits des de l'últim reload.
        """
        return self.__added

    def files_removed(self) -> list:
        """
        Retorna una llista dels arxius MP4 que han estat eliminats des de l'últim reload.
        """
        return self.__removed
    
    def __str__(self):
        cad = '________VIDEO FILES_____\n'
        cad += 'Num fitxers llegits: '+str(len(self.__files))
        return cad
    
    def __repr__(self):
        return f"VideoFiles({len(self.__files)} files)"
    
    def __len__(self):
        return len(self.__files)
    
    def __iter__(self):
        return iter(self.__files)
                                           