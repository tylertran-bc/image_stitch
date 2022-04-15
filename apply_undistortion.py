import sys
import os
import shutil
import numpy as np
import cv2

ip_folder = sys.argv[1]

# Changing directory to the input folder
os.chdir(ip_folder)

files = [f for f in os.listdir('.') if f.lower().endswith('.jpg')]
print("Applying undistortion to files: ", files)

# first try; old lens
# camera_matrix = np.array(
#     [
#         [3.74441547e03, 0.00000000e00, 1.53066087e03],
#         [0.00000000e00, 3.75135620e03, 1.96412368e03],
#         [0.00000000e00, 0.00000000e00, 1.00000000e00],
#     ]
# )
# dist = np.array([[-0.53275606, 0.3987033, 0.00368589, -0.00144038, -0.26369688]])

# new lens
camera_matrix = np.array(
    [
        [3.92511397e03, 0.00000000e00, 1.47487866e03],
        [0.00000000e00, 3.93152476e03, 2.11156451e03],
        [0.00000000e00, 0.00000000e00, 1.00000000e00],
    ]
)
dist = np.array([[-0.3776641, 0.10621045, -0.00358364, 0.00110551, 0.03084146]])

for f in files: 
    img = cv2.imread(f)
    height, width = img.shape[:2]
    new_camera_matrix, roi = cv2.getOptimalNewCameraMatrix(camera_matrix, dist, (width, height), 1, (width, height))

    xy_maps = cv2.initUndistortRectifyMap(camera_matrix, dist, None, new_camera_matrix, (width, height), 5)
    # xy_maps is consistent for all images and thus could be cached

    dst = cv2.remap(img, *xy_maps, cv2.INTER_LINEAR)
    x, y, w, h = roi
    dst = dst[y : y + h, x : x + w]
    cv2.imwrite(f.split('.')[0] + "_calibresult.jpg", dst)
    