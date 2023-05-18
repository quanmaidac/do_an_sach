import cv2
import numpy as np
import matplotlib.pyplot as plt

I=cv2.imread('tao.jpg')
cv2.imshow('anh goc',I)

Ihsv=cv2.cvtColor(I,cv2.COLOR_BGR2HSV)
#4
Ih,Is,Iv = cv2.split(I)
def tinh_hist(Ig):
    a=np.zeros(256,dtype='int')
    h=Ig.shape[0]
    w=Ig.shape[1]
    for i in range(h):
        for j in range(w):
             g=Ig[i][j]
             a[g]=a[g]+1
    return a

print('Kênh V')
Iv=I[:,:,2]
hV=tinh_hist(Iv)
plt.plot(hV)
plt.show()
#5
ST = cv2.medianBlur(Is,7)
cv2.imshow('Anh loc median kenh S',ST)
#6
Is = 255 - Is
threhold, ImgO = cv2.threshold(Is,125,255,cv2.THRESH_OTSU)
cv2.imshow('Anh nhi phan cua anh nghich dao kenh S',ImgO)
#7
contours,_ = cv2.findContours(I, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
max = 0.0
max_contours = []
for cnt in contours:
  if max <= cv2.arcLength(cnt,True):
    max = cv2.arcLength(cnt,True)
    max_contours = cnt
I_copy = I.copy()
cv2.drawContours(I_copy, [max_contours], -1, 255, 3)
cv2.imshow('Ve Contours',I_copy)

cv2.waitKey()
cv2.destroyAllWindows()