from ultralytics import YOLO

def train():
    model = YOLO("yolov8s.pt")  # مودل أقوى من n

    model.train(
        data="D:/VIRSION 1/data_cigarette.yaml",

        # 🔥 إعدادات أساسية
        epochs=40,
        imgsz=640,
        batch=6,
        device=0,
        workers=0,

        # 🔥 تعلم مستقر
        lr0=0.0008,
        lrf=0.01,
        optimizer="AdamW",
        patience=15,

        # 🔥 Augmentation مناسب للسيجارة
        hsv_h=0.01,
        hsv_s=0.6,
        hsv_v=0.4,

        degrees=5,
        translate=0.08,
        scale=0.4,
        shear=0.0,

        fliplr=0.5,
        mosaic=0.7,   # أقل من الفيس (لأن السيجارة صغيرة)
        mixup=0.05,

        # 🔥 تحسين الأداء
        cos_lr=True,
        warmup_epochs=3,

        project="D:/VIRSION 1/runs",
        name="cigarette_PRO"
    )

if __name__ == "__main__":
    train()