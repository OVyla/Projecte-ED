#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import vlc
import time
import cfg
import VideoData 
import VideoFiles 
import VideoID 
import os

class VideoPlayer:
    __slots__ = ['_video_data']

    def __init__(self, *args):
        if len(args) != 1 or not isinstance(args[0], VideoData.VideoData):
            raise NotImplementedError("Cal passar exactament un objecte de tipus VideoData.VideoData.")
        self._video_data = args[0]


    def print_video(self, uuid: str) -> None:
        print("Duració:", self._video_data.get_duration(uuid))
        print("Títol:", self._video_data.get_title(uuid))
        print("Àlbum:", self._video_data.get_album(uuid))
        print("Artista:", self._video_data.get_artist(uuid))
        print("Compositor:", self._video_data.get_composer(uuid))
        print("Gènere:", self._video_data.get_genre(uuid))
        print("Data:", self._video_data.get_date(uuid))
        print("Comentari:", self._video_data.get_comment(uuid))

    def play_file(self, file: str) -> None:
        if not os.path.exists(file):
            return None
        uuid = cfg.get_uuid(cfg.get_canonical_pathfile(file))
        
        if uuid not in self._video_data._graph:
            return None
        duracio = self._video_data.get_duration(uuid)
        try:
            player = vlc.MediaPlayer(file)
            player.play()
        except Exception:
            return None
    
        timeout = time.time() + duracio
        while True:
            if time.time() < timeout:
                try:
                    time.sleep(1)
                except KeyboardInterrupt:  # STOP amb <CTRL>+<C> a la consola
                    return None
            else:
                return None
        
        player.stop()
        
        return player

    def play_video(self, uuid: str, mode: int) -> None:
        
        if uuid not in self._video_data:
            print('Video no afegit.')
            return None
        if not isinstance(mode, int):
            return None
            
        if mode < 2:
            self.print_video(uuid)
        if mode > 0:
            file = self._video_data.get_filename(uuid)
            return self.play_file(file)
            
        return None
            
            
    
    def __str__(self):
        return f"VideoPlayer: {len(self._video_data)} vídeos disponibles."

    def __repr__(self):
        return f"VideoPlayer(video_data={repr(self._video_data)})"
    
    def __len__(self):
        return len(self._video_data)
    
    def __contains__(self, uuid):
        return uuid in self._video_data
    
    def __iter__(self):
        return iter(self._video_data)
    
    def __eq__(self, other):
        if not isinstance(other, VideoPlayer):
            return NotImplemented
        return self._video_data == other._video_data
    
    def __hash__(self):
        return hash(tuple(self._video_data))
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __lt__(self, other):
        return len(self._video_data) < len(other._video_data)


