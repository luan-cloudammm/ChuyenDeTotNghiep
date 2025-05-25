#cân bằng dữ liệu bằng kỹ thuật SMOTE
import os
import numpy as np
import shutil
from imblearn.over_sampling import SMOTE

# Đường dẫn đến thư mục chứa dữ liệu train
root_dir = "C:/Users/Admin/Downloads/archive/archive2"
train_img_dir = os.path.join(root_dir, "train/images")
train_lbl_dir = os.path.join(root_dir, "train/labels")

# Lấy danh sách file nhãn
label_files = [f for f in os.listdir(train_lbl_dir) if f.endswith(".txt")]

# Tạo danh sách lưu dữ liệu nhãn
X = []
y = []
file_map = {}  # Dùng để ánh xạ file nhãn với dữ liệu

for lbl_file in label_files:
    lbl_path = os.path.join(train_lbl_dir, lbl_file)
    with open(lbl_path, "r") as f:
        lines = f.readlines()

    for line in lines:
        parts = line.strip().split()
        if len(parts) > 0:
            class_id = int(parts[0])
            bbox = list(map(float, parts[1:]))  # Bounding box

            # Thêm vào dataset
            X.append(bbox)
            y.append(class_id)

            # Lưu file tương ứng
            if lbl_file not in file_map:
                file_map[lbl_file] = []
            file_map[lbl_file].append((class_id, bbox))

# Chuyển về numpy array
X = np.array(X)
y = np.array(y)

# Áp dụng SMOTE để tăng cường dữ liệu nhãn
smote = SMOTE(sampling_strategy="auto", k_neighbors=5)
X_resampled, y_resampled = smote.fit_resample(X, y)

# Ghi dữ liệu nhãn đã mở rộng vào thư mục train/labels/
resampled_idx = len(label_files)  # Đánh số file mới

for i in range(len(X_resampled)):
    class_id = y_resampled[i]
    bbox = X_resampled[i]

    # Ghi dữ liệu ra file mới
    new_lbl_file = f"aug_{resampled_idx}.txt"
    new_lbl_path = os.path.join(train_lbl_dir, new_lbl_file)

    with open(new_lbl_path, "w") as f:
        f.write(f"{class_id} " + " ".join(map(str, bbox)) + "\n")

    # Sao chép một ảnh bất kỳ để gán cho dữ liệu mới
    if len(label_files) > 0:
        random_img = label_files[0].replace(".txt", ".jpg")  # Chọn ảnh đầu tiên làm mẫu
        src_img_path = os.path.join(train_img_dir, random_img)
        dst_img_path = os.path.join(train_img_dir, new_lbl_file.replace(".txt", ".jpg"))

        if os.path.exists(src_img_path):
            shutil.copy(src_img_path, dst_img_path)

    resampled_idx += 1

print("Đã áp dụng SMOTE và mở rộng dữ liệu thành công!")
