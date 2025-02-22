import pystray
from pystray import MenuItem as item
from PIL import Image, ImageDraw
from threading import Thread
from platform import system

def load_image():
    return Image.open("omni.png")

def on_clicked(icon, item):
    if item == "Option 1":
        pass

icon = pystray.Icon("test_icon")
icon.icon = load_image()
icon.run()