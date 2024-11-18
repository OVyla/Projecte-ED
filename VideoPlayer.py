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
    def __init__(self, video_data):
        self._video_data = video_data

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
        if not os.path.isfile:
            return None
        if file not in self._video_data._files:
            return None
        uuid = cfg.get_uuid(cfg.get_canonical_pathfile(file))
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
        if uuid not in self._video_data._files:
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


