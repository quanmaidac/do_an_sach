import cv2
import numpy as np

I = cv2.imread('anh2.jpg')
cv2.imshow('anh goc',I)
B, G, R = I[:,:,0], I[:,:,1], I[:,:,2]
Ig = 0.39 * B + 0.5 * G + 0.11 * R
cv2.imshow("Anh cap sang",Ig)
print('Muc xam trung binh:', np.mean(Ig))
print('Muc xam lon nhat:', np.max(Ig))

sobelx = cv2.Sobel(I,ddepth=cv2.CV_64F, dx=1, dy=0, ksize=1)  # tìm biên sobel đạo hàm theo x
sobely = cv2.Sobel(I,cv2.CV_64F,0,1,ksize=1)  #  tìm biên sobel đạo hàm the y
cv2.imshow('sobel x',sobelx)
cv2.imshow('sobel y',sobely)

img_gaussian = cv2.GaussianBlur(Ig, (5, 5), 0)

Icanny = cv2.Canny(image=I, threshold1=100, threshold2=200) # tìm biên theo Canny 
cv2.imshow('Anh canny',Icanny)

threshold, Ib = cv2.threshold(Ig, 150, 255, cv2.THRESH_BINARY)
cv2.imshow("Nhi phan nguong 150",Ib)

cv2.waitKey()
cv2.destroyAllWindows()