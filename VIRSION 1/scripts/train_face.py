from ultralytics import YOLO

def train():
    model = YOLO("yolov8s.pt")

    model.train(
        data="D:/VIRSION 1/data_face.yaml",

        # 🔥 توازن بين القوة والأمان
        epochs=30,
        imgsz=640,
        batch=6,
        device=0,
        workers=0,

        # 🔥 تعلم أهدأ (مهم جداً)
        lr0=0.0005,
        optimizer="AdamW",
        patience=10,

        # 🔥 Augmentation نظيف للفيس
        hsv_h=0.01,
        hsv_s=0.4,
        hsv_v=0.3,

        degrees=1,
        translate=0.03,
        scale=0.2,

        fliplr=0.5,

        # 💣 أهم تعديل
        mosaic=0.3,
        mixup=0.0,

        # 🔥 تحسين التدريب
        cos_lr=True,
        warmup_epochs=2,

        project="D:/VIRSION 1/runs",
        name="face_PRO"
    )

if __name__ == "__main__":
    train()