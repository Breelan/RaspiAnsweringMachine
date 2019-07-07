import os
import subprocess
import time
import io
#also requires use of Dropbox-Uploader, which must be downloaded

def main():
    possible_file_command = "/home/pi/RaspiAnsweringMachine/Dropbox-Uploader/dropbox_uploader.sh list /new > out.txt"

    #save the list to file called out.txt
    subprocess.call(possible_file_command, shell=True)

    #TODO open the file, parse through the list, download each file one by one, play it, then move to the next one
    with open('out.txt', 'r') as file_object:

        #skip to the files
        line = file_object.readline()
        line = file_object.readline()

        while line:

            filename = line[13:].strip()
            print(filename)
            download_command = "/home/pi/RaspiAnsweringMachine/Dropbox-Uploader/dropbox_uploader.sh download /new/" + filename + ""
            subprocess.call(download_command, shell=True)

            music_command = "mpg123 /home/pi/RaspiAnsweringMachine/" + filename + ""
            subprocess.call(music_command, shell=True)

            #TODO move file to save folder in dropbox and delete locally
            
            line = file_object.readline()

        #TODO don't forget to close file_object


    #################################################################################################################
    #####start of old way, with problem of file playing getting interrupted by moving the file to a new location#####
    '''
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

    #the following is required to use omxplayer to play files though speakers
    #music_command = "omxplayer -o local "
    '''
if __name__ == '__main__':
    main()
