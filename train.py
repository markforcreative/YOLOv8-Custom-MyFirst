from ultralytics import YOLO
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
yaml_path = os.path.join(ROOT_DIR, "config", "fs_powerbank.yaml")
model_path = "yolov8n.pt"


if __name__ == "__main__":
    model = YOLO(model_path)

    results = model.train(
        batch=32,
        workers=8,
        nbs=64,

        amp=True,
        cache=True,

        data="fs_powerbank.yaml",
        epochs=100,
        patience=20,
        imgsz=640,
        device=0,

        cos_lr=True,
        lr0=0.001,
        lrf=0.01,
        optimizer="AdamW",

        save=True,
        save_period=10,
        project="os.path.join(ROOT_DIR, "runs")",
        name="my_experiment",
        verbose=True,
    )

    metrics = model.val()
    print(f"最终mAP50：{metrics.box.map50:.4f}")
    print(f"最终mAP50-95：{metrics.box.map:.4f}")

