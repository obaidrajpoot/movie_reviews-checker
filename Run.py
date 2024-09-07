from ultralytics import YOLO
model=YOLO('best5.pt')

model.predict(source=0 , imgsz=640 , conf=0.4 ,show=True)
