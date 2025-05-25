import os
from PIL import Image

# Đường dẫn thư mục
root_dir = "C:/Users/Admin/Downloads/archive"
image_dir = os.path.join(root_dir, "images")
label_dir = os.path.join(root_dir, "labels")

# 1. Lấy danh sách ảnh và nhãn
image_files = {os.path.splitext(f)[0] for f in os.listdir(image_dir) if f.lower().endswith(('.jpg', '.png', '.jpeg'))}
label_files = {os.path.splitext(f)[0] for f in os.listdir(label_dir) if f.endswith('.txt')}

# 2. Kiểm tra thiếu ảnh hoặc thiếu nhãn
missing_labels = image_files - label_files
missing_images = label_files - image_files

print(f"Tổng số ảnh: {len(image_files)}")
print(f"Tổng số nhãn: {len(label_files)}")
print(f"Ảnh không có nhãn: {missing_labels if missing_labels else 'Không có'}")
print(f"Nhãn không có ảnh: {missing_images if missing_images else 'Không có'}")

# 3. Kiểm tra định dạng và file rỗng
invalid_labels = []
empty_labels = []

def check_label_format(label_path):
    with open(label_path, "r") as f:
        lines = f.readlines()
        if len(lines) == 0:
            return False, "File rỗng"
        for i, line in enumerate(lines):
            parts = line.strip().split()
            if len(parts) != 5:
                return False, f"Line {i+1} không đủ 5 thành phần"
            try:
                class_id = int(parts[0])
                coords = list(map(float, parts[1:]))
                if not all(0 <= val <= 1 for val in coords):
                    return False, f"Line {i+1} có tọa độ ngoài [0, 1]"
            except ValueError:
                return False, f"Line {i+1} sai kiểu dữ liệu"
    return True, "OK"

for f in os.listdir(label_dir):
    if f.endswith(".txt"):
        full_path = os.path.join(label_dir, f)
        is_valid, message = check_label_format(full_path)
        if not is_valid:
            if message == "File rỗng":
                empty_labels.append(f)
            else:
                invalid_labels.append((f, message))

if empty_labels:
    print("\nCác file nhãn rỗng:")
    for f in empty_labels:
        print(f"- {f}")
else:
    print("\nKhông có file nhãn rỗng.")

if invalid_labels:
    print("\nCác file nhãn có định dạng lỗi:")
    for name, reason in invalid_labels:
        print(f"- {name}: {reason}")
else:
    print("\nTất cả file nhãn có định dạng hợp lệ.")

# 4. Kiểm tra ảnh lỗi
broken_images = []
for f in os.listdir(image_dir):
    try:
        img = Image.open(os.path.join(image_dir, f))
        img.verify()
    except Exception as e:
        broken_images.append(f)

if broken_images:
    print("\nCác ảnh lỗi không mở được:")
    for name in broken_images:
        print(f"- {name}")
else:
    print("\nTất cả ảnh mở được bình thường.")
