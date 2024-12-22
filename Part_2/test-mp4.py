# -*- coding: utf-8 -*-
"""
test-mp4.py : Script de proves per reproduïr MP4
"""

import cfg      # Necessari per a la pràctica !!
                # Mireu el contingut de l'arxiu

import os.path
import sys
import numpy    #  installed in anaconda by default
import time
#               Només per fer play dels media
import vlc      #  $ pip install python-vlc
#               Especific per obtenir les metadades
import tinytag  #  $ pip install tinytag


# STEP 1: Cerca dels arxius al filesystem
print("Cercant arxius dins [" + cfg.get_root() + "]\n")
uri_file = cfg.get_one_file(0)  # Aquesta funció és només de proves!
if not os.path.isfile(uri_file):
    print("ERROR: Arxiu MP4 inexistent!")
    sys.exit(1)


# STEP 2: Obtenció de les metadades
metadata = tinytag.TinyTag.get(uri_file)
print(metadata)
print('')

if metadata is None:
    print("ERROR: Arxiu MP4 erroni!")
    sys.exit(1)

try:
    duration = int(numpy.ceil(metadata.duration))
except AttributeError:
    duration = -1
try:
    title    = metadata.title
except AttributeError:
    title    = "None"
try:
    album    = metadata.album
except AttributeError:
    album    = "None"
try:
    artist   = metadata.artist
except AttributeError:
    artist   = "None"
try:
    composer = metadata.composer
except AttributeError:
    composer = "None"
try:
    genre    = metadata.genre
except AttributeError:
    genre    = "None"
try:
    date     = metadata.year
except AttributeError:
    date     = "None"
try:
    comment  = metadata.comment
except AttributeError:
    comment  = "None"


# STEP 3: Generació del identificador únic
name_file = cfg.get_canonical_pathfile(uri_file)
mp4_uuid  = cfg.get_uuid(name_file)


# STEP 4: Reproducció
if (cfg.PLAY_MODE < 2):
    print("Reproduïnt [{}]".format(uri_file))
    print(" Duració:  {} segons".format(duration))
    print(" Títol:    {}".format(title))
    print(" Àlbum:    {}".format(album))
    print(" Artista:  {}".format(artist))
    print(" Composer: {}".format(composer))
    print(" Gènere:   {}".format(genre))
    print(" Data:     {}".format(date))
    print(" Comments: {}".format(comment))
    print(" UUID:     {}".format(mp4_uuid))
    print(" Arxiu:    {}".format(name_file))

if (cfg.PLAY_MODE > 0):
    player = vlc.MediaPlayer(uri_file)

    player.play()     # Nota: Crida ASYNC !!

    # Poolling loop pel control de la reproducció
    timeout = time.time() + duration
    while True:
        if time.time() < timeout:
            try:
                time.sleep(1)
            except KeyboardInterrupt:  # STOP amb <CTRL>+<C> a la consola
                break
        else:
            break

    player.stop()


# END
print("\nFinal!")
