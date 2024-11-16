#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 16:29:17 2024

@author: aliciamartilopez
"""

import vlc
import time
import cfg
import VideoData 
import VideoFiles 
import VideoID 

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
        
        uuid = cfg.get_uuid(cfg.get_canonical_pathfile(file))
        duracio = self._video_data.get_duration(uuid)
        
        player = vlc.MediaPlayer(file)
        player.play()
    
        timeout = time.time() + duracio
        while True:
            if time.time() < timeout:
                try:
                    time.sleep(1)
                except KeyboardInterrupt:  # STOP amb <CTRL>+<C> a la consola
                    break
            else:
                break
        
        player.stop()

    def play_video(self, uuid: str, mode: int) -> None:
        if mode < 2:
            self.print_video(uuid)
        if mode > 0:
            file = self._video_data.get_filename(uuid)
            self.play_file(file)
    
    def __str__(self):
        pass
"""
def main():
    root = cfg.get_root()
    
    v_files = VideoFiles(root)
    v_id = VideoID()
    v_data = VideoData()
    
    videos_afegits = v_files.files_added()
    for path in videos_afegits:
        v_id.generate_uuid(path)
        uuid = v_id.get_uuid(path)
        v_data.add_video(uuid, path)
        v_data.load_metadata(uuid)
    v_files.reload_fs(root)
    
    v_player = VideoPlayer(v_data, v_id)
    
    print('Print Video heb307...630.mp4')
    uuid = v_id.get_uuid('/Users/aliciamartilopez/Desktop/ED/PROJECTE/P0/Videos/heb3070b1_1241630.mp4')
    uuid2 = v_id.get_uuid('/Users/aliciamartilopez/Desktop/ED/PROJECTE/P0/Videos/Les Tres Bessones - Opening HD (720p).mp4')
    
    mode = cfg.PLAY_MODE  # Això ho agafes de la configuració
    v_player.play_video(uuid2, mode)
    

if __name__ == "__main__":
    main()
"""