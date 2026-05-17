from ultralytics import YOLO

def train():
    model = YOLO("yolov8n.pt")

    model.train(
        data="D:/VIRSION 1/data_vape.yaml",
        epochs=90,
        imgsz=640,
        batch=8,
        device=0,

        lr0=0.0007,
        optimizer="AdamW",
        patience=20,

        hsv_h=0.02,
        hsv_s=0.8,
        hsv_v=0.5,

        degrees=5,
        translate=0.08,
        scale=0.5,

        fliplr=0.5,
        mosaic=1.0,
        mixup=0.1,

        project="D:/VIRSION 1/runs",
        name="vape_best"
    )

if __name__ == "__main__":
    train()