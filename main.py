import pystray
from pystray import MenuItem as Item
from PIL import Image
from threading import Thread
from platform import system
import os

# from Windows_Mouse_Movments.main_windows import run_windows

def load_image():
    with open("vimmode.txt", "r+") as f:
        typ = f.read()
        if typ == "Normal":
            return Image.open("omnivimn.png")
        if typ == "Visual":
            return Image.open("omnivimv.png")
        if typ == "Insert":
            return Image.open("omnivimi.png")
        if typ == "Mouse":
            return Image.open("omnivimm.png")
        return Image.open("omnivim.png")
        
def run_code():
    if os.name=='nt':
        pass
        # t1 = Thread(target=run_windows)
    elif os.name=='posix':
        pass
        # t2 = Thread(target=holo_touch)

run_code()

menu = pystray.Menu(
    Item("Toggle State", run_code, default=True) 
)

icon = pystray.Icon("omnivim", icon=load_image(), menu=menu)
icon.icon = Image.open("omnivim.png")
icon.run()