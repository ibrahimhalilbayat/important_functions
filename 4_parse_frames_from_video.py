'''
Script to parse the frames 
by 
Dark Lord İbrahim Halil BAYAT
Fearless, Nameless, Formless and other -less stuff

-----------------------------------------------------
Steps:
    1- Save this python file under the same directory 
       of the videos (avi format)
    2- On the shell run: 'python parse_frames.py'
    3- Go and live a happy day 
'''

import os
import cv2

def FrameCapture(out_path, video_file):
    '''
    Method to parse the frames of a avi extensioned video.
    Input:
        out_path: Output path to save the parsed frames
        video_file: Vide file to be parsed
    Returns:
        Creates a folder with the same name as the video file
        and save the parsed frames into that folder.
    '''
    
    video_object = cv2.VideoCapture(video_file)
    count = 0
    success = True
    video_name = video_file.split('.')[0]
    
    while success:

        video_object.set(cv2.CAP_PROP_POS_MSEC,(count*50))
        success, frame = video_object.read()
        if frame is not None:
            try:
                parsed_frame_name = out_path + "/"  + video_name + '_frame_' + str(count) + '.jpeg'
                cv2.imwrite(parsed_frame_name, frame)
                count += 1
            except Exception as e:
                print("An execption occured in FrameCapture...", e)
            finally:
                print(f"Parsing {video_file} is DONE like the rest of our happy days...")


THE_PATH = os.getcwd()
print("The Path: ", THE_PATH)

for avi_file in os.listdir():
    if avi_file.endswith('.avi'):
        folder_name = avi_file.split(".")[0]
        if folder_name not in os.listdir():
            os.mkdir(folder_name)
        FrameCapture(out_path=folder_name, video_file=avi_file)
