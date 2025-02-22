from pynput.mouse import Button, Controller
from pynput.keyboard import Controller, Key
import keyboard
from normal_mode import normal_on_key_event as normal
mode = "normal"
def on_key_event(event):
    global mode
    if event.event_type == 'down':
        if mode == "normal":
            match event.name:
                case "i":
                    mode = "insert"
                    print("Switch mode to "+mode+".")
                    return False
                case "v":
                    mode = "visual"
                    print("Switch mode to "+mode+".")
                    return False
                case "m":
                    mode = "mouse"
                    print("Switch mode to "+mode+".")                
                    return False
        elif (keyboard.is_pressed("ctrl") and keyboard.is_pressed("c")) or event.name=="esc":
            mode = "normal"
            print("Switch mode to "+mode+".")
            return False
        with open("../vimmode.txt", "w") as f:
            f.truncate(0)
            f.write(mode)
        match mode:
            case "normal":
                normal(event)
            case "insert":
                if event.event_type == "down":
                    if event.name == "shift":
                        keyboard.press("shift")
                        return False
                    elif event.name == "ctrl":
                        keyboard.press("ctrl")
                        return False
                    else:
                        keyboard.press_and_release(event.name)
                        keyboard.release("shift")
                        keyboard.release("ctrl")
                        return False
                    
keyboard.hook(on_key_event, suppress=True)
keyboard.wait("ctrl+f4")
