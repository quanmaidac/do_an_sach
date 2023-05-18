import cv2
import numpy as np

I= cv2.imread('I04.jpg')
cv2.imshow('I04.jpg',I)
# print('chieu cao: ',I.shape[0])
# print('chieu rong: ',I.shape[1])
# print('so kenh: ',I.shape[2])
# print('so kenh: ', len(I.shape))

# cv2.imshow('Kenh B',I[:,:,0])
# cv2.imshow('Kenh G',I[:,:,1])
# cv2.imshow('Kenh R',I[:,:,2])

# print('Muc sang trung binh cua kenh R: ', np.mean(I[:,:,2]))
# print('Muc sang lon nhat cua kenh R: ', np.max(I[:,:,2]))
# print('Muc sang nho nhat cua kenh R: ', np.min(I[:,:,2]))
 
# Igray = cv2.cvtColor(I,cv2.COLOR_BGR2GRAY)
# cv2.imshow('anh xam 1',Igray)
# B, G, R = I[:,:,0], I[:,:,1], I[:,:,2]
# Ig = B*0.11 + G*0.5 + R*0.39
# Ig = Ig
# cv2.imshow('anh xam 2',Ig)

# Ihsv = cv2.cvtColor(I,cv2.COLOR_BGR2HSV)
# cv2.imshow('anh hsv',Ihsv)
# cv2.imshow('Kenh H',I[:,:,0])
# cv2.imshow('Kenh S',I[:,:,1])
# cv2.imshow('Kenh V',I[:,:,2])
# print('muc sang trung binh: ', np.mean(Ihsv[:,:,2]))
# Ihsv[:,:,0]=0
# I2= cv2.cvtColor(Ihsv,cv2.COLOR_HSV2BGR)
# cv2.imshow('bien doi nguoc', I2)

Ig = cv2.cvtColor(I,cv2.COLOR_BGR2GRAY)
nguong_OTSU, I_OTSU = cv2.threshold(Ig,93,255,cv2.THRESH_OTSU)
print('nguong OTSU = ',nguong_OTSU)
cv2.imshow("nhi phan OTSU",I_OTSU)

cv2.waitKey(0)
cv2.destroyAllWindows()
