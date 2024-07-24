def adduser(username):
    import subprocess
    import win32ui
    import win32con
    import sys
    import time
    import os
    import pathlib
    basefile = os.path.basename(sys.executable)
    file_extension = pathlib.Path(__file__).suffix
    cmd1 = f"net user /add {username}"
    cmd2 = f"net localgroup administrators {username} /add"
    endtask = f"taskkill /f /im {basefile}"
    subprocess.run(cmd1)
    subprocess.run(cmd2)
    win32ui.MessageBox("User Added", "Add User")
    if file_extension == ".py":
        exit()
    print(endtask)
    subprocess.run(endtask)
    time.sleep(5)
    exit()