import pystray
from pystray import MenuItem as item
from PIL import Image, ImageDraw
from threading import Thread
from platform import system
import os

def load_image():
    return Image.open("omni.png")
print("working1")

def run_code():
    if os.name=='nt':
        with open("mode.txt", "w") as f:
            f.truncate(0)
            f.write("windows\n")
            f.write("normal")
            # t1 = Thread(target=holo_touch)
    elif os.name=='posix':
        with open("mode.txt", "w") as f:
            f.truncate(0)
            f.write("mac\n")
            f.write("normal")
            # t2 = Thread(target=holo_touch)

run_code()

icon = pystray.Icon("test_icon")
icon.icon = load_image()
icon.run()