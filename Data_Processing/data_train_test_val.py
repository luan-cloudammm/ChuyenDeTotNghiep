import os
import shutil
import random
# Đường dẫn gốc đến thư mục chứa hình ảnh và nhãn
root_dir = "C:/Users/Admin/Downloads/archive/archive2"
images_dir = os.path.join(root_dir, "images")  # Chứa hình ảnh
labels_dir = os.path.join(root_dir, "labels")  # Chứa nhãn

# Đường dẫn lưu tập train, val, test
train_img_dir = os.path.join(root_dir, "train/images")
train_lbl_dir = os.path.join(root_dir, "train/labels")

val_img_dir = os.path.join(root_dir, "val/images")
val_lbl_dir = os.path.join(root_dir, "val/labels")

test_img_dir = os.path.join(root_dir, "test/images")
test_lbl_dir = os.path.join(root_dir, "test/labels")

# Tạo thư mục nếu chưa tồn tại
for folder in [train_img_dir, train_lbl_dir, val_img_dir, val_lbl_dir, test_img_dir, test_lbl_dir]:
    os.makedirs(folder, exist_ok=True)

# Lấy danh sách tất cả hình ảnh
image_files = [f for f in os.listdir(images_dir) if f.endswith((".jpg", ".png", ".jpeg"))]
random.shuffle(image_files)  # Xáo trộn danh sách ảnh

# Chia tỷ lệ 7:2:1
total_images = len(image_files)
train_split = int(0.7 * total_images)
val_split = int(0.9 * total_images)  # 70% train + 20% val = 90%


# Hàm di chuyển file ảnh và file label tương ứng
def move_files(files, dest_img_folder, dest_lbl_folder):
    for img_file in files:
        # Tìm file label tương ứng
        label_file = img_file.replace(".jpg", ".txt").replace(".png", ".txt").replace(".jpeg", ".txt")

        # Đường dẫn gốc
        src_img_path = os.path.join(images_dir, img_file)
        src_lbl_path = os.path.join(labels_dir, label_file)

        # Đường dẫn đích
        dst_img_path = os.path.join(dest_img_folder, img_file)
        dst_lbl_path = os.path.join(dest_lbl_folder, label_file)

        # Di chuyển file nếu tồn tại nhãn
        if os.path.exists(src_lbl_path):
            shutil.move(src_img_path, dst_img_path)
            shutil.move(src_lbl_path, dst_lbl_path)


# Thực hiện chia dữ liệu
move_files(image_files[:train_split], train_img_dir, train_lbl_dir)  # 70% Train
move_files(image_files[train_split:val_split], val_img_dir, val_lbl_dir)  # 20% Val
move_files(image_files[val_split:], test_img_dir, test_lbl_dir)  # 10% Test

print("Chia dữ liệu hoàn tất!")