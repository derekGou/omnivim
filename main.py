import pystray
from pystray import MenuItem as Item
from PIL import Image
from threading import Thread
from platform import system
import os
import time
from Windows_Mouse_Movments.main_windows import run_windows

def load_image():
    with open("vimmode.txt", "r") as f:
        typ = f.read().strip()
    

    images = {
        "normal": "omnivimn.png",
        "visual": "omnivimv.png",
        "insert": "omnivimi.png",
        "mouse": "omnivimm.png"
    }
    
    if typ not in images:
        return Image.open("omnivim.png")
    return Image.open(images[typ])

def run_code():
    if os.name == 'nt':
        t1 = Thread(target=run_windows)
        t1.start()

menu = pystray.Menu(
    Item("Toggle State", run_code, default=True) 
)

def update_image():
    while True:
        icon.icon = load_image()
        time.sleep(0.5)
    
icon = pystray.Icon("omnivim", load_image(), menu=menu)

def setup(icon):
    icon.visible = True

icon.run(setup)
thread = Thread(target = update_image)
thread.start()