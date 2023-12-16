import cv2
import os

def extract_frames(video_path, output_folder):
    cap = cv2.VideoCapture(video_path)

    ## Handle exception, possibly not setup correctly
    if not cap.isOpened():
        print("Error: Unable to open video file.")
        return

    ## Get Framerate and Framecount from videofile
    frame_rate = cap.get(cv2.CAP_PROP_FPS)
    frame_total = cap.get(cv2.CAP_PROP_FRAME_COUNT)

    ## Create new path if folder does not exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    ## Initiate frame counter (First frame is 0)
    frame_count = 0

    while True:
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_count) ## Place CAP on current frame
        wasRead, frame = cap.read() 

        if not wasRead: ## Something went wrong reading the frame
            break

        ## Write image and save the image file locally
        output_file = os.path.join(output_folder, f"frame_{frame_count}.png")
        cv2.imwrite(output_file, frame) 

        frame_count += 1

        print(f"Saved frame number { frame_count } / { frame_total }.")

    cap.release() ## Release CAP pointer

## Get local directories
script_directory = os.path.dirname(os.path.abspath(__file__))

video_file = os.path.join(script_directory, "test.mp4")
output_folder = os.path.join(script_directory, "output")

## START
extract_frames(video_file, output_folder)
