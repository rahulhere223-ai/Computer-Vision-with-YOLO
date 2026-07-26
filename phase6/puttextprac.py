from ultralytics import YOLO
import cv2

image=cv2.imread("bus.jpg")

cv2.rectangle(image,(10,10),(450,60),(0,0,0),-1)
cv2.putText(image,"Rahul learning YOLO",(20,40),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)

cv2.imshow("putting text on image",image)

cv2.waitKey(0)
cv2.destroyAllWindows()


