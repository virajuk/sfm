from __future__ import print_function

# built-in modules
import os

import numpy as np
import cv2

chessboardSize = (9, 6)

grayL = cv2.cvtColor(cv2.imread('images/imageL5.png'), cv2.COLOR_BGR2GRAY)
grayR = cv2.cvtColor(cv2.imread('images/imageR5.png'), cv2.COLOR_BGR2GRAY)

# Find the chess board corners
retL, cornersL = cv2.findChessboardCorners(grayL, chessboardSize, None)
retR, cornersR = cv2.findChessboardCorners(grayR, chessboardSize, None)

print(np.mgrid[0:chessboardSize[0],0:chessboardSize[1]].T.reshape(-1, 2))

objp = np.zeros((chessboardSize[0] * chessboardSize[1], 3), np.float32)
# print(objp)
objp[:, :2] = np.mgrid[0:chessboardSize[0],0:chessboardSize[1]].T.reshape(-1, 2)
print(objp)
objp = objp * 20
# print(objp)

exit(0)

if retR and retL:

    for corner_l, corner_r in zip(cornersL, cornersR):

        center_coordinates_l = (int(corner_l[0][0]), int(corner_l[0][1]))
        cv2.circle(grayL, center_coordinates_l, radius=10, color=(255, 0, 0), thickness=2)

        center_coordinates_r = (int(corner_r[0][0]), int(corner_r[0][1]))
        cv2.circle(grayR, center_coordinates_r, radius=10, color=(255, 0, 0), thickness=2)


cv2.imshow("LEFT", grayL)
cv2.imshow("RIGHT", grayR)
cv2.waitKey(0)

cv2.destroyAllWindows()
