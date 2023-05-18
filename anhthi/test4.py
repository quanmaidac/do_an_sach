import cv2
import numpy as np

I=cv2.imread('anh5.jpg')
#show anh goc
cv2.imshow('Anh Goc',I)

dimensions = I.shape
print('Kich thuoc anh : ', dimensions)

I2=cv2.resize(I,(800,1200))
cv2.imshow('Anh Resize',I2)

Ihsv=cv2.cvtColor(I,cv2.COLOR_BGR2HSV)
cv2.imshow('Kenh S',Ihsv[:,:,1])

Is = cv2.blur(Ihsv[:,:,1], (5,5))
cv2.imshow('Anh Loc S',Is)

I_bina = 255 - Is
thresh, Ib = cv2.threshold(I_bina,180 , 255, cv2.THRESH_OTSU)
cv2.imshow('Ib',Ib)

contours,_ = cv2.findContours(Ib, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
max = 0.0
max_contours = []
for cnt in contours:
  if max <= cv2.arcLength(cnt,True):
    max = cv2.arcLength(cnt,True)
    max_contours = cnt
I_copy = I.copy()
cv2.drawContours(I_copy, [max_contours], -1, 255, 3)
cv2.imshow('Ve Contours',I_copy)

Iv=(Ihsv[:,:,2])
cv2.imshow('Anh Kenh V',Iv)
h = I.shape[0]
w = I.shape[1]
for i in range(h):
    for j in range(w):
        a = np.min(I[:,:,2])
        b = np.max(I[:,:,2])
        Iv[i][j]=(255*int(Iv[i][j]-a))//(b-a)
cv2.imshow('Kenh V bien doi', Iv)
img_rgb = cv2.cvtColor(Ihsv,cv2.COLOR_HSV2BGR)
cv2.imshow('Anh I ket qua',img_rgb)


cv2.waitKey(0)
cv2.destroyAllWindows()