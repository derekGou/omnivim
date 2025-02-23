from pynput.mouse import Button, Controller
from pynput.keyboard import Controller, Key
import keyboard
from Windows_Mouse_Movments.write_mode import write_mode
d_mode, g_mode = False,False
mouse = Controller()
kb_controller = Controller()

def visual_on_key_event(event): #Visual Mode Function
    global d_mode, g_mode
    if event.event_type == 'down':#Makes sure is key down
        if not d_mode and not g_mode:# Checks for special Cases
            match event.name: # Vim commands on visual mode
                case "h":
                    keyboard.send("right shift+left shift+left_arrow")
                    return False
                case "j":
                    keyboard.send("right shift+left shift+down_arrow")
                    return False
                case "k":
                    keyboard.send("right shift+left shift+up_arrow")
                    return False
                case "l":
                    keyboard.send("right shift+left shift+right_arrow")
                    return False
                case "b":
                    keyboard.send("ctrl+right shift+left shift+left_arrow")
                    return False
                case "w":
                    keyboard.send("ctrl+right shift+left shift+right_arrow")
                    return False
                case "0":
                    keyboard.send("right shift+left shift+home")
                    keyboard.send("right shift+left shift+home")
                    return False
                case "^":
                    keyboard.send("right shift+left shift+home")
                    keyboard.release("shift")
                    return False
                case "$":
                    keyboard.send("right shift+left shift+end")
                    keyboard.release("shift")
                    return False
                case "G":
                    keyboard.send("ctrl+right shift+left shift+end")
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
                    keyboard.send("backspace")
                    write_mode("normal")
                    return False
        elif g_mode: #G mode 
            match event.name:
                case "g":
                    keyboard.send("ctrl+right shift+left shift+home")
            g_mode = False
            return False


            
            
