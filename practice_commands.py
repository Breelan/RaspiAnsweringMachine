import os
import subprocess
import time
#also requires use of Dropbox-Uploader, which must be downloaded

def main():
    possible_file_command = "/home/pi/RaspiAnsweringMachine/Dropbox-Uploader/dropbox_uploader.sh list /new"

    #try to save the list to a var
    #mp3_list = subprocess.call(possible_file_command, shell=True)
    #print(mp3_list)

    #download everything into a local folder
    download_command = "/home/pi/RaspiAnsweringMachine/Dropbox-Uploader/dropbox_uploader.sh download /new"
    subprocess.call(download_command, shell=True)

    #mp3_list = subprocess.call(possible_file_command, shell=True)
    #print(mp3_list)

    #for each file in the /new directory, play it then move it to a save folder
    #note -- make sure the file name doesn't have any spaces in it
    for root, dirs, files in os.walk("./new", topdown=True):
        for name in files:
            #music_command = "omxplayer --adev hdmi /home/pi/RaspiAnsweringMachine/new/" + name
            music_command = "mpg123 ./new/" + name
            #subprocess.call("mpg123 ./voice.mp3", shell=True)
            subprocess.call(music_command, shell=True)
            #TODO get the length of the file and sleep for that amount of time
            #time.sleep()

    #wait until all the files have played before moving them around in dropbox
    for root, dirs, files in os.walk("./new", topdown=True):
        for name in files:        
            move_command = "/home/pi/RaspiAnsweringMachine/Dropbox-Uploader/dropbox_uploader.sh move /new/" + name + " /save"
            subprocess.call(move_command, shell=True)
            #delete the file from the /new folder

    
    #music_command = "omxplayer -o local "

if __name__ == '__main__':
    main()
