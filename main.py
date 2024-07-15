from src import auto_start, video # Local Imports
import os



BASE = os.path.expanduser('~') # Base Path C:\\Users\\<User>
NAME = "Narcissistic Background" # Application Base Name
PATH = os.path.abspath(__file__) # Script Path
STARTUP_PATH = BASE + "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"



if __name__ == "__main__":
    auto_start.add_to_autostart(STARTUP_PATH, NAME,
        BASE + '\\Desktop\\Narcissistic Background.exe') # Adds to Autostart

    # Main Application
    background = video.VideoCapture(BASE)
    background.start() # Starts Application
