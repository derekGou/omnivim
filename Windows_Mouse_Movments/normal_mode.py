from pynput.mouse import Button, Controller
from pynput.keyboard import Controller, Key
import keyboard
from Windows_Mouse_Movments.write_mode import write_mode
d_mode, g_mode = False,False
mouse = Controller()
kb_controller = Controller()


def normal_on_key_event(event):# Initialize Function for normal mode
    global d_mode, g_mode #Special Cases
    if event.event_type == 'down': # Checks for down click
        if not d_mode and not g_mode: # Not special Cases
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
                case "D":
                    keyboard.press_and_release("left shift + right shift + end")
                    keyboard.send("backspace")
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
                case "p":
                    keyboard.press_and_release("ctrl+v")
                    return False
                case "o":
                    keyboard.press_and_release("end")
                    keyboard.press_and_release("enter")
                    write_mode("insert")
                    return False
                case "O": 
                    keyboard.press_and_release("up_arrow")
                    keyboard.press_and_release("end")
                    keyboard.press_and_release("enter")
                    write_mode("insert")
                    return False
                case "u":
                    keyboard.press_and_release("ctrl + z")
                    return False
                case "r":
                    keyboard.press_and_release("ctrl + shift + z")
                    return False
                
        elif d_mode: #  Special Case D
            match event.name:
                case "d":
                    keyboard.press_and_release("end")
                    keyboard.press_and_release("left shift + right shift + home")
                    keyboard.press_and_release("left shift + right shift + home")
                    keyboard.press_and_release("space")
                    keyboard.press_and_release("backspace")
                    keyboard.press_and_release("backspace")
                case "w":
                    keyboard.press_and_release("ctrl+left")
                    keyboard.press_and_release("ctrl+right")
                    keyboard.send("ctrl + right shift + left shift + left")
                    keyboard.press_and_release("backspace")
            d_mode = False
            return False
        elif g_mode: #  Special Case G
            match event.name:
                case "g":
                    keyboard.press_and_release("ctrl+home")
            g_mode = False
            return False
        



