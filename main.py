import pystray
from pystray import MenuItem as Item
from PIL import Image
from threading import Thread
from platform import system
import os

from Windows_Mouse_Movments.main_windows import on_key_event as run_windows

def load_image():
    print("amit not gay")
    with open("vimmode.txt", "r") as f:
        typ = f.read()
        print("amit gay")
        if typ == "Normal":
            print('a')
            return Image.open("omnivimn.png")
        if typ == "Visual":
            print('b')
            return Image.open("omnivimv.png")
        if typ == "Insert":
            print('c')
            return Image.open("omnivimi.png")
        if typ == "Mouse":
            print('d')
            return Image.open("omnivimm.png")
        print('working') 
        return Image.open("omnivim.png")
        
def run_code():
    if os.name=='nt':
        t1 = Thread(target=run_windows)
    elif os.name=='posix':
        pass
        # t2 = Thread(target=holo_touch)

print("daniel not agy")
menu = pystray.Menu(
    Item("Toggle State", run_code, default=True) 
)

icon = pystray.Icon("omnivim", icon=load_image(), menu=menu)


icon.icon = load_image()
icon.visible = True
icon.run()