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
        """
        Inicialitza les llistes de fitxers, afegits i eliminats.
        """
        self.__files = []    # Llista de fitxers MP4
        self.__added = []    # Llista de fitxers afegits
        self.__removed = []  # Llista de fitxers eliminats
        
    
    def reload_fs(self, path: str) -> None:
        """
        Carrega el sistema de fitxers i actualitza la llista d'arxius MP4.
        """
        files_anterior = copy.deepcopy(self.__files)  # Guarda l'estat anterior
        self.__files = []  # Reinicia la llista de fitxers
        self.__added = []  # Reinicia la llista de fitxers afegits
        self.__removed = []  # Reinicia la llista de fitxers eliminats
        
        root = path+'/'
        for root, dirs, files in os.walk(path):
            for filename in files:
                if filename.lower().endswith('.mp4'):
                    file = os.path.join(root, filename)
                    if root in file:
                        file.replace(root,'') # Elimina el camí del directori root per guardar només el path relatiu
                    self.__files.append(file)  # Afegeix el fitxer a la llista
        
        for file in self.__files:
            if file not in files_anterior:
                self.__added.append(file)  # Afegeix a la llista d'afegits
        
        for file in files_anterior:
            if file not in self.__files:
                self.__removed.append(file)  # Afegeix a la llista d'eliminats
                

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
        """
        Retorna una representació en cadena de la classe.
        """
        return f"VideoFiles({len(self.__files)} files)"
    
    def __repr__(self):
        """
        Retorna una representació formal de la classe.
        """
        return f"VideoFiles({len(self.__files)} files)"
    
    def __len__(self):
        """
        Retorna el nombre de fitxers en la col·lecció.
        - int: Nombre de fitxers MP4.
        """
        return len(self.__files)
    
    def __iter__(self):
        """
        Permet la iteració sobre els fitxers de vídeo.
        """
        return iter(self.__files)
                                           