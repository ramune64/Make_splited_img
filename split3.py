import cv2
import glob

#imgs = glob.glob("20248/*")
file = "62_11.png"
#print(imgs)

img = cv2.imread(file)
size = img.shape[:2]
print(size)
row = 2
col = 4
ii = 0
slnum = 0
img = cv2.imread(file)
for c in range(col):
    for r in range(row):
        #print(r*2337,(r+1)*2337,c*1653,(c+1)*1653)
        spimg = img[r*2337:(r+1)*2337,c*1653:(c+1)*1653]
        splited_img = cv2.copyMakeBorder(spimg, 30, 30,30, 30, cv2.BORDER_CONSTANT, value=(255,255,255))
        if len(str(ii)) == 1:
            name = "imgfolder5/result0{}-00{}.png".format(slnum,ii)
        if len(str(ii)) == 2:
            name = "imgfolder5/result0{}-0{}.png".format(slnum,ii)
        if len(str(ii)) == 3:
            name = "imgfolder5/result0{}-{}.png".format(slnum,ii)
        print(name)
        cv2.imwrite(name,splited_img)
        ii += 1
slnum += 1