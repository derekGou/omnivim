from pynput.mouse import Button, Controller
from pynput.keyboard import Controller, Key
import keyboard
from normal_mode import on_key_event as normal
mode = "normal"

def run_windows():
    def on_key_event(event):
        global mode
        if event.event_type == 'down':
            if mode == "default":
                match event.name:
                    case "i":
                        mode = "insert"
                        return False
                    case "v":
                        mode = "visual"
                        return False
                    case "m":
                        mode = "mouse"                    
                        return False
            elif event.name=="ctrl+c" or event.name=="esc":
                mode = "normal"
                return False
            with open("../immode.txt", "w") as f:
                f.truncate(0)
                f.write(mode)
            match mode:
                case "normal":
                    normal(event)


    keyboard.hook(on_key_event, suppress=True)
    keyboard.wait("f4")