import pystray
from pystray import MenuItem as item
from PIL import Image, ImageDraw
from threading import Thread
from platform import system
import os

from Windows_Mouse_Movments.main_windows import run_windows

def load_image():
    return Image.open("omni.png")

def run_code():
    if os.name=='nt':
        with open("mode.txt", "w") as f:
            f.truncate(0)
            f.write("windows")
            t1 = Thread(target=run_windows)
    elif os.name=='posix':
        with open("mode.txt", "w") as f:
            f.truncate(0)
            f.write("mac")
            # t2 = Thread(target=holo_touch)

run_code()

icon = pystray.Icon("test_icon")
icon.icon = load_image()
icon.run()