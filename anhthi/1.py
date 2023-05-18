import cv2
import numpy as np
import matplotlib.pyplot as plt
#1
I = cv2.imread("hat1.PNG")
cv2.imshow("Anh goc",I)
#2
Ihsv = cv2.cvtColor(I,cv2.COLOR_BGR2HSV)
print("ma tran hsv \n",Ihsv)
cv2.imshow("kenh V",Ihsv[:,:,2])
print("muc sang lon nhat kenh S:", np.max(Ihsv[:,:,1]))
print("muc sang nho nhat kenh S:", np.min(Ihsv[:,:,1]))
#3
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
Is=Ihsv[:,:,1]
hS=tinh_hist(Is)
plt.plot(hS)
plt.show()
#4
I_med = cv2.medianBlur(Is,3)
cv2.imshow("anh lam tron", I_med)
#5
threhold, Ib = cv2.threshold(Is,125,255,cv2.THRESH_OTSU)
cv2.imshow("anh OTSU",Ib)
#6
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

cv2.waitKey()
cv2.destroyAllWindows()


