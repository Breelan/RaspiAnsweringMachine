"""
This program is meant to run as a cron job that will scrape your dropbox folder for 
any mp3 files you've placed in there, play them from the command line, and move them 
to a different folder when it's done. Set it to run as often as you like in your crontab.

Author: Breelan Lubers
"""

# use dropbox_uploader
import time
import subprocess
#import dropbox
#from dropbox.client import DropboxOAuth2Flow, DropboxClient

#saveFile = 'token.txt'


# TODO make this cron job-able!
def main():

    ## ask for the user to enter their token
    #auth_token = raw_input("Please enter your Dropbox auth token: ")

    #client = DropboxClient(auth_token)

# see if there are any new .mp3 files
# currently the program sleeps for 5 minutes between checks - change it
# however you like
    while True:

        time.sleep(5 * 60)

        #possible_file = client.metadata('/new')
	possible_file_command = "/home/pi/RaspiAnsweringMachine/Dropbox-Uploader/dropbox_uploader.sh download 

        # check for errors
        contents = possible_file.get('contents')

        files = len(contents)

        if files > 0:
            print 'something here'
            i = 0
            while i < files: 
                path = contents[i].get('path')
                # print path

                # get the file
                file, metadata = client.get_file_and_metadata(path)

                # transfer the file to local
                out = open('voice.mp3', 'wb')
                out.write(file.read())
                out.close()


                # execute a bash command using mpg123 to play the .mp3
                subprocess.call("mpg123 ./voice.mp3", shell=True)

                # move the file to the save folder
                # old_path = './new/' + path
                # print old_path
                # print path
                new_path = path[4:]
                # TODO add date to path name
                new_path = '/save/' + new_path
                # print new_path
                print "moving from " + path + " to " + new_path
                client.file_move(path, new_path)

                i+=1
        else:
            print 'nothing here'


if __name__ == '__main__':
    main()
