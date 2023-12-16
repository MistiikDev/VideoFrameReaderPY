# VideoFrameReaderPY
Extracts a video's frame incrementally. Commonly used for Gimmick accs on Twitter

# Documentation

## Create a VideoReader Object
```py
VideoReader = VideoFrameUtil("test.mp4", "output") ## have to be set localy, so video file and output folder in the same directory as the script.
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
