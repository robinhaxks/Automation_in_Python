import os
from mutagen.easyid3 import EasyID3
from mutagen.flac import FLAC
import shutil

# Specify the path to the directory containing the music files
path = ""

# Loop through all the files in the directory
for filename in os.listdir(path):
    print(filename)
    # Check if the file is an MP3 file
    if filename.endswith(".mp3"):
        # Load the metadata of the file
        filepath = os.path.join(path, filename)
        audio = EasyID3(filepath)
        # Get the album and music director information from the metadata
        print("Album: ",audio["album"][0])
        print("Music Director: ",audio["composer"][0])
        if os.path.exists(path+"/"+audio["album"][0]):
            shutil.move(path+'/'+filename,path+'/'+audio["album"][0]+'/'+filename)
        else:
            os.makedirs(path+"/"+audio["album"][0])
            shutil.move(path+'/'+filename,path+'/'+audio["album"][0]+'/'+filename)
        


        
    # Check if the file is a FLAC file
    elif filename.endswith(".flac"):
        # Load the metadata of the file
        filepath = os.path.join(path, filename)
        audio = FLAC(filepath)
        # Get the album and music director information from the metadata
        print("Album: ",audio["album"][0])
        print("Music Director: ",audio["artist"][0])
        print("--"*20)
        if os.path.exists(path+"/"+audio["album"][0]):
            shutil.move(path+'/'+filename,path+'/'+audio["album"][0]+'/'+filename)
        else:
            os.makedirs(path+"/"+audio["album"][0])
            shutil.move(path+'/'+filename,path+'/'+audio["album"][0]+'/'+filename)
