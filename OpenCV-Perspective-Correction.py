#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 11:00:41 2024

@author: mac
"""

import cv2  # dakhlina cv2 (OpenCV) bash n3mlou traitements 3la l-swir
import numpy as np  # dakhlina numpy bash n3mlou hssabat

image_path = "/Users/mac/Downloads/plaka.jpg"  # hadi hia path dyal taswira
image = cv2.imread(image_path)  # qrina taswira mn l-path li 3tina

if image is None:
    raise ValueError("resim yuklenemedi")  # ila ma l9ina taswira, ntl3ou erreur

pts1 = np.float32([[22, 69],  [356, 44],[22, 130], [347, 190]])  # hadou points dyal l-corner dyal l-object f l-original image
pts2 = np.float32([[0, 0], [400, 0], [0, 300], [408, 300]])  # w hadou points dyal l-corner li bghina ndiro f l-output image

M = cv2.getPerspectiveTransform(pts1, pts2)  # khdina transformation matrix bash nbdlo perspective

dst = cv2.warpPerspective(image, M, (400, 300))  # applayina l-transformation 3la taswira

cv2.imshow("perspecf duzeltme", dst)  # nwrriw taswira jdida
cv2.waitKey(0)  # ntsnaw press 3la chi button bach tghlaq l-window
cv2.destroyAllWindows()  # nghlqou ga3 l-windows li fethin

output_path = "plate_corrected.png"  # hadi hia l-path li bghina nsaveiw fiha l-taswira l-mmodifa
cv2.imwrite(output_path, dst)  # nsaveiw taswira l-jdida f l-path
output_path  # njibou l-path dyal taswira l-jdida
