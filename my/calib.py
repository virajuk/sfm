from __future__ import print_function

# built-in modules
import os

# hello test

import numpy as np
import cv2

chessboardSize = (9, 6)

imgL = cv2.imread('images/imageL0.png')
imgR = cv2.imread('images/imageR5.png')

grayL = cv2.cvtColor(imgL, cv2.COLOR_BGR2GRAY)
grayR = cv2.cvtColor(imgR, cv2.COLOR_BGR2GRAY)

# Find the chess board corners
retL, cornersL = cv2.findChessboardCorners(grayL, chessboardSize, None)
retR, cornersR = cv2.findChessboardCorners(grayR, chessboardSize, None)

objp = np.zeros((chessboardSize[0] * chessboardSize[1], 3), np.float32)
# print(objp)
objp[:, :2] = np.mgrid[0:chessboardSize[0],0:chessboardSize[1]].T.reshape(-1, 2)
# print(objp.shape)
objp = objp * 20
# print(objp)
# exit(0)

if retR and retL:

    for corner_l, corner_r in zip(cornersL, cornersR):

        # Draw and display the corners
        cv2.drawChessboardCorners(imgL, chessboardSize, cornersL, retL)
        cv2.imshow('img left', imgL)
        cv2.drawChessboardCorners(imgR, chessboardSize, cornersR, retR)
        cv2.imshow('img right', imgR)


# cv2.imshow("LEFT", grayL)
# cv2.imshow("RIGHT", grayR)
cv2.waitKey(0)

cv2.destroyAllWindows()
