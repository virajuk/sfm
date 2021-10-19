from __future__ import print_function

import os

import numpy as np
import cv2

from glob import glob


class Calibrate:

    def __init__(self):

        self.chess_board_size = (9, 6)
        self.objp_init()
        self.object_points, self.image_points_left, self.image_points_right = [], [], []
        self.criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)       # termination criteria
        self.frame_image_size = (2268, 1940, 3)

    def objp_init(self):

        self.objp = np.zeros((self.chess_board_size[0] * self.chess_board_size[1], 3), np.float32)
        self.objp[:, :2] = np.mgrid[0:self.chess_board_size[0], 0:self.chess_board_size[1]].T.reshape(-1, 2)
        self.objp = self.objp*20

    def __read_images_from_dir_and_sort(self):

        self.images_left = sorted(glob(('images/left/*.png')))
        self.images_right = sorted(glob(('images/right/*.png')))

    def iterate_images(self):

        self.__read_images_from_dir_and_sort()

        for image_left, image_right in zip(self.images_left, self.images_right):

            image_left = cv2.imread(image_left)
            image_right = cv2.imread(image_right)

            print("converting images to gray")
            gray_left = cv2.cvtColor(image_left, cv2.COLOR_BGR2GRAY)
            gray_right = cv2.cvtColor(image_right, cv2.COLOR_BGR2GRAY)

            print("finding chessboard corners")
            return_left, corners_left = cv2.findChessboardCorners(gray_left, self.chess_board_size, None)
            return_right, corners_right = cv2.findChessboardCorners(gray_right, self.chess_board_size, None)

            # If found, add object points, image points (after refining them)
            print(return_left, return_right)
            if return_left and return_right:

                self.object_points.append(self.objp)

                print("finding corner subpixels")
                corners_left = cv2.cornerSubPix(gray_left, corners_left, (11, 11), (-1, -1), self.criteria)
                self.image_points_left.append(corners_left)

                corners_right = cv2.cornerSubPix(gray_right, corners_right, (11, 11), (-1, -1), self.criteria)
                self.image_points_right.append(corners_right)

                # Draw and display the corners
                cv2.drawChessboardCorners(image_left, self.chess_board_size, corners_left, return_left)
                cv2.imshow('img left', self.__resize_image(image_left, 100))
                cv2.drawChessboardCorners(image_right, self.chess_board_size, corners_right, return_right)
                cv2.imshow('img right', self.__resize_image(image_right, 100))
                cv2.waitKey(0)
                cv2.destroyAllWindows()

    @staticmethod
    def __resize_image(image, scale):

        scale_percent = scale  # percent of original size
        width = int(image.shape[1] * scale_percent / 100)
        height = int(image.shape[0] * scale_percent / 100)
        dim = (width, height)

        # resize image
        return cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

    def calibrate(self):

        return_left, camera_matrix_left, dist_left, rvecs_left, tvecs_left = cv2.calibrateCamera(self.object_points, self.image_points_left, self.frame_image_size[:2], None, None)
        new_camera_matrix_left, roi_left = cv2.getOptimalNewCameraMatrix(camera_matrix_left, dist_left, (self.frame_image_size[1], self.frame_image_size[0]), 1, (self.frame_image_size[1], self.frame_image_size[0]))

        print(rvecs_left)
        print(tvecs_left)

        # print(camera_matrix_left)
        # print(new_camera_matrix_left)

        return_right, camera_matrix_right, dist_right, rvecs_right, tvecs_right = cv2.calibrateCamera(self.object_points, self.image_points_right, self.frame_image_size[:2], None, None)
        new_camera_matrix_right, roi_right = cv2.getOptimalNewCameraMatrix(camera_matrix_right, dist_right, (self.frame_image_size[1], self.frame_image_size[0]), 1, (self.frame_image_size[1], self.frame_image_size[0]))

        print(rvecs_left)
        print(tvecs_left)

        # print(camera_matrix_right)
        # print(new_camera_matrix_right)

# chessboardSize = (9, 6)
#
# imgL = cv2.imread('images/imageL0.png')
# imgR = cv2.imread('images/imageR5.png')
#
# grayL = cv2.cvtColor(imgL, cv2.COLOR_BGR2GRAY)
# grayR = cv2.cvtColor(imgR, cv2.COLOR_BGR2GRAY)
#
# # Find the chess board corners
# retL, cornersL = cv2.findChessboardCorners(grayL, chessboardSize, None)
# retR, cornersR = cv2.findChessboardCorners(grayR, chessboardSize, None)
#
# objp = np.zeros((chessboardSize[0] * chessboardSize[1], 3), np.float32)
# objp[:, :2] = np.mgrid[0:chessboardSize[0], 0:chessboardSize[1]].T.reshape(-1, 2)
# objp = objp * 20
#
# if retR and retL:
#
#     for corner_l, corner_r in zip(cornersL, cornersR):
#
#         # Draw and display the corners
#         cv2.drawChessboardCorners(imgL, chessboardSize, cornersL, retL)
#         cv2.imshow('img left', imgL)
#         cv2.drawChessboardCorners(imgR, chessboardSize, cornersR, retR)
#         cv2.imshow('img right', imgR)
#
#
# # cv2.imshow("LEFT", grayL)
# # cv2.imshow("RIGHT", grayR)
# cv2.waitKey(0)
#
# cv2.destroyAllWindows()


if __name__ == '__main__':

    calib = Calibrate()
    calib.iterate_images()

    # calib.calibrate()

    # cv2.destroyAllWindows()
