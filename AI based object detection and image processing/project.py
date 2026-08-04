from ultralytics import YOLO
import cv2

model=YOLO("yolov8n.pt")

video=cv2.VideoCapture("video5.mp4")

frame_count=1

vehicle_ids={
    'car':set(),
    'truck':set(),
    'bus':set()
}
previous_position={}
crossed_id=set()
crossed_vehicle_count =0

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
                
                x1,y1,x2,y2=box.xyxy[0]

                center_y=int((y1+y2)/2)

                if track_id in previous_position:
                   previous_y=previous_position[track_id]
                   print(f'Track id :{track_id}')
                   print(f'previous_y {previous_y} current_y : {center_y}')


                   if previous_y <= 180 and center_y > 180 :
                       if track_id not in crossed_id:
                          print(f'{object_name} crossed the line')

                          crossed_id.add(track_id)
                          crossed_vehicle_count +=1 


                previous_position[track_id]=center_y    


        # print(f'frame : {frame_count}')
        # print(f'Total vehicle {len(vehicle_ids['car']) + len(vehicle_ids['truck']) + len(vehicle_ids['bus'])   }')
        # print("="*30)
        # print('\n')        



    annotated_frame=results[0].plot()

    cv2.line(annotated_frame,(0,180),(640,180),(0,0,255),2)

    for result in results:

        for box in result.boxes:
            x1,y1,x2,y2=box.xyxy[0]

            center_x=int((x1+x2)/2)
            center_y=int((y1+y2)/2)

            cv2.circle(annotated_frame,(center_x,center_y),2,(0,255,255),-1)

    car_count=len(vehicle_ids["car"])
    truck_count=len(vehicle_ids["truck"])
    bus_count=len(vehicle_ids["bus"])
    
    vehicle_count=car_count + truck_count + bus_count
    
    cv2.rectangle(annotated_frame,(5,10),(300,120),(0,0,0),-1)
    cv2.putText(annotated_frame,f'Total vehicle : {vehicle_count}',(20,30),cv2.FONT_HERSHEY_COMPLEX,0.6,(0,255,0),2)
    cv2.putText(annotated_frame,f'car : {car_count}',(20,50),cv2.FONT_HERSHEY_COMPLEX,0.6,(0,255,0),2)
    cv2.putText(annotated_frame,f'Truck : {truck_count}',(20,70),cv2.FONT_HERSHEY_COMPLEX,0.6,(0,255,0),2)
    cv2.putText(annotated_frame,f'bus : {bus_count}',(20,90),cv2.FONT_HERSHEY_COMPLEX,0.6,(0,255,0),2)
    cv2.putText(annotated_frame,f'vehicle crossed the line {crossed_vehicle_count}',(20,110),cv2.FONT_HERSHEY_COMPLEX,0.6,(0,255,0),2)



    cv2.imshow("Yolo vehicle crossing line",annotated_frame)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        print("quitting....")
        break

    frame_count +=1


video.release()
cv2.destroyAllWindows()


