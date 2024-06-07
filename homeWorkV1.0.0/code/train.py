from ultralytics import YOLO

model = YOLO("yolov8.yaml")
model = YOLO("yolov8n.pt")
model = YOLO("yolov8n.yaml").load("yolov8n.pt")

results = model.train(data="../dataset/data.yaml", epochs=100)
