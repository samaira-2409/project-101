import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)


        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BKlLps5pr4TcwhJ_hX2tD30nSRDM0hcE_S7yCU0_D7C501It2dR92syA2JR-5rS3iz2Dw6wiZh82yI7wtfzly5-WzTIkUwlf9m7ayxiV7FN8Pxg81MlSlDMfS5hbFRUaTNR4oo9Dfy7b'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer : -")
    file_to = input("enter the full path to upload to dropbox:- ")  # This is the full path to upload the file to, including name that you wish the file to be called once uploaded.

    # API v2
    transferData.upload_file(file_from, file_to)
    print("file has been moved !!!")


main()