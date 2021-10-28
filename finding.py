
import cv2
import numpy as np
img = cv2.imread('finding.jpg')
patch = cv2.imread('13.png')
threshold = 1


(h, w, d) = img.shape
r = 500 / w 
dim = (500, int(h * r))


mask = patch.copy()

(ho, wo, do) = patch.shape
for h in range(ho):
    for w in range(wo):
        black = 1
        for d in range(do):
            mask[h][w][d] = (255 - patch[h][w][d])
            if mask[h][w][d] < 255 /100 * threshold :
                black = 0
        if black == 0:
            for d in range(do):
                mask[h][w][d] = 0
        else:
            for d in range(do):
                mask[h][w][d] = 255

cv2.imshow('mask', mask)

result = cv2.matchTemplate(img, patch, cv2.TM_CCORR_NORMED,None,mask)
cv2.imshow('result', cv2.resize(result,dim))
cv2.normalize( result, result, 0, 1, cv2.NORM_MINMAX, -1 )

_minVal, _maxVal, minLoc, maxLoc = cv2.minMaxLoc(result, None)

matchLoc = maxLoc
img_display = img.copy()
cv2.rectangle(img_display, matchLoc, (matchLoc[0] + patch.shape[1], matchLoc[1] + patch.shape[0]), (0,0,0),2)
cv2.rectangle(result, matchLoc, (matchLoc[0] + patch.shape[1], matchLoc[1] + patch.shape[0]), (0,0,0),2 )

resized = cv2.resize(img_display, dim)
cv2.imshow('Display image', resized)

cv2.waitKey(0)