import cv2
import numpy as np
from PIL import Image
import json
import _pickle as cPickle
import codecs

class Camera:
    def __init__(self, width, height, json=True):
        self.json = json
        try:
            self.cap = cv2.VideoCapture(0)
        except cv2.error as e:
            print(e, " can not capture camera0.")
        except:
            print("unknown error.")
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        
    def takePicture(self):
        ret, frame = self.cap.read()
        if ret == True :
            # opencv read result is np.array format, PIL is PIL.Image format
            if self.json == True :
                dic = {}
                bytesImg = cPickle.dumps(frame)
                strImg = s = str(bytesImg)[2:-1]
                dic["default"] = strImg
                dicJson = json.dumps(dic)
                return dicJson
            return frame
        return None
    
    def releaseCam(self):
        self.cap.release()

if __name__ == "__main__":
    cam = Camera(384, 192, False)
    img = cam.takePicture()
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cam.releaseCam()
        