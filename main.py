import cv2, keyboard, threading, ctypes, time, os



base = os.path.expanduser('~') # Base Path C:\\Users\\<User>
image = [
    base + "\\Pictures\\Screenshots\\narcissistic_bg.png", # Image 1
    base + "\\Pictures\\Screenshots\\narcissistic_bg2.png" # Image 2
]
switch = 0 # Image Switch


exit_flag = False
def exit_kod():
    global exit_flag
    keyboard.add_hotkey("shift+f3", lambda: set_exit()) # Exit Key Input
def set_exit():
    global exit_flag
    exit_flag = True



def set_background():
    global switch
    last = 0 # last Image Switch
    if(switch == 0):
        switch = 1 # Update Switch
    else:
        switch = 0 # Reset Switch
        last = 1

    # Set Background
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image[switch], 0)

def main():
    cap = cv2.VideoCapture(0) # Video Source

    # Starts Exit Listening Thread
    thread = threading.Thread(target=exit_kod, args=())
    thread.daemon = True
    thread.start()


    # Capture Frames
    while(True):
        start_time = time.time()  # Start Time Record
        ret, frame = cap.read() # Read Frame

        # Save image as .PNG
        cv2.imwrite(image[switch], frame)
        set_background() # Background Change


        if(exit_flag): break
        time.sleep(0.1) # Delay

    # Cleanup
    cap.release()



if __name__ == "__main__":
    main()
