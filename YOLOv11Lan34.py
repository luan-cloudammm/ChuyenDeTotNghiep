
from ultralytics import YOLO

def train_model():
    model = YOLO("yolo11n.pt")

    results = model.train(
        data="C:/Users/Admin/Downloads/archive/archive/bienbaogiaothong.yaml",

        epochs=100,
        imgsz=640,
        device="cuda",
        augment=True,

        # Tăng cường ảnh
        degrees=10.0,              # Xoay ảnh ±10 độ
        translate=0.1,             # Dịch ảnh ±10%
        scale=0.5,                 # Phóng to/thu nhỏ ±50%
        shear=5.0,                 # Xoắn hình
        perspective=0.0005,        # Hiệu ứng phối cảnh nhẹ
        flipud=0.1,                # Xoay ảnh theo chiều dọc 10%
        fliplr=0.5,                # Lật ảnh ngang 50%

        # Thay đổi màu sắc, ánh sáng, độ tương phản
        hsv_h=0.015,               # Thay đổi hue (sắc độ)
        hsv_s=0.7,                 # Thay đổi saturation (độ bão hòa)
        hsv_v=0.4,                 # Thay đổi value (độ sáng)

        # hiệu năng
        batch=16,
        amp=False,
        cache=True,               # Lưu cache để tăng tốc
        patience=20,              # Early stopping nếu không cải thiện
    )

if __name__ == '__main__':
    train_model()
