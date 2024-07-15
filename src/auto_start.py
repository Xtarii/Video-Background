import os



# Checks if Application is in Autostart
def check_autostart(STARTUP_PATH: str, NAME: str):
    return os.path.exists(os.path.join(STARTUP_PATH, NAME + ".bat")) # Check if Startup

def add_to_autostart(STARTUP_PATH: str, NAME: str, PATH: str):
    # Check if This application already is in Autostart
    if(not check_autostart(STARTUP_PATH, NAME)):
        shortcut = os.path.join(STARTUP_PATH, NAME + ".bat")
        content = "@echo off\n" + PATH + "\n"

        # Creates Shortcut
        with open(shortcut, "w") as file:
            file.write(content)
