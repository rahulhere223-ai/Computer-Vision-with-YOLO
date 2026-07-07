from ultralytics import YOLO

model=YOLO("yolov8n.pt")

results=model("bus.jpg")

for result in results:
    # print(result.boxes)
    # boxes=result.boxes

    # for box in boxes:
    #     print("Class ID : ",int(box.cls))
    #     print("Confidence : ",float(box.conf))
    #     print("Cordinates : ",box.xyxy)
    #     print("--------------------")

    names=result.names


    for box in result.boxes:
        class_id=int(box.cls)

        print("Object : ",names[class_id])
        print("Confidence",float(box.conf))
        x1,y1,x2,y2=box.xyxy[0]
        print(f'Cordinates {int(x1),int(y1)} -> {int(x2),int(y2)} ')
        print("------------------")




