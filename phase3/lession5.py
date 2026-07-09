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
        print("="*30)
        print(f'Frame : {frame_count}')
        count_obj={}
        
        for box in result.boxes:

            class_id=int(box.cls)
            confidence=float(box.conf)

            object_name=names[class_id]

            if object_name in count_obj:
                count_obj[object_name] +=1
            else:
                count_obj[object_name] =1

        for object_name,count in count_obj.items():
            print(f'{object_name:<10}: {count}')                        

    annotated_frame=results[0].plot()

    cv2.imshow("YOLO video detection",annotated_frame)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        print("Quitting...")
        break
    frame_count +=1

video.release()
cv2.destroyAllWindows()