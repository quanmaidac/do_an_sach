import cv2
import numpy as np
import matplotlib.pyplot as plt

I = cv2.imread('hat1.PNG')
cv2.imshow('anh goc',I)
#chuyen doi sang HSV
Ihsv=cv2.cvtColor(I,cv2.COLOR_BGR2HSV)
#Hien thi kenh V
cv2.imshow('Kenh V', Ihsv[:,:,2])
#Xac dinh muc xam max kenh H
print(np.max(Ihsv[:,:,0]))
#Ve histogram kenh S
Ih,Is,Iv = cv2.split(Ihsv)

def tinh_hist(Ig):
    a=np.zeros(256,dtype='int')
    h=Ig.shape[0]
    w=Ig.shape[1]
    for i in range(h):
        for j in range(w):
             g=Ig[i][j]
             a[g]=a[g]+1
    return a

print('Kênh S')
Is=I[:,:,1]
hS=tinh_hist(Is)
plt.plot(hS)
plt.show()
#Lam tron anh tren kenh S
I_s = cv2.blur(Is,(5,5))
cv2.imshow('Anh loc kenh S',I_s)
#Lam tron median tren kenh S
I_ms = cv2.medianBlur(Is,5)
cv2.imshow('Anh loc median kenh S',I_ms)
#Ve contour
I_bina = 255 - I
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

cv2.waitKey(0)
cv2.destroyAllWindows()