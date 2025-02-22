import pystray
from pystray import MenuItem as item
from PIL import Image, ImageDraw
from threading import Thread
from platform import system
import os

# from Windows_Mouse_Movments.main_windows import run_windows

def load_image():
    while True:
        with open("vimmode.txt", "r+") as f:
            typ = f.read()
            if typ == "Normal":
                icon.icon = Image.open("omnivimn.png")
                return
            if typ == "Visual":
                icon.icon = Image.open("omnivimv.png")
                return
            if typ == "Insert":
                icon.icon = Image.open("omnivimi.png")
                return
            if typ == "Mouse":
                icon.icon = Image.open("omnivimm.png")
                return
            icon.icon = Image.open("omnivim.png")
            return
        
def run_code():
    if os.name=='nt':
        pass
        t1 = Thread(target=run_windows)
    elif os.name=='posix':
        pass
        # t2 = Thread(target=holo_touch)

run_code()

icon = pystray.Icon("test_icon")
icon.icon = Image.open("omnivim.png")
icon.menu = pystray.Menu(
    item("Start", lambda: run_code()),
)
thread = Thread(target=load_image)
thread.start()
icon.run()