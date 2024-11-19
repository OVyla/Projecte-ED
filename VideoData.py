# -*- coding: utf-8 -*-
import cfg
import os
import sys
import numpy
import sys
import tinytag

class VideoData:
    def __init__(self):
        self._files={}

    def existeix_file(self, file):
        return file in [v[0] for v in self._files.values()]

    def add_video(self, uuid, file):
        if not self.existeix_file(file):
            path = os.path.join(os.path.join(cfg.get_root(), file))
            self._files[uuid] = [file,path]

    def remove_video(self, uuid):
        if uuid in self._files.keys(): 
            del self._files[uuid]

    def load_metadata(self, uuid):
        if self.existeix_uuid(uuid):
            path = self._files[uuid][1]
            metadata = tinytag.TinyTag.get(path)
            if metadata is None:
                print("ERROR: Arxiu MP4 erroni!")
                sys.exit(1)
            try:
                self._files[uuid].append(numpy.ceil(metadata.duration))

            except AttributeError:
                duration = -1
            
            try:
                self._files[uuid].append(metadata.title)
            except AttributeError:
                title = "None"
         
            try:
                self._files[uuid].append(metadata.album)
            except AttributeError:
                album = "None"

            try:
                self._files[uuid].append(metadata.artist)
            except AttributeError:
                artist = "None"
            
            try:
                self._files[uuid].append(metadata.composer)
            except AttributeError:
                composer = "None"
            

            try:
                self._files[uuid].append(metadata.genre)
            except AttributeError:
                genre = "None"
            
            try:
                self._files[uuid].append(metadata.year)
            except AttributeError:
                date = "None"
            
            try:
                self._files[uuid].append(metadata.comment)
            except AttributeError:
                comment = "None"
            
 
    def __len__(self):
        return len(self._files)

    def existeix_uuid(self,uuid):
        return uuid in self._files.keys()
   
    def existeix_meta(self,uuid):
        if self.existeix_uuid(uuid):
            m = len(self._files[uuid])
            return m > 2
       
    def get_filename(self,uuid):
        if self.existeix_meta(uuid):
            return str(self._files[uuid][0])
   
    def get_path(self,uuid):
        if self.existeix_meta(uuid):
            return self._files[uuid][1]
   
    def get_duration(self,uuid):
        if self.existeix_meta(uuid):
            return self._files[uuid][2]
       
    def get_title(self,uuid):
        if self.existeix_meta(uuid):
            return str(self._files[uuid][3])
       
    def get_album(self,uuid):
        if self.existeix_meta(uuid):
            return str(self._files[uuid][4])
       
    def get_artist(self,uuid):
        if self.existeix_meta(uuid):
            return str(self._files[uuid][5])
       
    def get_composer(self,uuid):
        if self.existeix_meta(uuid):
            return str(self._files[uuid][6])
       
    def get_genre(self,uuid):
        if self.existeix_meta(uuid):
            return str(self._files[uuid][7])
       
    def get_date(self,uuid):
        if self.existeix_meta(uuid):
            return str(self._files[uuid][8])

    def get_comment(self,uuid):
        if self.existeix_meta(uuid):
            return str(self._files[uuid][9])
   
    def files(self):
        return self._files
    

    def get_uuids(self) -> list:
        """Retorna tots els UUIDs disponibles."""
        return list(self._files.keys())
