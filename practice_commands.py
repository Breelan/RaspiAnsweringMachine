import os
import subprocess
import time
import io
#also requires use of Dropbox-Uploader, which must be downloaded

def main():

    #check if anything is in the dropbox and save the list to out.txt
    subprocess.call("/home/pi/RaspiAnsweringMachine/Dropbox-Uploader/dropbox_uploader.sh list /new > out.txt", shell=True)

    #open the file, parse through the list, download each file one by one, play it, then move to the next one
    with open('out.txt', 'r') as file_object:

        #skip to the files
        line = file_object.readline()
        line = file_object.readline()

        while line:
            #skip first three spaces, then take the rest of the string as the filename
            spaces = 0
            file_start = 0
            for char in line:
                file_start +=1
                if char == " ":
                    spaces +=1

                if spaces == 3:
                    break
            
            filename = line[file_start:].strip()

            download_command = "/home/pi/RaspiAnsweringMachine/Dropbox-Uploader/dropbox_uploader.sh download /new/" + filename
            subprocess.call(download_command, shell=True)

            music_command = "mpg123 /home/pi/RaspiAnsweringMachine/" + filename
            subprocess.call(music_command, shell=True)

            #move file to save folder in dropbox and delete locally - can we do it with sudo? what about without?
            move_command = "sudo mv " + filename + " ./old_files"
            subprocess.call(move_command, shell=True)

            delete_command = "/home/pi/RaspiAnsweringMachine/Dropbox-Uploader/dropbox_uploader.sh delete /new/" + filename
            subprocess.call(delete_command, shell=True)
            
            line = file_object.readline()

        #don't forget to close file_object
        file_object.close()

if __name__ == '__main__':
    main()
