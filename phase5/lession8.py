import cv2
from ultralytics import YOLO

model=YOLO("yolov8n.pt")

video=cv2.VideoCapture("video5.mp4")

frame_count=1
uniquevehicle=set()

while True:
    success,frame=video.read()

    if not success:
        break

    frame=cv2.resize(frame,(640,360))

    results=model.track(frame,persist=True,verbose=False)

    for result in results:
        names=result.names
       

        for box in result.boxes:
            class_id=int(box.cls)
            object_names=names[class_id]
            

            if box.id is not None and object_names in ["car","truck","bus"]:
                track_id=int(box.id)
                uniquevehicle.add(track_id)

        print(f'Frame : {frame_count}')
        print(f'Uniquevehicle : {len(uniquevehicle)}')
        print("="*30)             

    annotated_frame=results[0].plot()

    cv2.imshow("YOLO vehicle detection count",annotated_frame)

    if cv2.waitKey(10) & 0xFF ==ord('q'):
        print("Quitting..........")
        break

    frame_count +=1

video.release()
cv2.destroyAllWindows()