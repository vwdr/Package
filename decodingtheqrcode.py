import numpy as np
from pyzbar.pyzbar import decode
import cv2

vid = cv2.VideoCapture(0)
vid.set(3, 640)
vid.set(4, 740)

while True:
  success, img = vid.read()
  for barcode in decode(img):
    text = barcode.data.decode('utf-8')
    print(text) 
    polygon_Points = np.array([barcode.polygon], np.int32)
    polygon_Points=polygon_Points.reshape(-1,1,2)
    rect_Points= barcode.rect
    cv2.polylines(img,[polygon_Points],True,(255,255, 0), 5)
    cv2.putText(img, text, (rect_Points[0],rect_Points[1]), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255,255, 0), 2)
  cv2.imshow("Video", img)
  cv2.waitKey(1)
