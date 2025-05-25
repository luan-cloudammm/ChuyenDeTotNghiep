#xem số lượng sample của từng class
from collections import Counter
import os

# Đường dẫn đến thư mục chứa nhãn sau SMOTE
train_lbl_dir = "C:/Users/Admin/Downloads/archive/archive/train/labels"

# Đếm số lượng mẫu của từng lớp
class_counts = Counter()
label_files = [f for f in os.listdir(train_lbl_dir) if f.endswith(".txt")]

for lbl_file in label_files:
    lbl_path = os.path.join(train_lbl_dir, lbl_file)
    with open(lbl_path, "r") as f:
        lines = f.readlines()

    for line in lines:
        parts = line.strip().split()
        if len(parts) > 0:
            class_id = int(parts[0])
            class_counts[class_id] += 1

# Hiển thị kết quả ngắn gọn
print("Số lượng mẫu của từng lớp sau khi áp dụng SMOTE:")
for class_id, count in sorted(class_counts.items()):
    print(f"Lớp {class_id}: {count} mẫu")
