import os

root_dir = "C:/Users/Admin/Downloads/archive/archive"
label_dir = os.path.join(root_dir, "labels")
image_dir = os.path.join(root_dir, "images")

# Duyệt toàn bộ các file .txt trong thư mục labels
for filename in os.listdir(label_dir):
    label_path = os.path.join(label_dir, filename)

    # Nếu file rỗng (không có nội dung)
    if os.path.getsize(label_path) == 0:
        # Xóa file nhãn
        os.remove(label_path)
        print(f"Đã xóa nhãn rỗng: {label_path}")

        # Tên ảnh tương ứng (same name, .jpg hoặc .png)
        base_name = os.path.splitext(filename)[0]
        img_jpg_path = os.path.join(image_dir, f"{base_name}.jpg")
        img_png_path = os.path.join(image_dir, f"{base_name}.png")

        # Xóa ảnh nếu tồn tại
        if os.path.exists(img_jpg_path):
            os.remove(img_jpg_path)
            print(f"Đã xóa ảnh JPG: {img_jpg_path}")
        elif os.path.exists(img_png_path):
            os.remove(img_png_path)
            print(f"Đã xóa ảnh PNG: {img_png_path}")
