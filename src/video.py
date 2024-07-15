import cv2, time
import ctypes, ctypes.wintypes



# Video Capture ( Background )
class VideoCapture:
    def __init__(self, base):
        self.switch = 0 # Image Switch
        self.IMAGE = [
            base + "\\Pictures\\Screenshots\\narcissistic_bg.png", # Image 1
            base + "\\Pictures\\Screenshots\\narcissistic_bg2.png" # Image 2
        ]


        # Video Capture
        self.cap = cv2.VideoCapture(0) # Video Source


    # Set Background
    def set_background(self):
        last = 0 # last Image Switch
        if(self.switch == 0):
            self.switch = 1 # Update Switch
        else:
            self.switch = 0 # Reset Switch
            last = 1

        # Set Background
        ctypes.windll.user32.SystemParametersInfoW(20, 0, self.IMAGE[self.switch], 0)


    # Cleanup
    def cleanup(self):
        # Cleanup
        self.cap.release()


    # Start
    def start(self):
        try:
            # Capture Frames
            while(True):
                ret, frame = self.cap.read() # Read Frame

                # Save image as .PNG
                cv2.imwrite(self.IMAGE[self.switch], frame)
                self.set_background() # Background Change
                time.sleep(0.1) # Delay

        finally:
            self.cleanup() # Cleanup
