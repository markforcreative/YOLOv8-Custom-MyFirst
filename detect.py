from ultralytics import YOLO

if __name__ == "__main__":
    model = YOLO("models/best.pt")

    results = model.predict(
        source="assets/samples/Nongfu_Spring_water_bottle_sample.jpg",
        save=True,
        conf=0.5,
        device=0,
    )
