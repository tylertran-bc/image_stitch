import cv2

image_paths =['1.jpg','2.jpg']
img_list = [] 

for image_path in image_paths:
    img = cv2.imread(image_path)
    img = cv2.resize(img, (0,0), fx=0.2, fy=0.2)
    img_list.append(img)

# Test to see if images are showing
cv2.imshow('image1',img_list[0])
cv2.imshow('image2', img_list[1])
    


stitchy = cv2.Stitcher.create()
(status, stitched) = stitchy.stitch(img_list)

if stitched != None:
    print("Stitching...")
    cv2.imshow("Stitched", stitched)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print(f"Stitch failed: status code {status}")