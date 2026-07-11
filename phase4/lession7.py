import cv2
from ultralytics import YOLO

model=YOLO("yolov8n.pt")

video=cv2.VideoCapture("video5.mp4")
frame_count=1

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
            object_name=names[class_id]
            confidence=float(box.conf)

            if box.id is not None:
                track_id=int(box.id)

                print(f'Frame: {frame_count}')
                print(f'Tracking ID: {track_id}')
                print(f'Detected: {object_name}')
                print(f'confidence: {confidence:.2f}')
                print("=="*30)


    annotated_frame=results[0].plot()
    cv2.imshow("YOLO Tracking",annotated_frame)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        print("Quitting.........")
        break
    frame_count +=1

video.release()
cv2.destroyAllWindows()                


