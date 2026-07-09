import cv2
from ultralytics import YOLO

model =YOLO("yolov8n.pt")

video=cv2.VideoCapture("video.mp4")
frame_count=1

while True:
    success,frame=video.read()

    if not success:
        break

    frame=cv2.resize(frame,(640,360))

    results=model(frame,verbose=False)

    for result in results:
        names=result.names
        print(f'Frame : {frame_count} ---------------')
        car_count=0
        truck_count=0
        person_count=0
        
        for box in result.boxes:

            class_id=int(box.cls)
            confidence=float(box.conf)

            if names[class_id] == 'car':
                car_count +=1
            elif names[class_id] == 'person':
                person_count+=1
            elif names[class_id] == 'truck':
                truck_count+=1        

        print(f'Detected : car {car_count}') 
        print(f'truck {truck_count}') 
        print(f'person {person_count}')                

    annotated_frame=results[0].plot()

    cv2.imshow("YOLO video detection",annotated_frame)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        print("Quitting...")
        break
    frame_count +=1

video.release()
cv2.destroyAllWindows()