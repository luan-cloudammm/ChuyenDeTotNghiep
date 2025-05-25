# test khả năng nhận diện của model với các ảnh thực tế
from ultralytics import YOLO
import os
model = YOLO("C:/Users/Admin/runs/detect/train_YOLOv11_Lan2/weights/best.pt")

#results = model("C:/Users/Admin/Downloads/test6.png")

results = model("C:/Users/Admin/Downloads/anh2.jpg")

# Thư mục lưu kết quả
save_dir = "C:/Users/Admin/Downloads/nhandien"
os.makedirs(save_dir, exist_ok=True)

for result in results:
    xywh = result.boxes.xywh  # center-x, center-y, width, height
    xywhn = result.boxes.xywhn  # normalized
    xyxy = result.boxes.xyxy  # top-left-x, top-left-y, bottom-right-x, bottom-right-y
    xyxyn = result.boxes.xyxyn  # normalized
    names = [result.names[cls.item()] for cls in result.boxes.cls.int()]  # class name of each box
    confs = result.boxes.conf  # confidence score of each box
    save_path = os.path.join(save_dir, os.path.basename("C:/Users/Admin/Downloads/test6.png"))  # giữ tên ảnh gốc
    result.save(filename=save_path)

    result.show()  # display to screen