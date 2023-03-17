import matplotlib.pyplot as plt
import numpy as np
from skimage import transform
import cv2


image = cv2.imread() # Enter the image path


points_of_interest = []

def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f'({x}, {y}')
        cv2.circle(image, (x,y), 3, (0,255,255), -1)
        points_of_interest.append([x,y])

cv2.namedWindow("Point Coordinates")

cv2.setMouseCallback("Point Coordinates", click_event)
print("""
Click once to the points in the direction of 
upper-right
lower-right
lower-left
uper-right

Then click escape.""")
while True:
    cv2.imshow("Point Coordinates", image)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

print(points_of_interest)
cv2.destroyAllWindows()

projection = np.array([[500, 200],
                       [500, 390],
                       [100, 390],
                       [100, 200]])
points_of_interest = np.array(points_of_interest)


tform = transform.estimate_transform('projective', points_of_interest, projection)
tf_img_warp = transform.warp(image, tform.inverse, mode = 'symmetric')
plt.figure(num=None, figsize=(8, 6), dpi=80)
fig, ax = plt.subplots(1,2, figsize=(15, 10), dpi = 80)
ax[0].set_title(f'Original', fontsize = 15)
ax[0].imshow(image)
ax[0].set_axis_off()
ax[1].set_title(f'Transformed', fontsize = 15)
ax[1].imshow(tf_img_warp)
ax[1].set_axis_off()
plt.show()
