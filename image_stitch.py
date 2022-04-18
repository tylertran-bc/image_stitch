"""
Syntax: python/3 image_stitch.py [IMAGE FOLDER]
"""

import cv2
import os
import sys

ip_folder = sys.argv[1]
os.chdir(ip_folder)

image_paths = [f for f in os.listdir('.') if f.lower().endswith('result.png')]

# image_paths=['1_test_calibresult.png','2_test_calibresult.png']
# initialized a list of images
imgs = []
 
for i in range(len(image_paths)):
    imgs.append(cv2.imread(image_paths[i]))
    imgs[i]=cv2.resize(imgs[i],(0,0),fx=0.4,fy=0.4)
    # this is optional if your input images isn't too large
    # you don't need to scale down the image
    # in my case the input images are of dimensions 3000x1200
    # and due to this the resultant image won't fit the screen
    # scaling down the images
# showing the original pictures
cv2.imshow('1',imgs[0])
cv2.imshow('2',imgs[1])

# Test to see the function call to read the image is successful
print(imgs)
print(imgs[0].shape)

stitchy=cv2.Stitcher.create()
dummy, output = stitchy.stitch(imgs)
 
if dummy != cv2.STITCHER_OK:
  # checking if the stitching procedure is successful
  # .stitch() function returns a true value if stitching is
  # done successfully
    print(f"stitching ain't successful (Status: {dummy})")
else:
    print('Your Panorama is ready!!!')
 
cv2.imshow('output', output)
cv2.imwrite('stitch_out.png', output)
 
cv2.waitKey(0)




#First Try/Method
# import cv2

# image_paths =['1.jpg','2.jpg']
# img_list = [] 

# for image_path in image_paths:
#     img = cv2.imread(image_path)
#     img = cv2.resize(img, (0,0), fx=0.2, fy=0.2)
#     img_list.append(img)

# # Test to see if images are showing
# cv2.imshow('image1',img_list[0])
# cv2.imshow('image2', img_list[1])
    


# stitchy = cv2.Stitcher.create()
# (status, stitched) = stitchy.stitch(img_list)

# if stitched != None:
#     print("Stitching...")
#     cv2.imshow("Stitched", stitched)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
# else:
#     print(f"Stitch failed: status code {status}")