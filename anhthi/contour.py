import cv2
import numpy as ns
I=cv2.imread('tao.jpg')
cv2.imshow('Anh Goc',I)

Igray = cv2.cvtColor(I,cv2.COLOR_BGR2GRAY)
cv2.imshow('anh gray',Igray)

thresh, I_bina = cv2.threshold(Igray, 180, 255, cv2.THRESH_BINARY)
cv2.imshow('anh nhi phan nguong 180', I_bina)

thresh, I_binary = cv2.threshold(Igray, 180, 255, cv2.THRESH_BINARY)
I_binary = 255 - I_binary
cv2.imshow('nen den contours', I_binary)

#tim contour cua anh
I_copy = I.copy()
contours, hierarchy = cv2.findContours(I_binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(I_copy, contours, -1, (255,0,0), 3)
cv2.imshow('Anh contours',I_copy)

#loai bo contour be
I_copy2 = I.copy()
for contour in contours:
    if cv2.contourArea(contour) > 5000:
        cv2.drawContours(I_copy2, [contour], -1, (0,255,0), 3)
cv2.imshow('Loai bo contours be',I_copy2)

cv2.waitKey()
cv2.destroyAllWindows()