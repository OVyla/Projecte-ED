#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cfg

class VideoID:
    """
    OBJECTIU: Gestionar el parell file-path <-> UUID.
    RESPONSABILITAT: Generar identificadors únics (UUID) per a cada arxiu MP4 individual de vídeo.
    """
    __slots__ = ['__files']
    def __init__(self):
        """
        Inicialitza el diccionari de fitxers.
        """
        self.__files = {}  # clau: path, valor: uuid
    
    def generate_uuid(self, file="") -> str:
        """
        Genera un UUID per a un fitxer donat.
        """
        uuid = str(cfg.get_uuid(cfg.get_canonical_pathfile(file))) # Obté un UUID a partir del camí normalitzat
        if uuid in self.__files.values(): # Comprova si el UUID ja existeix
            print("Nou uuid ha colisionat amb un uuid anterior. Operació cancelada.")
            return None # Retorna None si hi ha col·lisió
        self.__files[file] = uuid # Associa el fitxer amb el UUID
        return uuid
    
    def get_uuid(self, file="") -> str:
        """
        Retorna el UUID associat a un fitxer.
        """
        return self.__files.get(file)

    def __get_path(self, uuid: str) -> str:
        """
        Recupera el camí del fitxer associat a un UUID.
        """
        for key, val in self.__files.items():
            if val == uuid:
                return key

    def remove_uuid(self, uuid="") -> None:   
        """
        Elimina el UUID associat a un fitxer.
        """
        try:
            self.__files.pop(self.__get_path(uuid))
        except:
            print("No es pot eliminar uuid.")
        
    def __len__(self) -> int:
        """
        Retorna el nombre de fitxers emmagatzemats.
        """
        return len(self.__files)
    
    def __str__(self) -> str:
        """
        Retorna una representació en cadena de la classe.
        """
        return f"VideoID({self.__files})"

    def __repr__(self):
        """
        Retorna una representació formal de la classe.
        """
        return f"VideoID({self.__files})"
    
    def __iter__(self):
        """
        Permet la iteració sobre els fitxers.
        """
        return iter(self.__files.keys())
    