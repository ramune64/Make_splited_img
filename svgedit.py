import cv2
import numpy as np

# 1cm = 37.795pxとして計算
cm_to_px = 37.795
width_cm = 158  # 幅158cm
height_cm = 168  # 縦168cm

# 幅と高さをピクセルに変換
width_px = int(width_cm * cm_to_px)
height_px = int(height_cm * cm_to_px)

# 画像の背景を白で作成
image = np.ones((height_px, width_px, 3), dtype=np.uint8) * 255
""" for y in range(height_px):
    for x in range(width_px):
        # 左上から右下への距離に応じて色を変える
        alpha = (x + y) / (width_px + height_px)  # 0.0 ~ 1.0 の値
        purple = np.array([128, 0, 128])  # 紫の色
        white = np.array([255, 255, 255])  # 白の色
        color = (1 - alpha) * purple + alpha * white  # グラデーションを計算
        image[y, x] = color """
# 横線の間隔（14cm毎）と線の太さ
interval_cm = 14  # 14cm間隔
interval_px = int(interval_cm * cm_to_px)  # ピクセルに変換
line_thickness = 4  # 2px

# 上下の境界には線を引かないので、その間に線を引く
for y in range(interval_px, height_px - interval_px, interval_px):
    cv2.line(image, (0, y), (width_px, y),(0,0,0), line_thickness)

# 結果を表示または保存
#cv2.imshow('Image with lines', image)
cv2.imwrite('image_with_lines.png', image)
cv2.waitKey(0)
cv2.destroyAllWindows()