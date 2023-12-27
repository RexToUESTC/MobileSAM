import cv2
import os

path = r"C:\Users\eternal\PycharmProjects\MobileSAM\my_project\sam_result2"
to_path = r"C:\Users\eternal\PycharmProjects\MobileSAM\my_project\sam_result_aggregation2"
dirs = os.listdir(path)

for dir in dirs:
    final_path = os.path.join(path, dir, "0.png")
    if os.path.exists(final_path):
        my_img = cv2.imread(final_path)
        cv2.imwrite(os.path.join(to_path, dir + ".png"), my_img)
