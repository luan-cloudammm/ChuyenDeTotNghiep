
from ultralytics import YOLO

def train_model():
    model = YOLO("yolo11n.pt")

    results = model.train(
        data="C:/Users/Admin/Downloads/archive/archive/bienbaogiaothong.yaml",
        epochs=100,
        imgsz=640,
        device="cuda",
        augment=True,
        amp=False,
    )


if __name__ == '__main__':
    train_model()
