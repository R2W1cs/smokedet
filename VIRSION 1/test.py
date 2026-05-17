
from ultralytics import YOLO

model = YOLO("D:/VIRSION 1/models/best.pt")

results = model.predict(
    source="test2.jpg",
    conf=0.5,
    save=True,
    name="face_result",
    exist_ok=True
)