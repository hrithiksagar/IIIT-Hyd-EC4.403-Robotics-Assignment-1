import matplotlib.pyplot as plt
import math
import random
import numpy as np
from matplotlib.lines import Line2D
import itertools
import os
import cv2
print("imported openCV")

## Helper function to generate video from individual frames.
def frames_to_video(input_path, output_path, fps):
    '''
        Function to Concatenate given frames and fps into a video file.
        Input Arguments
        input_path  : Path to the input directory containing input frames
        output_path : Path to the output directory containing the video file
        fps         : Frames per Second of the output video
        Return
        Boolean     : True is Video written successfully, False if writing is not successful.
    '''
    image_files = [file for file in os.listdir(input_path) if file.endswith('.png') or file.endswith('jpg')]
    image_files.sort()

    frames = []
    # size = None 

    for file in image_files:
        f = os.path.join(input_path, file)
        frame = cv2.imread(f)
        height, width, channels = frame.shape
        size = (width, height)
        frames.append(frame)

    # video_writer = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
    video_writer = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'MP4V'), fps, size)


    for frame in frames:
        video_writer.write(frame)

    video_writer.release()
    print("done")
    return True

# frames_to_video("./results","./results/plot.mp4", 25)

output_directory = "/Users/hrithik/Library/Mobile Documents/com~apple~CloudDocs/iCloud Downloads/IIITH PGSSP/#S24/Robotics P&N/Robotics_Assign1/Main/results/Videos/"

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

frames_to_video("/Users/hrithik/Library/Mobile Documents/com~apple~CloudDocs/iCloud Downloads/IIITH PGSSP/#S24/Robotics P&N/Robotics_Assign1/Main/results/nonholonomic_path", 
                os.path.join(output_directory, "nonholonomic_path.mp4"), 25)
