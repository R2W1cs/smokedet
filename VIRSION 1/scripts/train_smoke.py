from ultralytics import YOLO

def train():
    model = YOLO("yolov8n.pt")

    model.train(
        data="D:/VIRSION 1/data_smoke.yaml",
        epochs=100,
        imgsz=640,
        batch=8,
        device=0,

        lr0=0.0005,
        optimizer="AdamW",
        patience=25,

        hsv_h=0.02,
        hsv_s=0.9,
        hsv_v=0.6,

        degrees=0,
        translate=0.1,
        scale=0.6,

        fliplr=0.5,
        mosaic=1.0,
        mixup=0.15,

        project="D:/VIRSION 1/runs",
        name="smoke_best"
    )

if __name__ == "__main__":
    train()