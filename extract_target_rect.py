import os
import cv2
from PIL import Image
"""
This script is used to extract the target rectangles from the label files and save them as separate images.

The label files should be in the format of:

class_id x_center y_center width height

where class_id is 0 for the target rectangle.(of course, you can modify the code to extract other types of objects)

The script will read each label file and extract the corresponding rectangle from the corresponding image file. 

The cropped image will be saved in the output folder with the same name as the label file but with a different suffix.  


"""
# 设置路径
label_folder = r'D:\fall_person_dataset\Fall_Detection\valid\labels'
image_folder = r'D:\fall_person_dataset\Fall_Detection\valid\images'
output_folder = r'D:\fall_person_dataset\Fall_Detection\valid\cropped_images'

# 创建输出文件夹
os.makedirs(output_folder, exist_ok=True)

# 遍历标签文件
for label_file in os.listdir(label_folder):
    if label_file.endswith('.txt'):
        # 获取对应的图片文件名
        image_file = label_file.replace('.txt', '.jpg')  # 根据需要调整后缀名
        image_path = os.path.join(image_folder, image_file)

        # 读取图片
        if not os.path.exists(image_path):
            print(f"Image {image_path} does not exist.")
            continue

        image = cv2.imread(image_path)

        # 读取标签文件
        with open(os.path.join(label_folder, label_file), 'r') as f:
            for line in f.readlines():
                parts = line.strip().split()
                class_id = int(parts[0])

                # 检查类ID
                if class_id == 0:
                    # 获取归一化的坐标
                    x_center, y_center, width, height = map(float, parts[1:])

                    # 计算像素坐标
                    img_height, img_width = image.shape[:2]
                    x_center *= img_width
                    y_center *= img_height
                    width *= img_width
                    height *= img_height

                    # 计算矩形的左上角和右下角坐标
                    x1 = int(x_center - width / 2)
                    y1 = int(y_center - height / 2)
                    x2 = int(x_center + width / 2)
                    y2 = int(y_center + height / 2)

                    # 裁剪图像
                    cropped_image = image[y1:y2, x1:x2]

                    # 保存裁剪后的图像
                    output_file = os.path.join(output_folder, f"{label_file.replace('.txt', '')}_{class_id}.jpg")
                    cv2.imwrite(output_file, cropped_image)
                    print(f"Saved cropped image: {output_file}")