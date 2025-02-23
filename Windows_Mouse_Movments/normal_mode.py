from pynput.mouse import Button, Controller
from pynput.keyboard import Controller, Key
import keyboard
d_mode, g_mode = False,False
mouse = Controller()
kb_controller = Controller()
from write_mode import write_mode

def normal_on_key_event(event):
    global d_mode, g_mode
    if event.event_type == 'down':
        if not d_mode and not g_mode:
            match event.name:
                case "h":
                    keyboard.press_and_release("left_arrow")
                    return False
                case "j":
                    keyboard.press_and_release("down_arrow")
                    return False
                case "k":
                    keyboard.press_and_release("up_arrow")
                    return False
                case "l":
                    keyboard.press_and_release("right_arrow")
                    return False
                case "b":
                    keyboard.press_and_release("ctrl+left_arrow")
                    return False
                case "w":
                    keyboard.press_and_release("ctrl+right_arrow")
                    return False
                case "0":
                    keyboard.press_and_release("left_arrow")
                    keyboard.press_and_release("home")
                    keyboard.press_and_release("home")
                    return False
                case "^":
                    keyboard.press_and_release("home")
                    keyboard.release("shift")
                    return False
                case "$":
                    keyboard.press_and_release("end")
                    keyboard.release("shift")
                    return False
                case "G":
                    keyboard.press_and_release("ctrl+end")
                    keyboard.release("shift")
                    return False
                case "d":
                    d_mode = True
                    return False
                case "g":
                    g_mode = True
                    return False
                case "x":
                    keyboard.press_and_release("backspace")
                    return False
        elif d_mode:
            match event.name:
                case "d":
                    keyboard.press_and_release("shift+ home")
            d_mode = False
            return False
        elif g_mode:
            match event.name:
                case "g":
                    keyboard.press_and_release("ctrl+home")
            g_mode = False
            return False

