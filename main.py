import pystray
from pystray import MenuItem as Item
from PIL import Image
from threading import Thread
from platform import system
import os
from Windows_Mouse_Movments.main_windows import run_windows
from Windows_Mouse_Movments.write_mode import write_mode
import time



write_mode("normal")

def load_image():
    with open("Windows_Mouse_Movments/vimmode.txt", "r") as f:
        typ = f.read().strip()


    images = {
        "normal": "Images/omnivimn.png",
        "visual": "Images/omnivimv.png",
        "insert": "Images/omnivimi.png",
        "mouse": "Images/omnivimm.png"
    }

    if typ not in images:
        return Image.open("Images/omnivim.png")
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