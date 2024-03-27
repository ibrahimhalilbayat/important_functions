""""
This script is used to create binary masks from json file
obstacle: 0
sea: 1
sky: 2
ignore_region: 4
"""

import os
import cv2
import json
import numpy as np

JSON_PATH = 'json/'
if 'masks' not in os.listdir():
    os.mkdir('masks')
MASK_PATH = 'masks/'

for data in os.listdir(JSON_PATH):
    with open(JSON_PATH+data) as file:
        json_file = json.load(file)
    MASK_WIDTH = json_file['imageWidth']				    
    MASK_HEIGHT = json_file['imageHeight']

    mask = np.zeros((MASK_HEIGHT,MASK_WIDTH)) + 4 # Creating ignore region

    for index in range(len(json_file['shapes'])):
        class_name = json_file['shapes'][index]['label']
        points = np.array(json_file['shapes'][index]['points'], dtype='int32')
        
        if class_name == 'obstacle':
            mask = cv2.fillPoly(mask, pts=[points], color=(0))
        
        elif class_name == 'sea' or class_name == 'water':
            mask = cv2.fillPoly(mask, pts=[points], color=(1))
        
        elif class_name == 'sky':
            mask = cv2.fillPoly(mask, pts=[points], color=(2))
        
        elif class_name == 'ignore_region' or class_name == 'ignore region':
            mask = cv2.fillPoly(mask, pts=[points], color=(4))
    
    file_name = data.split('.')[0]
    
    cv2.imwrite(MASK_PATH+file_name+'m.jpeg', mask)
    
    print(file_name+'.jpeg is SAVED to ', MASK_PATH)
