import os
import cv2

img_array = []

for image in sorted(os.listdir('output/')):
    img = cv2.imread('output/'+image)
    height, width, layers =  img.shape
    size = (width, height)
    img_array.append(img)

out = cv2.VideoWriter('output_video.mp4',cv2.VideoWriter_fourcc(*'DIVX'), 30, size)

for i in range(len(img_array)):
    out.write(img_array[i])
out.release()
