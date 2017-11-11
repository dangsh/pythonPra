from PIL import Image , ImageGrab
import socket 
import threading , time
import VideoCapture


cam = VideoCapture.Device(devnum=0)
s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)

def getImages():
    while True:
        # image = ImageGrab.grab()
        image = cam.getImage()
        image = image.resize((160 , 120))
        

        data = image.tobytes()

        s.sendto(data , ("127.0.0.1" , 7777))




t= threading.Thread(target=getImages);
t.start()


while True:
    pass

s.close()