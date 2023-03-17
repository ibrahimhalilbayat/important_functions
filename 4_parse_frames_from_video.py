'''
Script to parse the frames 
by 
Dark Lord İbrahim Halil BAYAT
Fearless, Nameless, Formless and other -less stuff
'''

import os
import cv2

def FrameCapture(in_path, out_path, video_file):
    
    video_object = cv2.VideoCapture(in_path + video_file)
    count = 0
    success = True
    video_name = video_file.split('.')[0]
    
    while success:

        video_object.set(cv2.CAP_PROP_POS_MSEC,(count*1000))
        success, frame = video_object.read()
        try:
            cv2.imwrite(out_path  + video_name + '_frame_' + str(count) + '.jpeg', frame)
            count += 1
        except:
            print("An execption occured in FrameCapture...")
	
for video_file in os.listdir("09_03_2023/short_forms"):
    print("Video File: ", video_file)
    
    FrameCapture("09_03_2023/short_forms/", "09_03_2023_frames/", video_file)
    print(video_file, " is parsed")
