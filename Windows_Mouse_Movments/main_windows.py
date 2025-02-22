from pynput.mouse import Button, Controller
from pynput.keyboard import Controller, Key
import keyboard
from normal_mode import normal_on_key_event as normal
from mouse_mode import mouse_on_key_event as mouse
mode = "normal"
ctrl_mode = False
def write_mode():
    global mode
    with open("vimmode.txt", "w") as f:
        f.truncate(0)
        f.write(mode)
    f.close()
def on_key_event(event):
    global mode, ctrl_mode
    if event.event_type == 'down':
        if mode == "normal":
            match event.name:
                case "i":
                    mode = "insert"
                    print("Switch mode to "+mode+".")
                    write_mode()
                    return False
                case "v":
                    mode = "visual"
                    print("Switch mode to "+mode+".")
                    write_mode()
                    return False
                case "m":
                    mode = "mouse"
                    print("Switch mode to "+mode+".")
                    write_mode()             
                    return False
        elif (ctrl_mode and event.name == "c") or event.name=="esc":
            mode = "normal"
            print("Switch mode to "+mode+".")
            write_mode()
            return False
        match mode:
            case "normal":
                if event.name == "ctrl":
                    ctrl_mode = True
                    return False
                else:
                    normal(event)
            case "mouse":
                if event.name == "ctrl":
                    ctrl_mode = True
                    return False
                else:
                    mouse(event)
            case "insert":
                if event.event_type == "down":
                    if event.name == "shift":
                        keyboard.press("shift")
                        return False
                    elif event.name == "ctrl":
                        ctrl_mode = True
                        return False
                    else:
                        keyboard.press_and_release(event.name)
                        keyboard.release("shift")
                        ctrl_mode = False
                        return False      
    elif event.event_type == 'up' and mode == "mouse":
        mouse(event)
        return False
keyboard.hook(on_key_event, suppress=True)
keyboard.wait("ctrl+f4")