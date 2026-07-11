import cv2
from ultralytics import YOLO

model=YOLO("yolov8n.pt")

video=cv2.VideoCapture("video5.mp4")

while True:
    success,frame=video.read()

    if not success:
        break

    frame=cv2.resize(frame,(640,360))

    results=model.track(frame,persist=True)

    annotated_frame=results[0].plot()

    cv2.imshow("YOLO tracking",annotated_frame)

    if cv2.waitKey(10) & 0xFF ==ord('q'):
        print("Quiting.........")
        break

video.release()
cv2.destroyAllWindows()    
