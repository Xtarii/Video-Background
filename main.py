from src import auto_start, video # Local Imports
import os, win32api, win32gui, win32con, time



BASE = os.path.expanduser('~') # Base Path C:\\Users\\<User>
NAME = "Narcissistic Background" # Application Base Name
PATH = os.path.abspath(__file__) # Script Path
STARTUP_PATH = BASE + "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"

background = None



def wndproc(hwnd, msg, wparam, lparam):
    background.cleanup()



if __name__ == "__main__":
    auto_start.add_to_autostart(STARTUP_PATH, NAME,
        BASE + '\\Desktop\\Narcissistic Background.exe') # Adds to Autostart

    # Main Application
    background = video.VideoCapture(BASE)
    background.start() # Starts Application

    hinst = win32api.GetModuleHandle(None)
    wndclass = win32gui.WNDCLASS()
    wndclass.hInstance = hinst
    wndclass.lpszClassName = "narWindowClass"
    messageMap = {
        win32con.WM_QUERYENDSESSION : wndproc,
        win32con.WM_ENDSESSION : wndproc,
        win32con.WM_QUIT : wndproc,
        win32con.WM_DESTROY : wndproc,
        win32con.WM_CLOSE : wndproc
    }

    wndclass.lpfnWndProc = messageMap


    myWindowClass = win32gui.RegisterClass(wndclass)
    hwnd = win32gui.CreateWindowEx(
        win32con.WS_EX_LEFT,
        myWindowClass,
        "narMsgWindow",
        0,
        0,
        0,
        win32con.CW_USEDEFAULT,
        win32con.CW_USEDEFAULT,
        0,
        0,
        hinst,
        None
    )

    while True:
        win32gui.PumpWaitingMessages()
        time.sleep(1)
