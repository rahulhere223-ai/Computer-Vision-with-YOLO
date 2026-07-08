from ultralytics import YOLO
import cv2

image=cv2.imread("bus.jpg")
model=YOLO("yolov8n.pt")

results=model(image)

for result in results:
    names=result.names
    print(names)

    for box in result.boxes:
        class_id=int(box.cls)
        confidence_score=float(box.conf)

        x1,y1,x2,y2=map(int,box.xyxy[0])
        if names[class_id] == 'person':
         cv2.rectangle(image,(x1,y1),(x2,y2),(255,0,0),2)
         cv2.putText(image,f'{names[class_id]} {confidence_score}',(x1,y1-10),cv2.FONT_HERSHEY_SIMPLEX,0.6,(255,0,0),2)
        elif names[class_id] == 'bus':
         cv2.rectangle(image,(x1,y1),(x2,y2),(0,255,0),2)
         cv2.putText(image,f'{names[class_id]} {confidence_score}',(x1,y1-10),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,255,0),2)
        elif names[class_id] == 'stop sign':
         cv2.rectangle(image,(x1,y1),(x2,y2),(0,0,255),2)
         cv2.putText(image,f'{names[class_id]} {confidence_score}',(x1,y1-10),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,0,255),2) 


cv2.imwrite("Colored_Detection.jpg",image)
cv2.imshow("Object Detection",image)
cv2.waitKey(0)
cv2.destroyAllWindows()

