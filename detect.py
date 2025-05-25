#nhận diện biển báo giao thông bằng cam laptop
import cv2
import matplotlib.pyplot as plt
from ultralytics import YOLO

model = YOLO("C:/Users/Admin/runs/detect/train_YOLOv11_Lan2/weights/best.pt")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)
    annotated_frame = results[0].plot()

    # Chuyển BGR → RGB để hiển thị đúng màu
    rgb_frame = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)

    plt.imshow(rgb_frame)
    plt.title("YOLOv11n - Traffic Sign Detection")
    plt.axis('off')
    plt.pause(0.01)  # Dừng 10ms
    plt.clf()        # Xóa ảnh cũ trước khi hiển thị ảnh mới

    # Nhấn Ctrl+C để dừng vòng lặp
