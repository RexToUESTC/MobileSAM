import cv2
import os

import numpy as np

# 输入和输出文件夹路径
input_folder = 'C:/Users/trcay/Desktop/lasso/images/'
output_folder = 'C:/Users/trcay/Desktop/lasso/bi_images/'

# 创建输出文件夹（如果不存在）
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 获取输入文件夹中所有的 JPG 图像文件名
image_files = [file for file in os.listdir(input_folder) if file.lower().endswith('.jpg')]


if __name__ == "__main__":
    
    
    # 循环处理每张图像
    for id in range(8753):
        img_file = "v_" + str(id) + ".jpg"
        
        # 读取图像
        img_path = os.path.join(input_folder, img_file)
        img = cv2.imread(img_path)

        normalized_img = cv2.normalize(img, None, alpha=40, beta=255, norm_type=cv2.NORM_MINMAX)

        # 使用中值滤波降噪点
        median_blur = cv2.medianBlur(normalized_img, 5)

        # 将图片转为灰度图
        img_gray = cv2.cvtColor(median_blur, cv2.COLOR_RGB2GRAY)

        # 将灰度图转换为二值图
        _, img_binary = cv2.threshold(img_gray, 170, 255, cv2.THRESH_BINARY)

        # 保存二值化图像到输出文件夹中 转化为bmp格式
        name = os.path.splitext(img_file)[0]
        newFileName = name + ".bmp"
        output_path = os.path.join(output_folder, newFileName)
        cv2.imwrite(output_path, img_binary)


