import cv2 
import os
  
def FrameCapture(path): 
    
    vidObj = cv2.VideoCapture(path) 
    
    count = 0
    
    success = 1

    os.chdir("./init_frames/")
  
    while success: 

        success, image = vidObj.read() 
  
        cv2.imwrite("frame%d.jpg" % count, image)
        print(count)
  
        count += 1
  
if __name__ == '__main__': 

    FrameCapture("bad_apple.mp4")
