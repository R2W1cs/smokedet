from ultralytics import YOLO

def train():
    model = YOLO("yolov8n.pt")

    model.train(
        data="D:/VIRSION 1/data_face.yaml",
        epochs=10,
        imgsz=640,
        batch=8,
        device=0,
        project="D:/VIRSION 1/runs",
        name="face_first_train"
    )

if __name__ == "__main__":
    train()