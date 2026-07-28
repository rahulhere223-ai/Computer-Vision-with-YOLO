# Computer-Vision-with-YOLO
# YOLOv8 Learning Journey

This repository documents my learning journey in Computer Vision using YOLOv8 and OpenCV during my DRDO Summer Internship.

## Topics Covered

- YOLOv8 Installation
- Object Detection
- Confidence Score
- Bounding Boxes
- Class IDs

  <img width="1600" height="327" alt="Screenshot 2026-07-07 195819" src="https://github.com/user-attachments/assets/48a912ae-15f3-4ed5-a76e-40d407960946" />
  <img width="1108" height="732" alt="Screenshot 2026-07-07 200936" src="https://github.com/user-attachments/assets/02c0e589-19d4-4d32-b355-418116a23193" />
  <img width="1131" height="561" alt="Screenshot 2026-07-07 203259" src="https://github.com/user-attachments/assets/071c9b01-d49a-48e2-8b7e-e6d3bc9e20d8" />

## Mapping class IDs to Object names
  
  <img width="1166" height="656" alt="Screenshot 2026-07-08 192756" src="https://github.com/user-attachments/assets/155b2fbd-6d09-4066-887b-ece44826999d" />

## Object detection
  
<img width="1162" height="663" alt="Screenshot 2026-07-09 200016" src="https://github.com/user-attachments/assets/d8f8cf10-87cc-4e6a-892d-f4ffa0e43eb2" />
<img width="465" height="521" alt="Screenshot 2026-07-09 233249" src="https://github.com/user-attachments/assets/90d19908-25ef-49c8-866c-2c10e6820751" />

## Object Tracking in a video
-model.track() -persist==True -Tracking IDs

<img width="800" height="483" alt="Screenshot 2026-07-11 195414" src="https://github.com/user-attachments/assets/29957b71-de76-4a2b-9118-7e2b0d1a9842" />
<img width="798" height="486" alt="Screenshot 2026-07-11 195400" src="https://github.com/user-attachments/assets/5a4da3f5-1ced-4b6d-9f47-5638418db19c" />

## Unique vehicle counter
-learned python data structure set to count vehicle and filter

<img width="646" height="239" alt="Screenshot 2026-07-13 194131" src="https://github.com/user-attachments/assets/5b758a1d-cb8c-413f-9c72-52be2754db24" />
<img width="325" height="364" alt="Screenshot 2026-07-13 195938" src="https://github.com/user-attachments/assets/bfd10e1a-4c03-44d3-afbd-7589b2f5544e" />
<img width="351" height="386" alt="Screenshot 2026-07-13 195927" src="https://github.com/user-attachments/assets/108df41f-2791-441d-a71a-f7d1f0c5d38e" />

📅 Day 8 - Live Vehicle Counter Dashboard
🚀 What I Learned
Learned how to use cv2.putText() to display text on video frames.
Learned how to use cv2.rectangle() to create a dashboard background.
Displayed the live count of unique vehicles on the video instead of the terminal.
Used a Python set to store unique tracking IDs and avoid duplicate counting.
Filtered only vehicle classes (car, truck, bus) for counting.
Understood how YOLO tracking IDs help identify unique objects across frames.

<img width="1600" height="900" alt="Screenshot 2026-07-26 202332" src="https://github.com/user-attachments/assets/8e31ab9b-88a9-4377-9eed-45b38e4a155d" />

Built a vehicle counting DashBoard
<img width="889" height="591" alt="Screenshot 2026-07-27 215850" src="https://github.com/user-attachments/assets/12f92c83-37f1-4b8b-b517-5bb3543cab0a" />

Day 9- vehicle crossing the line
<img width="952" height="709" alt="Screenshot 2026-07-28 231441" src="https://github.com/user-attachments/assets/0fcc0939-45cf-45c7-8190-c0f56dc35947" />
<img width="958" height="686" alt="Screenshot 2026-07-28 235746" src="https://github.com/user-attachments/assets/2062d2d9-597d-49c4-a64d-05dc4b3f006c" />









