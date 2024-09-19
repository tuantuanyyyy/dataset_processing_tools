# -*- coding: utf-8 -*-

"""
this script is used to split the dataset into train, val, and test set.
The script will copy all the images and corresponding labels to three folders: train, val, and test.
The train set contains 80% of the data, the val set contains 10% of the data, and the test set contains 10% of the data.
The script will create the folders if they do not exist.

"""
import os
import random
import shutil


def split_data(image_source_folder, label_source_folder, base_folder):
    # 获取所有图片文件和对应的 txt 文件
    image_files = [f for f in os.listdir(image_source_folder) if f.endswith(('.jpg', '.png', '.jpeg'))]
    txt_files = [f for f in os.listdir(label_source_folder) if f.endswith('.txt')]

    # 确保图片和标签文件一一对应
    pairs = []
    for image_file in image_files:
        image_name, image_extension = os.path.splitext(image_file)
        for txt_file in txt_files:
            txt_name, _ = os.path.splitext(txt_file)
            if image_name == txt_name:
                pairs.append((image_file, txt_file))

    random.shuffle(pairs)

    # 计算划分点
    train_split_point = int(len(pairs) * 8 / 10)
    val_split_point = train_split_point + int(len(pairs) * 1 / 10)

    train_pairs = pairs[:train_split_point]
    val_pairs = pairs[train_split_point:val_split_point]
    test_pairs = pairs[val_split_point:]

    # 创建 images 和 labels 文件夹以及子文件夹
    images_folder = os.path.join(base_folder, 'images')
    labels_folder = os.path.join(base_folder, 'labels')
    train_images_folder = os.path.join(images_folder, 'train')
    val_images_folder = os.path.join(images_folder, 'val')
    test_images_folder = os.path.join(images_folder, 'test')
    train_labels_folder = os.path.join(labels_folder, 'train')
    val_labels_folder = os.path.join(labels_folder, 'val')
    test_labels_folder = os.path.join(labels_folder, 'test')

    for folder in [images_folder, labels_folder, train_images_folder, val_images_folder, test_images_folder, train_labels_folder, val_labels_folder, test_labels_folder]:
        if not os.path.exists(folder):
            os.makedirs(folder)

    # 复制文件到相应的文件夹
    for pair in train_pairs:
        image_file, txt_file = pair
        shutil.copy(os.path.join(image_source_folder, image_file), os.path.join(train_images_folder, image_file))
        shutil.copy(os.path.join(label_source_folder, txt_file), os.path.join(train_labels_folder, txt_file))

    for pair in val_pairs:
        image_file, txt_file = pair
        shutil.copy(os.path.join(image_source_folder, image_file), os.path.join(val_images_folder, image_file))
        shutil.copy(os.path.join(label_source_folder, txt_file), os.path.join(val_labels_folder, txt_file))

    for pair in test_pairs:
        image_file, txt_file = pair
        shutil.copy(os.path.join(image_source_folder, image_file), os.path.join(test_images_folder, image_file))
        shutil.copy(os.path.join(label_source_folder, txt_file), os.path.join(test_labels_folder, txt_file))


# 示例用法
image_source_folder = 'your_image_source_folder'
label_source_folder = 'your_label_source_folder'
base_folder = 'your_base_folder'

split_data(image_source_folder, label_source_folder, base_folder)
