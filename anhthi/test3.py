import cv2
import numpy as np
import matplotlib.pyplot as plt

I = cv2.imread('I04.jpg')
cv2.imshow('I04.jpg',I)
I2 = cv2.resize(I,(512,256))
cv2.imshow('Anh resize', I2)

#chuyen doi sang HSV
Ihsv=cv2.cvtColor(I,cv2.COLOR_BGR2HSV)
#Hien thi kenh V
cv2.imshow('Kenh V', Ihsv[:,:,2])

I_gray = cv2.cvtColor(I,cv2.COLOR_BGR2GRAY)
cv2.imshow('Anh xam', I_gray)
I_copy = I.copy()
img_gaussian = cv2.GaussianBlur(I, (5, 5), 0)
cv2.imshow('gaussian',img_gaussian)

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

print('Kênh S')
Is=I[:,:,1]
hS=tinh_hist(Is)
plt.plot(hS)
plt.show()

I_gray=cv2.cvtColor(I,cv2.COLOR_BGR2GRAY)
cv2.imshow('Anh Cap Xam',I_gray)

I_new = I.copy()
I_new[:,:,2]=cv2.equalizeHist(I[:,:,2])

cv2.imshow('Anh Can Bang',I_new)

h_n,s_n,v_n = cv2.split(I_new)
def tinh_hist_new(g_n):
    a=np.zeros(256,dtype='int')
    h=g_n.shape[0]
    w=g_n.shape[1]
    for i in range(h):
        for j in range(w):
             g=g_n[i][j]
             a[g]=a[g]+1
    return a

print('Kênh V_new')
Iv_new=I_new[:,:,2]
hV_new=tinh_hist(Iv_new)
plt.plot(hV_new)
plt.show()

I4 = cv2.cvtColor(I_new,cv2.COLOR_HSV2BGR)
cv2.imshow('new img',I4)

cv2.waitKey()
cv2.destroyAllWindows()