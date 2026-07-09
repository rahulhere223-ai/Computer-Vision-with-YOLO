import cv2

video=cv2.VideoCapture("video.mp4")

while True:
    success,frame=video.read()

    if not success:
       break

    cv2.imshow("Video",frame)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        print("Quitting")
        break

video.release()
cv2.destroyAllWindows()    
       
