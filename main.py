import pystray
from pystray import MenuItem as Item
from PIL import Image
from threading import Thread
from platform import system
import os
from Windows_Mouse_Movments.main_windows import run_windows
import time
with open("vimmode.txt", "w") as f:
    f.truncate(0)
    f.write("normal")
f.close()

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
        t1 = Thread(target=run_windows, daemon=True)
        t1.start()

run_code()

menu = pystray.Menu(
    Item("Toggle State", run_code, default=True)
)

icon = pystray.Icon("omnivim", load_image(), menu=menu)

def setup(icon):
    icon.visible = True
    while icon.visible:  # Ensure the thread stops if the icon is closed
        icon.icon = load_image()
        time.sleep(1)  # Avoid 100% CPU usage

run_code()
icon.run(setup)