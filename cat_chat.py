# connect to dropbox account using auth_token
import dropbox
import subprocess
from dropbox.client import DropboxOAuth2Flow, DropboxClient
# import hash_cat
from cryptography.fernet import Fernet

auth_token = 'put auth token here'
storedToken = ''
key = ''
saveFile = 'token.txt'

# TODO use oath instead of hashing and encrypting
def main():

    # TODO ask for the user to enter a new token, or use the one already stored
    choice = input("Use stored token? Answer \"y\" or \"n\"\n")
    choice = choice.lower()

    while choice != "n" and choice != "y":
        choice = input("Use stored token? Answer \"y\" or \"n\"\n")
        choice = choice.lower()

    # TODO create a new token and store it safely
    if choice == "n":
        token = input("Enter new token - make sure to wrap in quotes\n")

        # generate the key
        key = Fernet.generate_key();
        cipher_suite = Fernet(key);

        # encrypt the input
        cipher_text = cipher_suite.encrypt(token)

        # save key and encrypted token to backup file
        backup = open(saveFile, 'wb')
        backup.write(key)
        backup.write('\n')
        backup.write(cipher_text)
        backup.write('\n')


        # run the token through the hash function
        # storedToken = hash_cat.encrypt_token(key, token)

    # else:
        # TODO check if there is a stored token, otherwise prompt the user for a new token
        # client = DropboxClient(hash_cat.unencrypt_token(key, storedToken))


    # print hash_cat.unencrypt_token(key, storedToken)
    # client = DropboxClient(hash_cat.unencrypt_token(key, storedToken))
    client = DropboxClient(auth_token)

    # print 'linked account: ', client.account_info() 

# see if there are any new .mp3 files
    possible_file = client.metadata('/new')

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
            print path
            new_path = path[4:]
            # TODO add date to path name
            new_path = '/save/' + new_path
            print new_path
            client.file_move(path, new_path)

            i+=1
    else:
        print 'nothing here'




if __name__ == '__main__':
    main()