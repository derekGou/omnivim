import pystray
from pystray import MenuItem as item
from PIL import Image, ImageDraw
from threading import Thread
from platform import system
import os

# from Windows_Mouse_Movments.main_windows import run_windows

def load_image():
    with open("mode.txt", "w") as f:
        typ = f.read()
        if len(typ) == 0:
            return Image.open("omnivim.png")
        if typ == "Normal":
            return Image.open("omnivimn.png")
        if typ == "Visual":
            return Image.open("omnivimv.png")
        if typ == "Insert":
            return Image.open("omnivimi.png")
        if typ == "Mouse":
            return Image.open("omnivimm.png")
        
def run_code():
    if os.name=='nt':
        with open("mode.txt", "w") as f:
            f.truncate(0)
            f.write("windows")
            # t1 = Thread(target=run_windows)
            f.close()
    elif os.name=='posix':
        with open("mode.txt", "w") as f:
            f.truncate(0)
            f.write("mac")
            # t2 = Thread(target=holo_touch)
            f.close()

run_code()

icon = pystray.Icon("test_icon")
icon.icon = load_image()
icon.run()