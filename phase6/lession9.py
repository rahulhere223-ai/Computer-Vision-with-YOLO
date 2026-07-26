import cv2
from ultralytics import YOLO

model=YOLO("yolov8n.pt")

video=cv2.VideoCapture("video5.mp4")
unique_vehicle=set()
frame_count=1

while True:
    success,frame=video.read()

    if not success:
        break

    frame=cv2.resize(frame,(640,360))

    results=model.track(frame,persist=True,verbose=False)

    for result in results:
        name=result.names

        for box in result.boxes:
            class_id=int(box.cls)
            object_name=name[class_id]

            if box.id is not None and object_name in {"car","truck","bus"}:
                track_id=int(box.id)
                unique_vehicle.add(track_id)

        print(f'frame count {frame_count}')
        print(f'Number of uniquevehicle is {len(unique_vehicle)}')
        print("="*30)
        print("\n")        
    
    annotated_frame=results[0].plot()

    cv2.rectangle(annotated_frame,(10,10),(340,60),(0,0,0),-1)

    cv2.putText(annotated_frame,f'uniquevehicle : {len(unique_vehicle)}',(20,40),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)

    cv2.imshow("Yolo counting vehicle",annotated_frame)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        print("quitting......")
        break

    frame_count+= 1


video.release()
cv2.destroyAllWindows()    

