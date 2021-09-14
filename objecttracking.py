import numpy as np
import cv2
import keyboard
import threading

def resize(img):
        return cv2.resize(img,(1200,800)) # arg1- input image, arg- output_width, output_height

cap=cv2.VideoCapture("teste.mp4")
cap.set(cv2.CAP_PROP_BUFFERSIZE, 3)
ret,frame=cap.read()
object_detector = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=40)

def open_video():
        while True:
            ret,frame=cap.read()    
            mask = object_detector.apply(frame)
            _, mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)
            contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            i = 0
            for cnt in contours:
                # Calculate area and remove small elements
                area = cv2.contourArea(cnt)
                x, y, w, h = cv2.boundingRect(cnt)
                if area > 1500:
                #Show image
                    text = ("ID {}").format(cnt)
                    cv2.putText(frame, "ID {}".format(i), (x - 25, y - 25),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
                    cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0 ), 3)
                    i = i+1
            key=cv2.waitKey(1)
            cv2.imshow('FG Mask', resize(frame))
            if keyboard.is_pressed('q'):
                break
        cv2.waitKey(0)
        cv2.destroyAllWindows()

def start_thread():
        tred = threading.Thread(target=open_video).start()
        

start_thread()
