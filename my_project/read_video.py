import cv2
import os.path as osp
import os

cap = cv2.VideoCapture(r"C:\Users\eternal\PycharmProjects\MobileSAM\my_project\lasso2.MP4")

c = 0

while (1):
    ret, frame = cap.read()
    print(c)
    if os.path.exists(r"C:\Users\eternal\PycharmProjects\MobileSAM\my_project\images2\v_" + str(c) + ".jpg"):
        c = c + 1
        continue
    # cv2.imshow("capture", frame)
    cv2.imwrite("./images2/v_" + str(c) + ".jpg", frame)
    c = c + 1
    # print(c, ret)
    if not ret:
        break

cap.release()
cv2.destroyAllWindows()
