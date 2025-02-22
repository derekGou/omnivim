import pystray
from pystray import MenuItem as Item
from PIL import Image
from threading import Thread
from platform import system
import os

from Windows_Mouse_Movments.main_windows import run_windows

def load_image():
    with open("vimmode.txt", "r") as f:
        typ = f.read().strip()

    images = {
        "Normal": "omnivimn.png",
        "Visual": "omnivimv.png",
        "Insert": "omnivimi.png",
        "Mouse": "omnivimm.png"
    }
    return Image.open(images.get(typ, "omnivim.png"))

def run_code():
    if os.name == 'nt':
        t1 = Thread(target=run_windows)
        t1.start()

menu = pystray.Menu(
    Item("Toggle State", run_code, default=True) 
)

icon = pystray.Icon("omnivim", load_image(), menu=menu)

def setup(icon):
    icon.visible = True

icon.run(setup)
