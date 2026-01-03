from ultralytics import YOLO

if __name__ == "__main__":
    model = YOLO("../runs/train/fs_powerbank_model_optimized_small/weights/best.pt")

    results = model.predict(
        source=0,
        save=False,
        conf=0.5,
        device=0,
        show=True,
    )
