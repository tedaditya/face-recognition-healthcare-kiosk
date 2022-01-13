import cv2
import os

cam = cv2.VideoCapture("E:\Work\Kuliah\TEKNIK KOMPUTER 2018\TA\TA Alvian Tedy Aditya\Healthcare Kiosk\Dataset\Video\WhatsApp Video 2021-12-23 at 23.22.19.mp4")

try:
    
    # creating a folder named data
    if not os.path.exists('data'):
        os.makedirs('data')

# if not created then raise error
except OSError:
    print ('Error: Creating directory of data')

# frame
currentframe = 0

while(True):
    
    # reading from frame
    ret,frame = cam.read()

    if ret:
        # if video is still left continue creating images
        name = './data/frame_' + str(currentframe) + '.jpg'
        print ('Creating...' + name)

        # writing the extracted images
        cv2.imwrite(name, frame)

        # increasing counter so that it will
        # show how many frames are created
        currentframe += 1
    else:
        break

# Release all space and windows once done
cam.release()
cv2.destroyAllWindows()