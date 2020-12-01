import time
import random
import cv2
import dropbox

startTime = time.time()

def capture():
    number = random.randint(0,100)
    videoCaptureObj = cv2.VideoCapture(0)
    result = True

    while(result):
        ret,frame = videoCaptureObj.read()
        imageName = "img" + str(number) + ".png"

        cv2.imwrite(imageName,frame)
        startTime = time.time
        result = False

    return imageName
    print("Snapshot Taken!")

    videoCaptureObj.release()
    cv2.destroyAllWindows()

def uploadFile(imageName):
    access_token = "xwdVff57ad8AAAAAAAAAAfl3GJO0iqLwyKuk6wvEOClCvrN1GPIxa4uLVNr_PmdH"
    file = imageName
    file_from = file
    file_to = "/C102/" + (imageName)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(), file_to, mode=dropbox.files.WriteMode.overwrite)
        print("File Uploaded!")

def main():
    while(True):
        if((time.time()-startTime)>=5):
            name = capture()
            uploadFile(name)

main()