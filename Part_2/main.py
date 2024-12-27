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
    uuid = "6f2a934c-e44c-5f72-9d25-b5f96a349fe5"
    file = "/Users/aliciamartilopez/Desktop/pED_2/Videos/Beyond/900-2_901-6159-PD2.mp4"
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
    #for uuid in obj_video_data:
    #    print(obj_video_data.get_artist(uuid))
        
    
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
    
    print(" PlayList (Func5) ")
    playlist_1 = PlayList.PlayList(obj_video_id, obj_video_player)
    file = '/Users/aliciamartilopez/Desktop/pED_2/family_meal.m3u'
    #file2 = '/Users/aliciamartilopez/Desktop/pED_2/carpeta_2_m3us'
    playlist_1.load_file(file)
    playlist_2 = PlayList.PlayList(obj_video_id, obj_video_player)
    playlist_2.load_file(file)
    print(len(playlist_1))
    
    print(" SearchMetadata (Func6) ")
    obj_search_metadata = SearchMetadata.SearchMetadata(obj_video_data)
    playlist_and = obj_search_metadata.and_operator(str(playlist_1), str(playlist_2))
    playlist_buisness = obj_search_metadata.genre('business')
    print(len(playlist_buisness))
    obj_video_data.read_playlist(playlist_buisness)
    
    
    obj_ElementData = ElementData.ElementData()
    
    
    
    
    
    

main()



