from ultralytics import YOLO
import cv2

model=YOLO("yolov8n.pt")

video=cv2.VideoCapture("video5.mp4")
frame_count=1

vehicle_ids={
    "car":set(),
    "truck":set(),
    "bus":set()
}

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

            if box.id is not None and object_name in vehicle_ids:
                track_id=int(box.id)
                vehicle_ids[object_name].add(track_id)


        print(f'Frame count : {frame_count}')
        print(f'Total vehicle: {len(vehicle_ids["car"]) + len(vehicle_ids["truck"]) +len(vehicle_ids["bus"])}')        
        print(f'car : {len(vehicle_ids["car"])}')
        print(f'truck : {len(vehicle_ids["truck"])}')
        print(f'bus : {len(vehicle_ids["bus"])}')
        print("="*30)
        print('\n')

    annotated_frame=results[0].plot()
    car_count=len(vehicle_ids["car"])
    truck_count=len(vehicle_ids["truck"])
    bus_count=len(vehicle_ids["bus"])

    vehicle_count=car_count + truck_count + bus_count

    cv2.rectangle(annotated_frame,(5,10),(300,100),(0,0,0),-1)
    cv2.putText(annotated_frame,f'Total vehicle : {vehicle_count}',(20,30),cv2.FONT_HERSHEY_COMPLEX,0.6,(0,255,0),2)
    cv2.putText(annotated_frame,f'car : {car_count}',(20,50),cv2.FONT_HERSHEY_COMPLEX,0.6,(0,255,0),2)
    cv2.putText(annotated_frame,f'Truck : {truck_count}',(20,70),cv2.FONT_HERSHEY_COMPLEX,0.6,(0,255,0),2)
    cv2.putText(annotated_frame,f'bus : {bus_count}',(20,90),cv2.FONT_HERSHEY_COMPLEX,0.6,(0,255,0),2)


    cv2.imshow("YOLO vehicle counting",annotated_frame)    

    if cv2.waitKey(10) & 0xFF == ord('q'):
        print("quitting....")
        break

    frame_count +=1


video.release()
cv2.destroyAllWindows()