# VideoFrameReaderPY
Extracts a video's frame incrementally. Commonly used for Gimmick accs on Twitter

# Importing the module
```py
## Works as a module, so you can call 
from {whatever_you_called_the_file} import VideoFrameUtil
```

# Propreties
```py
self.cap = cv2.VideoCapture(self.video_path) ## USE THIS ONE IF YOU KNOW WHAT YOU ARE DOING
       
self.current_frame = 0
self.frame_rate = self.cap.get(cv2.CAP_PROP_FPS)
self.frame_total = self.cap.get(cv2.CAP_PROP_FRAME_COUNT)
```

# Methods

## Create a VideoReader Object
```py
## Have to be set localy, so video file and output folder in the same directory as the script.
VideoReader = VideoFrameUtil("test.mp4", "output")
```

## Convert time (in seconds) to frames

```py
## Start and get the closest frame at 3.1 seconds
start = self.SecondsToFrame(3.1) 
```

## Place reader to a certain frame
```py
VideoReader.SetCurrentFrame(0) ## Place at the begining
```

## Get Frames for a intervall of time
```py
frames_1 = VideoReader.GetFramesForTime(1, 3)
```

## Get All frames directly 
```py
frames_all = VideoReader.GetAllFrames()
```

## Get all frames and do things in real time

```py
VideoReader.SetCurrentFrame(0)
while True:
    data = VideoReader.GetNextFrame()

    path = data[0]
    image = data[1]
    ## Do whatever you want, keep reference to the image and add it to the Media Array when tweeting for example.
```

## Close the reader
```py
## Its important to close the reader whenever you are done, to save memory and keep it clean.
VideoReader.Close() 
```
