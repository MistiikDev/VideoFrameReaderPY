import cv2
import os
import numpy as np 

from math import *

class VideoFrameUtil:
    def __init__(self, video_name, output_folder): 
        ## Get references to all paths
        script_directory = os.path.dirname(os.path.abspath(__file__))
        video_file = os.path.join(script_directory, video_name)
        output_folder = os.path.join(script_directory, output_folder)

        if not output_folder or not video_file:
            return print("Could not find video file or output directory references localy.")

        ## Create new path if folder does not exist
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        self.video_path = video_file
        self.output_folder = output_folder
        self.cap = cv2.VideoCapture(self.video_path)
       
        ## Get Framerate and Frame count from video file
        self.current_frame = 0
        self.frame_rate = self.cap.get(cv2.CAP_PROP_FPS)
        self.frame_total = self.cap.get(cv2.CAP_PROP_FRAME_COUNT)

    def SetCurrentFrame(self, frame):
        self.current_frame = frame

    def GetNextFrame(self):
        self.cap.set(cv2.CAP_PROP_POS_FRAMES, self.current_frame) ## Place CAP on current frame
        wasRead, output_frame = self.cap.read() 

        if not wasRead: ## Something went wrong reading the frame
            return print(f"Something went wrong while trying to read frame number : {self.current_frame}.")
       
        ## Write image and save the image file locally
        output_file = os.path.join(self.output_folder, f"frame_{self.current_frame}.png")
        cv2.imwrite(output_file, output_frame) 

        self.current_frame += 1

        print(f"Saved frame number { self.current_frame } / { self.frame_total }.")

        return [output_file, output_frame]
    def SecondsToFrame(self, s):
        if self.frame_total:
            return int(min((s * 60), self.frame_total))
        else:
            return s*60

    def GetFramesForTime(self, s, d):
        frames = []
        start = self.SecondsToFrame(s)
        duration = self.SecondsToFrame(d)

        self.SetCurrentFrame(start)

        while self.current_frame < duration:
            data = self.GetNextFrame()

            frames.append(data)
        return frames
    
    def GetAllFrames(self):
        frames = []
        self.SetCurrentFrame(0)

        while self.current_frame < self.frame_total:
            data = self.GetNextFrame()

            frames.append(data)
        return frames
    
    def Close(self):
        self.cap.release() ## Release CAP pointer (release futur unused memory)
