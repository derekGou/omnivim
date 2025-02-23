from pynput.mouse import Button, Controller
from pynput.keyboard import Controller, Key
import keyboard
from Windows_Mouse_Movments.write_mode import write_mode
d_mode, g_mode = False,False
mouse = Controller()
kb_controller = Controller()

def visual_on_key_event(event):
    global d_mode, g_mode
    if event.event_type == 'down':
        if not d_mode and not g_mode:
            match event.name:
                case "h":
                    keyboard.press_and_release("shift + left_arrow")
                    return False
                case "j":
                    keyboard.press_and_release("shift + down_arrow")
                    return False
                case "k":
                    keyboard.press_and_release("shift + up_arrow")
                    return False
                case "l":
                    keyboard.press_and_release("shift + right_arrow")
                    return False
                case "b":
                    keyboard.press_and_release("shift + ctrl+left_arrow")
                    return False
                case "w":
                    keyboard.press_and_release("shift + ctrl + right_arrow")
                    return False
                case "0":
                    keyboard.press_and_release("shift + left_arrow")
                    keyboard.press_and_release("shift + home")
                    keyboard.press_and_release("shift + home")
                    return False
                case "^":
                    keyboard.press_and_release("shift + home")
                    keyboard.release("shift")
                    return False
                case "$":
                    keyboard.press_and_release("shift + end")
                    keyboard.release("shift")
                    return False
                case "G":
                    keyboard.press_and_release("shift+ ctrl+end")
                    keyboard.release("shift")
                    return False
                case "g":
                    g_mode = True
                    return False
                case "y":
                    keyboard.press_and_release("ctrl + c")
                    keyboard.press_and_release("left_arrow")
                    keyboard.press_and_release("right_arrow")
                    write_mode("normal")
                    return False
                case "x":
                    keyboard.press_and_release(" ")
                    keyboard.press_and_release("backspace")
                    write_mode("normal")
                    return False
        elif g_mode:
            match event.name:
                case "g":
                    keyboard.press_and_release("shift+ctrl+home")
            g_mode = False
            return False


            
            
