#train lại epochs hiện tại khi bị tắt máy giữa hoặc bị lỗi
from ultralytics import YOLO

if __name__ == "__main__":
    # Load a model
    model = YOLO("C:/Users/Admin/runs/detect/train4/weights/last.pt")  # load a partially trained model

    # Resume training
    results = model.train(resume=True)
