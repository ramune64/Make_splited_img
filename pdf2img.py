import glob
import cv2

dir = glob.glob("result6/*")

for f in dir:
    img = cv2.imread(f)
    splited_img = cv2.copyMakeBorder(img, 30, 30,30, 30, cv2.BORDER_CONSTANT, value=(255,255,255))
    dirname = "result6/" + f.split("\\")[1]
    print(dirname)
    cv2.imwrite(dirname,splited_img)