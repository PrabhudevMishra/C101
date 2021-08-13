#to import the dropbox module
from os import access
import dropbox

#create a class called TransferData
class TrasnferData:
    #create a function called __init__
    def __init__(self,access_token):
        self.access_token = access_token

    #create a function called upload_files
    def uploadFiles(self,file_from,file_to):
        
        #upload a file in the dropbox --> dropbox.Dropbox()
        dbx = dropbox.Dropbox(self.access_token)

        #to open the file to be uploaded using with open()
        with open(file_from, 'rb') as f:

            #to upload the files --> files_upload()
            dbx.files_upload(f.read(),file_to)

#create a fnction  called main()
def main():
    access_token = 'Bzb7t9pBPbMAAAAAAAAAAR2lAq1TeJG9tSfG4cJEQDtc7VdYJ4SN3hSV6J7DkHVS'
    transferData = TrasnferData(access_token)

    file_from = input("Enter the file name to transfer: ")
    file_to = input("Enter the path of the file to be transfered: ")

    transferData.uploadFiles(file_from, file_to)

if __name__ == '__main__':
    main()



