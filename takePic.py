import cv2

def takeShot():

    videCaptureObj = cv2.VideoCapture(0)
    result = True

    while(result):
        ret,frame = videCaptureObj.read()
        print(ret)

        cv2.imwrite("pic1.jpg",frame)
        result = False

    videCaptureObj.release()
    cv2.destroyAllWindows()

takeShot()