from pynput.mouse import Button, Controller
from pynput.keyboard import Controller, Key
import keyboard
from Windows_Mouse_Movments.normal_mode import normal_on_key_event as normal
from Windows_Mouse_Movments.mouse_mode import mouse_on_key_event as mouse
from Windows_Mouse_Movments.visual_mode import visual_on_key_event as visual
from Windows_Mouse_Movments.write_mode import write_mode


ctrl_mode = False
shift_mode = False

# wrapper function required for main.py to run
def run_windows():

    def on_key_event(event):
        global ctrl_mode,shift_mode

        # file used to dictate mode (visual, normal, insert, mouse)
        with open("Windows_Mouse_Movments/vimmode.txt", "r") as f:
            mode = f.read().strip()
        f.close()


        if event.event_type == 'down':

            # only allow switching to other modes from normal mode
            if mode == "normal":

                match event.name:
                    case "i":
                        write_mode("insert")
                        return False
                    case "v":
                        write_mode("visual")
                        return False
                    case "m":
                        write_mode("mouse")
                        return False

                # saving in normal mode
                if ctrl_mode and event.name == "s":
                    keyboard.press_and_release("ctrl+s")
                    ctrl_mode = False
                    return False

            # exit back to normal mode
            elif ((ctrl_mode and event.name == "c") or event.name=="esc") and mode != "kill":
                keyboard.release("ctrl")
                keyboard.release("shift")
                write_mode("normal")
                ctrl_mode=False
                return False
            match mode:
                case "visual":
                    if event.name == "shift":
                        shift_mode = True
                    if event.name == "ctrl":
                        ctrl_mode = True
                    elif shift_mode and ctrl_mode:
                        if event.name == "q":
                            write_mode("kill")
                    else:
                        visual(event)
                case "normal":
                    if event.name == "shift":
                        shift_mode = True
                    if event.name == "ctrl":
                        ctrl_mode = True
                    elif shift_mode and ctrl_mode:
                        if event.name == "Q":
                            write_mode("kill")
                    else:
                        normal(event)

                case "mouse":
                    if event.name == "shift":
                        shift_mode = True 
                    if event.name == "ctrl":
                        ctrl_mode = True
                    elif shift_mode and ctrl_mode:
                        if event.name == "q":
                            write_mode("kill")
                    else:
                        mouse(event)
                        shift_mode = False
                        ctrl_mode = False

                case "insert" | "kill":
                    if event.event_type == "down":
                        # allows for default key-binds to be used in insert mode
                        if event.name == "ctrl":
                            keyboard.press(event.name)
                            ctrl_mode = True
                        # allows for typing shifted keys
                        if event.name =="shift":
                            shift_mode = True
                        if shift_mode and not ctrl_mode:
                            # if alphabetic and one character long (not SPACE, BACKSPACE, or ENTER)
                            if event.name.isalpha() and len(event.name) == 1:
                                keyboard.write(event.name.upper())
                                return False
                            elif event.name in ["up","down","left","right"]:
                                keyboard.send(f"right shift + left shift + {event.name}")
                                return False
                            else:

                                # hard coded because shift + = returns errors
                                if event.name == "+":
                                    keyboard.send("+")
                                else:
                                    keyboard.press(f"shift+{event.name}")
                                return False
                        elif shift_mode and ctrl_mode:
                            if event.name == "q":
                                write_mode("normal" if mode == "kill" else "kill")
                            elif event.name in ["up","down","left","right"]:
                                keyboard.send(f"ctrl+right shift + left shift + {event.name}")
                                return False
                            else:
                                keyboard.send(f"ctrl+shift+{event.name}")
                        else:
                            keyboard.press(event.name)
                            return False
                    return False

        # release held keys for mouse navigation
        elif event.event_type == 'up' and mode == "mouse":
            mouse(event)
            return False

        # release held keys for multi key combos 
        elif event.event_type == "up":
            if event.name == "ctrl":
                keyboard.release(event.name)
                ctrl_mode = False
            elif event.name == "shift":
                keyboard.release(event.name)
                shift_mode = False
            else:
                keyboard.release(event.name)
    keyboard.hook(on_key_event, suppress=True)
