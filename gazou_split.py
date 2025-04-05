import cv2

img = cv2.imread("kaidankoukoku.png")
size_maeno = img.shape[:2]
print(size_maeno)

#img = img.reshape(21772,23150)
#A4:2,894px x 4,093px


bairitux = 21772/size_maeno[1]
bairituy = 23150/size_maeno[0]

bairitux_1 = size_maeno[1]/21772
bairituy_1 = size_maeno[0]/23150

top = 0     # 上には余白を追加しない
bottom = int(4093/bairituy)  # 下に4093ピクセルの余白
left = 0    # 左には余白を追加しない
right = int(2894/bairitux)  # 右に2894ピクセルの余白

# 白い余白を追加 (白色は[255, 255, 255])
white_color = [255, 255, 255]
img = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_CONSTANT, value=white_color)

size= img.shape[:2]
print(size)


a4width = int(2894/bairitux)
a4height = int(4093/bairituy)
countx = int(size[1]/a4width) + 1
county = int(size[0]/a4height) + 1
num = 0
for y in range(county):
    y = y * a4height
    #cv2.line(img,(x,0),(x,img.shape[0]),(0,0,0),10)
    for x in range(countx):
        x = x * a4width
        tox = x + a4width
        toy = y + a4height
        if x > size[1]:
            tox = size[1]
        if y > size[0]:
            toy = size[0]
        splited_img = img[y:toy,x:tox]
        splited_img = cv2.resize(splited_img, (2894,4093),fx=0,fy=0)
        splited_img = cv2.copyMakeBorder(splited_img, 69, 69,69, 69, cv2.BORDER_CONSTANT, value=white_color)
        img_name = "wsplit_result/kaidan{}({},{}).png".format(num,x,y)
        cv2.imwrite(img_name,splited_img)
        num += 1
        #cv2.line(img,(0,y),(img.shape[0],y),(0,0,0),10)
cv2.imwrite("lined.png",img)
