#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cfg

class VideoID:
    """
    OBJECTIU: Gestionar el parell file-path <-> UUID.
    RESPONSABILITAT: Generar identificadors únics (UUID) per a cada arxiu MP4 individual de vídeo.
    """
    __slots__ = ['_files']
    def __init__(self):
        self._files = {}  # clau: path, valor: uuid
    
    def generate_uuid(self, file="") -> str:
        uuid = str(cfg.get_uuid(cfg.get_canonical_pathfile(file)))
        for v in self._files.values():
            if uuid == v:
                print("Nou uuid ha colisionat amb un uuid anterior. Operació cancelada.")
                return None
        self._files[file] = uuid
        return uuid
    
    def get_uuid(self, file="") -> str:
        return self._files.get(file)

    def _get_path(self, uuid: str) -> str:
        for key, val in self._files.items():
            if val == uuid:
                return key

    def remove_uuid(self, uuid="") -> None:    
        try:
            self._files.pop(self._get_path(uuid))
        except:
            print("No es pot eliminar uuid.")
        
    def __len__(self) -> int:
        return len(self._files)
    
    def __str__(self) -> str:
        cad = '________VIDEO ID________\n'
        cad += 'Num fitxers identificats: ' + str(len(self._files))
        return cad

    def __repr__(self):
        return f"VideoID({self.id_value})"

    def __eq__(self, other):
        if not isinstance(other, VideoID):
            return NotImplemented
        return self.id_value == other.id_value

    def __hash__(self):
        return hash(self.id_value)
    
    def __iter__(self):
        return iter(self._files)
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __lt__(self, other):
        return len(self._files) < len(other._files)