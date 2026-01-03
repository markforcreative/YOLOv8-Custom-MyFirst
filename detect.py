from ultralytics import YOLO

if __name__ == "__main__":
    model = YOLO("models\best.pt")

    results = model.predict(
        source=0,
        save=False,
        conf=0.5,
        device=0,
        show=True,
    )
