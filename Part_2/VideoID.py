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
        self.__files = {}  # clau: path, valor: uuid
    
    def generate_uuid(self, file="") -> str:
        uuid = str(cfg.get_uuid(cfg.get_canonical_pathfile(file)))
        if uuid in self.__files.values():
            print("Nou uuid ha colisionat amb un uuid anterior. Operació cancelada.")
            return None
        self.__files[file] = uuid
        return uuid
    
    def get_uuid(self, file="") -> str:
        return self.__files.get(file)

    def _get_path(self, uuid: str) -> str:
        for key, val in self.__files.items():
            if val == uuid:
                return key

    def remove_uuid(self, uuid="") -> None:    
        try:
            self.__files.pop(self._get_path(uuid))
        except:
            print("No es pot eliminar uuid.")
        
    def __len__(self) -> int:
        return len(self.__files)
    
    def __str__(self) -> str:
        cad = '________VIDEO ID________\n'
        cad += 'Num fitxers identificats: ' + str(len(self.__files))
        return cad

    def __repr__(self):
        return f"VideoID({self.__files})"

    def __eq__(self, other):
        if not isinstance(other, VideoID):
            return NotImplemented
        return self.__files == other.__files

    def __hash__(self):
        return hash(self.__files)
    
    def __iter__(self):
        return iter(self.__files.items())
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __lt__(self, other):
        return len(self.__files) < len(other.__files)