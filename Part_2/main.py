#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import VideoFiles
import VideoID
import VideoData
import VideoPlayer
import PlayList
import SearchMetadata
import GrafHash
import ElementData


"""
Test: VideoData (Func3)
--------------------------------------------
Test: Func3 (debug=False)
[3.0] OK: initializing VideoData (0 elements)
[3.0] OK: VideoData.add_video() declaration
[3.0] OK: VideoData.remove_video() declaration
[3.0] OK: VideoData.load_metadata() declaration
[3.0] OK: VideoData.get_duration() declaration
[3.0] OK: VideoData.get_title() declaration
[3.0] OK: VideoData.get_album() declaration
[3.0] OK: VideoData.get_artist() declaration
[3.0] OK: VideoData.get_composer() declaration
[3.0] OK: VideoData.get_genre() declaration
[3.0] OK: VideoData.get_date() declaration
[3.0] OK: VideoData.get_comment() declaration
[3.0] OK: VideoData.get_filename() declaration
--------------------------------------------
[3.1] OK: with empty VideoData class
--------------------------------------------
[3.2] OK: not loading fake files
--------------------------------------------
[3.3] OK: adding fake videos (1 element)
--------------------------------------------
[3.4] OK: testing remove video (0 elements)
--------------------------------------------
[3.5] OK: testing adding all videos (175 elements)
--------------------------------------------
WARNING with empty metadata elements
WARNING with empty metadata elements
WARNING with empty metadata elements
WARNING with empty metadata elements
WARNING with empty metadata elements
WARNING with empty metadata elements
WARNING with empty metadata elements
WARNING with empty metadata elements
WARNING with empty metadata elements
WARNING with empty metadata elements
WARNING with empty metadata elements
WARNING with empty metadata elements
WARNING with empty metadata elements
WARNING with empty metadata elements
WARNING with empty metadata elements
WARNING with empty metadata elements
WARNING with empty metadata elements
WARNING with empty metadata elements
WARNING with empty metadata elements
WARNING with empty metadata elements
[3.6] FAIL: with empty metadata elements
--------------------------------------------
[3.7] OK: (expected) when loading metadata elements
--------------------------------------------
[3.8] OK: metadata elements loaded
--------------------------------------------
Partial Grade: 45
============================================
--------------------------------------------
Test: VideoPlayer (Func4)
--------------------------------------------
Test: Func4 (debug=False)
[4.0] OK: initializing VideoPlayer
[4.0] OK: VideoPlayer.print_video() declaration
[4.0] OK: VideoPlayer.play_file() declaration
[4.0] OK: VideoPlayer.play_video() declaration
--------------------------------------------
[4.1] OK: (expected) when playing non existent video
--------------------------------------------
[4.2] OK: (expected) when print_video() with fake UUID
--------------------------------------------
[4.3] OK: (expected) when play_file() with fake filepath
--------------------------------------------
[4.4] OK: playing all videos (175 elements)
--------------------------------------------
Partial Grade: 55
============================================
--------------------------------------------
Test: PlayList (Func5)
--------------------------------------------
Test: Func5 (debug=False)
[5.0] OK: initializing PlayList
[5.0] OK: PlayList.load_file() declaration
[5.0] OK: PlayList.play() declaration
[5.0] OK: PlayList.add_video_at_end() declaration
[5.0] OK: PlayList.remove_first_video() declaration
[5.0] OK: PlayList.remove_last_video() declaration
--------------------------------------------
[5.1] OK: empty Playlist
[5.1] OK: (expected) when playing an empty PlayList
--------------------------------------------
[5.2] OK: not loading fake M3U files
--------------------------------------------
[5.3] FAIL: loading 0 videos (from M3U file: /home/p11914/tmpcorpus/jetsetters.m3u )
--------------------------------------------
[5.4] FAIL: reloading 0 videos (from M3U file: /home/p11914/tmpcorpus/jetsetters.m3u )
--------------------------------------------
[5.5] FAIL: adding 0 videos (from M3U file: /home/p11914/tmpcorpus/total.m3u )
[5.5] FAIL: adding 0 videos (from M3U file: /home/p11914/tmpcorpus/mix-other.m3u )
--------------------------------------------
[5.6] OK: (expected) when playing the PlayList
--------------------------------------------
Partial Grade: 67
============================================
--------------------------------------------
Test: SearchMetadata (Func6)
--------------------------------------------
Test: Func6 (debug=False)
[6.0] OK: initializing SearchMetadata
[6.0] OK: SearchMetadata.duration() declaration
[6.0] OK: SearchMetadata.title() declaration
[6.0] OK: SearchMetadata.album() declaration
[6.0] OK: SearchMetadata.artist() declaration
[6.0] OK: SearchMetadata.composer() declaration
[6.0] OK: SearchMetadata.genre() declaration
[6.0] OK: SearchMetadata.date() declaration
[6.0] OK: SearchMetadata.comment() declaration
[6.0] OK: SearchMetadata.and_operator() declaration
[6.0] OK: SearchMetadata.or_operator() declaration
--------------------------------------------
[6.1] OK: search A returns 0 elements
--------------------------------------------
[6.2] FAIL: search B returns (0,0,0,0) elements
--------------------------------------------
[6.3] OK: search C returns (0,0,2,0) elements
--------------------------------------------
[6.4] OK: operations OR:2 OR:2 AND:2 elements
--------------------------------------------
[6.5] OK: complex search return correct element
--------------------------------------------
Partial Grade: 80
============================================
--------------------------------------------
Test: PlayList (Func7)
--------------------------------------------
Test: Func7 (debug=False)
[7.0] FAIL: Playlist is not empty
--------------------------------------------
[7.1] OK not loading fake M3U files
[7.1] OK: non existent M3U generates empty Playlist
--------------------------------------------
[7.2] FAIL: adding repeated videos in a PlayList
--------------------------------------------
[7.3] OK: deleting/consuming videos from a PlayList
--------------------------------------------
[7.4] OK: deleting/consuming videos from an empty PlayList
--------------------------------------------
[7.5] OK: last complex search 1 elements
[7:5] OK: last complex search found correct 1 elements
--------------------------------------------
[7.6] OK (expected) when playing the PlayList of the Search
--------------------------------------------
Partial Grade: 97
============================================
--------------------------------------------
Iteradors i Helpers (Func2.1)
--------------------------------------------
Test: Func21 (debug=False)
[21.0] OK: initializing GrafHash
[21.0] OK: initializing ElementData
--------------------------------------------
[21.1] EXCEPTION: [AttributeError] - Comprovem __repr__() amb les classes rellevants
--------------------------------------------
[21.2] EXCEPTION: [AttributeError] - Comprovem __len__() amb les classes rellevants
--------------------------------------------
[21.3] EXCEPTION: [AttributeError] - Comprovem __iter__() amb les classes rellevants
--------------------------------------------
[21.4] OK: (ElementData.__hash__() all checks consistent
--------------------------------------------
[21.5] OK: ElementData.__eq__(A)
[21.5] OK: ElementData.__eq__(B)
[21.5] OK: ElementData.__eq__(copy(A))
[21.5] OK: ElementData.__ne__(A)
[21.5] OK: ElementData.__ne__(B)
[21.5] OK: ElementData.copy(A).__ne__(B)
[21.5] FAIL: ElementData.__lt__(A)
[21.5] FAIL: ElementData.__lt__(A,B)
--------------------------------------------
Partial Grade: 101
============================================
--------------------------------------------
Constructors i Extensions (Func2.2)
--------------------------------------------
Test: Func22 (debug=False)
--------------------------------------------
[22.1] EXCEPTION: [TypeError] - Comprovem __init__() de VideoPlayer, que ha de retornar NotImplementedError si no es pot instanciar
--------------------------------------------
[22.2] EXCEPTION: [TypeError] - Comprovem __init__() de SearchMetadata, que ha de retornar NotImplementedError si no es pot instanciar
--------------------------------------------
[22.3] EXCEPTION: [TypeError] - Comprovem __init__() de PlayList, que ha de retornar NotImplementedError si no es pot instanciar
--------------------------------------------
[22.4] EXCEPTION: [AttributeError] - Comprovem ús de __slots__ en totes les classes i que són privats
--------------------------------------------
[22.5] OK: get_filename(fake_UUID) returns None
[22.5] OK: get_filename(UUID) returns a valid MP4 file
--------------------------------------------
[22.6] OK: get_duration(fake_UUID) returns less than 0
[22.6] OK: get_filename(UUID) returns greater than 0
--------------------------------------------
Partial Grade: 105
============================================
--------------------------------------------
class GrafHash/ElementData (Func2.3)
--------------------------------------------
Test: Func23 (debug=False)
--------------------------------------------
[23.1] FAIL: ElementData setters
[23.1] EXCEPTION: [AttributeError] - Comprovem els atributs d'ElementData
--------------------------------------------
[23.2] OK: ElementData equality
[23.2] OK: ElementData inequality
[23.2] EXCEPTION: [TypeError] - Comprovem les funcions d'ElementData
--------------------------------------------
[23.3] OK: GrafHash insert_vertex()
[23.3] FAIL: GrafHash insert_vertex(k,obj) not fails without Element
[23.3] OK: GrafHash insert_vertex(k,e)
[23.3] OK: GrafHash insert_vertex(k,e) with duplicate Key
[23.3] OK: GrafHash insert_vertex(k,e) with duplicate Element
--------------------------------------------
[23.4] OK: GrafHash __contains__ check Key
[23.4] OK: GrafHash __contains__ check unknown Key
[23.4] FAIL: GrafHash __getitem__ with correct Key
[23.4] EXCEPTION: [KeyError] - ...
[23.4] FAIL: GrafHash __getitem__ with incorrect Key
[23.4] OK: GrafHash __delitem__ with correct Key
[23.4] OK: GrafHash deleted Key
[23.4] FAIL: GrafHash Iteration result
--------------------------------------------
[23.5] OK: GrafHash insert_edge()
[23.5] OK: GrafHash insert_edge(k1,k2)
[23.5] OK: GrafHash insert_edge(k1,k2) in previous edges
[23.5] EXCEPTION: [AttributeError] - ...
[23.5] FAIL: GrafHash edges_out() result
[23.5] EXCEPTION: [AttributeError] - ...
[23.5] FAIL: GrafHash edges_in() result
[23.5] EXCEPTION: [AttributeError] - ...
[23.5] FAIL: GrafHash grauPesOut() result
[23.5] EXCEPTION: [AttributeError] - ...
[23.5] FAIL: GrafHash grauPesIn() result
--------------------------------------------
[23.6] OK: GrafHash camiMesCurt() result
--------------------------------------------
Partial Grade: 119
============================================
--------------------------------------------
Xarxa de llistes de videos (Func2.5)
--------------------------------------------
Test: Func25 (debug=False)
--------------------------------------------
[25.1] FAIL: PlayList load_file()
--------------------------------------------
[25.2] OK: VideoData read_playlist()
--------------------------------------------
[25.3] FAIL: PlayList read_list()
--------------------------------------------
[25.4] OK: VideoData read_playlist()
--------------------------------------------
Partial Grade: 123
============================================
--------------------------------------------
Reimplementació VideoData (Func2.4)
--------------------------------------------
Test: Func24 (debug=False)
[24.0] EXCEPTION: [IndexError] - Selecció d'alguns videos de dins la col·lecció
--------------------------------------------
[24.1] EXCEPTION: [IndexError] - Comprovem la funció VideoData.get_video_rank()
--------------------------------------------
[24.2] EXCEPTION: [IndexError] - Comprovem la funció VideoData.get_next_videos()
--------------------------------------------
[24.3] EXCEPTION: [IndexError] - Comprovem la funció VideoData.get_previous_videos()
--------------------------------------------
[24.4] EXCEPTION: [IndexError] - Comprovem la funció VideoData.get_video_distance()
--------------------------------------------
[24.5] EXCEPTION: [IndexError] - Esborrar videos amb arestes
--------------------------------------------
Partial Grade: 123
============================================
--------------------------------------------
Generar playlist automàtiques (Func2.6)
--------------------------------------------
Test: Func26 (debug=False)
--------------------------------------------
[26.1] EXCEPTION: [TypeError] - Fer un càlcul dels videos similars
--------------------------------------------
[26.2] DEBUG - Results get_auto_play(0):
[26.2] EXCEPTION: [TypeError] - Fer el càlcul per generar una seqüència de 8 de la col·lecció
--------------------------------------------
Partial Grade: 123
============================================
--------------------------------------------
--: Final del Test amb errors.
--------------------------------------------
Grade Final: 123 sobre 260"""








"""Test: VideoData (Func3)
--------------------------------------------
Test: Func3 (debug=False)
[3.0] OK: initializing VideoData (0 elements)
[3.0] OK: VideoData.add_video() declaration
[3.0] EXCEPTION: [KeyError] - Comprovar la instanciació i la interficie de funcions
--------------------------------------------
[3.1] OK: with empty VideoData class
--------------------------------------------
[3.2] EXCEPTION: [AttributeError] - Insereix un video fictici i intenta llegir les serves metadades
--------------------------------------------
[3.3] FAIL: adding fake videos
--------------------------------------------
[3.4] EXCEPTION: [KeyError] - Esborra (dues vegades) el video existent anterior
--------------------------------------------
[3.5] FAIL: testing adding all videos
--------------------------------------------
[3.6] EXCEPTION: [AttributeError] - Intenta retornar metadades abans de llegir-les
--------------------------------------------
[3.7] EXCEPTION: [AttributeError] - Llegeix les metadades de tots els videos i recupera després els valors
--------------------------------------------
[3.8] EXCEPTION: [AttributeError] - Comprovació manual d'algunes metadades"""




def main():
    
    root = "/Users/aliciamartilopez/Desktop/pED_2"
    
    print(" VideoFiles (Func1) ")
    obj_video_files = VideoFiles.VideoFiles()
    #print(len(obj_video_files))
    obj_video_files.reload_fs(root) 
    #print(len(obj_video_files.files_added()))
    #print(obj_video_files.files_removed())
    print(len(obj_video_files))
    #for el in obj_video_files:
     #   print(el)
    
    
    
    
    
    
    print(" VideoID (Func2) ")
    obj_video_id = VideoID.VideoID()
    for file in obj_video_files:
        obj_video_id.generate_uuid(file)
    print(len(obj_video_id))
    #for i in obj_video_id:
     #   print(i)
    
    
    
    
    

    
    print(" VideoData (Func3) ")
    obj_video_data = VideoData.VideoData()
    uuid_fictici = "aaaaaaddddddd77770000"
    file_fictici = "el_video_fictici_08500"
    #uuid = "6f2a934c-e44c-5f72-9d25-b5f96a349fe5"
    #file = "/Users/aliciamartilopez/Desktop/pED_2/Videos/Beyond/900-2_901-6159-PD2.mp4"
    #obj_video_data.add_video(uuid, file)
    #obj_video_data.load_metadata(uuid)
    #obj_video_data.remove_video(uuid_fictici) 
    #obj_video_data.add_video(uuid_fictici, file_fictici)
    #obj_video_data.load_metadata(uuid_fictici)
    #uuid = "6f2a934c-e44c-5f72-9d25-b5f96a349fe5"
    #file = "/Users/aliciamartilopez/Desktop/pED_2/Videos/Beyond/900-2_900-6159-PD2.mp4"
    #obj_video_data.load_metadata(uuid)
    #obj_video_data.add_video(uuid, file)
    #print(obj_video_data.get_duration(uuid_fictici))
    #print(obj_video_data.get_duration(uuid))
    #print(obj_video_data.get_title(uuid))
    #print(obj_video_data.get_album(uuid))
    #print(obj_video_data.get_artist(uuid))
    #print(obj_video_data.get_composer(uuid))
    #print(obj_video_data.get_genre(uuid))
    #print(obj_video_data.get_date(uuid))
    #print(obj_video_data.get_comment(uuid))
    #obj_video_data.load_metadata(uuid)
    #print(obj_video_data.get_duration(uuid))
    #print(obj_video_data.get_title(uuid))
    #print(obj_video_data.get_album(uuid))
    #print(obj_video_data.get_artist(uuid))
    #print(obj_video_data.get_composer(uuid))
    #print(obj_video_data.get_genre(uuid))
    #print(obj_video_data.get_date(uuid))
    #print(obj_video_data.get_comment(uuid))
    #print('\n')
    #for i in obj_video_data:
    #    print(i)
    for file, uuid in obj_video_id:
        obj_video_data.add_video(uuid, file)
        obj_video_data.load_metadata(uuid)
    #print('intenta tornar les metadades abans de llegir-les')
    #for file, uuid in obj_video_id:
        #print(obj_video_data.get_artist(uuid))
        
    
#    print(len(obj_video_data))
 #   uuid = '6f2a934c-e44c-5f72-9d25-b5f96a349fe5'
  #  print(obj_video_data.get_duration(uuid))
   # print(obj_video_data.get_title(uuid))
    #print(obj_video_data.get_album(uuid))
#    print(obj_video_data.get_artist(uuid))
 #   print(obj_video_data.get_composer(uuid))
  #  print(obj_video_data.get_genre(uuid))
   # print(obj_video_data.get_date(uuid))
    #print(obj_video_data.get_comment(uuid))
    
    print(" VideoPlayer (Func4) ")
    obj_video_player = VideoPlayer.VideoPlayer(obj_video_data)
    obj_video_player.play_video('13c51838-92d0-5927-9f13-0908348fa22d', 0)
    
    
    
    
    
    
    print(" PlayList (Func5) ")
    PlayListu = PlayList.PlayList(obj_video_id, obj_video_player)
    playlist_cas_general = PlayList.PlayList(obj_video_id, obj_video_player)
    #playlist_amb_arxius_inexistents = PlayList.PlayList(obj_video_id, obj_video_player)
    playlist_buida = PlayList.PlayList(obj_video_id, obj_video_player)
    #playlist_amb_arxius_q_no_estan_a_la_col_leccio = PlayList.PlayList(obj_video_id, obj_video_player)
    
    #print(len(playlist_amb_arxius_q_no_estan_a_la_col_leccio))
    file_general = '/Users/aliciamartilopez/Desktop/pED_2/cas_general_4_elements.m3u'
    #file_amb_inexistent = '/Users/aliciamartilopez/Desktop/pED_2/amb_fitxer_inexistent.m3u'
    file_buit = '/Users/aliciamartilopez/Desktop/pED_2/buida.m3u'
    #file_amb_no_col_leccio = '/Users/aliciamartilopez/Desktop/pED_2/un_q_no_esta_a_col_leccio.m3u'
    #file2 = '/Users/aliciamartilopez/Desktop/pED_2/carpeta_2_m3us'
    playlist_cas_general.load_file(file_general)
    #playlist_amb_arxius_inexistents.load_file(file_amb_inexistent)
    playlist_buida.load_file(file_buit)
    #playlist_amb_arxius_q_no_estan_a_la_col_leccio.load_file(file_amb_no_col_leccio)
    
    
    print(playlist_cas_general)
    print(len(playlist_cas_general))
    
    print(playlist_buida)
    print(len(playlist_buida))
    
    playlist_cas_general.load_file(file_general)
    print(playlist_cas_general)
    print(len(playlist_cas_general))
    #print(playlist_amb_arxius_inexistents)
    #print(len(playlist_amb_arxius_inexistents))
    
    #print(playlist_buida)
    #print(len(playlist_buida))
    
    #print(playlist_amb_arxius_q_no_estan_a_la_col_leccio)
    #print(len(playlist_amb_arxius_q_no_estan_a_la_col_leccio))
    
    #for file in obj_video_data:
     #   uuid = obj_video_id.get_uuid(file)
      #  PlayListu.add_video_at_end(uuid)
    
    #print(len(PlayListu))
    
    #obj_video_data.read_playlist(PlayListu)
    
    
    
    
    
    
    
    
    
    
    """print(" SearchMetadata (Func6) ")
    obj_search_metadata = SearchMetadata.SearchMetadata(obj_video_data)
    #playlist_buisness = obj_search_metadata.genre('business')
    #print(len(playlist_buisness))
    #obj_video_data.read_playlist(playlist_buisness)
    playlist_similar = obj_search_metadata.get_similar('268605d5-63b0-5f50-9189-bdf4cc0a988b', 4)
    print(len(playlist_similar))
    print(playlist_similar)"""
    

main()