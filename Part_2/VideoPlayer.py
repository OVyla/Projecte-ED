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
    """
    OBJECTIU: Gestionar la reproducció de vídeos.
    RESPONSABILITAT: Proporcionar funcionalitats per reproduir vídeos i mostrar les seves metadades.
    """
    __slots__ = ['__video_data']

    def __init__(self, *args):
        """
        Inicialitza la classe VideoPlayer.
        """
        if len(args) != 1 or not isinstance(args[0], VideoData.VideoData):
            raise NotImplementedError("Cal passar exactament un objecte de tipus VideoData.VideoData.")  # Llença una excepció si no es passa un objecte VideoData
        self.__video_data = args[0]


    def print_video(self, uuid: str) -> None:
        """
        Imprimeix les metadades d'un vídeo associat a un UUID.
        """
        print("Duració:", self.__video_data.get_duration(uuid))
        print("Títol:", self.__video_data.get_title(uuid))
        print("Àlbum:", self.__video_data.get_album(uuid))
        print("Artista:", self.__video_data.get_artist(uuid))
        print("Compositor:", self.__video_data.get_composer(uuid))
        print("Gènere:", self.__video_data.get_genre(uuid))
        print("Data:", self.__video_data.get_date(uuid))
        print("Comentari:", self.__video_data.get_comment(uuid))

    def play_file(self, file: str) -> None:
        """
        Reprodueix un fitxer de vídeo.
        """
        if not os.path.exists(file):
            return None
        uuid = str(cfg.get_uuid(cfg.get_canonical_pathfile(file)))
        
        duracio = self.__video_data.get_duration(uuid)
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
        """
        Reprodueix un vídeo associat a un UUID en un mode especificat.
        """
        if uuid not in self.__video_data:  # Comprova si l'UUID existeix
            print('Video no afegit.')
            return None
        if not isinstance(mode, int):
            return None
            
        if mode < 2:  # Si el mode és menor que 2
            self.print_video(uuid)  # Imprimeix les metadades del vídeo
        if mode > 0:  # Si el mode és major que 0
            file = self.__video_data.get_filename(uuid)  # Obté el nom del fitxer
            return self.play_file(file)  # Reprodueix el fitxer
            
        return None
    
    def __str__(self):
        """
        Retorna una representació en cadena de la classe VideoPlayer.
        """
        return f"VideoPlayer: {len(self.__video_data)} vídeos disponibles."
    
    def __contains__(self, uuid):
        """
        Comprova si un UUID està en el VideoData.
        """
        return uuid in self.__video_data
    
    
    def __repr__(self):
        """
        Retorna una representació formal de la classe VideoPlayer.
        """
        return f"VideoPlayer(VideoData={len(self.__video_data)})"


