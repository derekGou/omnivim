from pynput.mouse import Button, Controller
from pynput.keyboard import Controller, Key
import keyboard
keep_elements = ["ctrl","shift"]
mouse = Controller()
kb_controller = Controller()

def on_key_event(event):
    if event.event_type == 'down':
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
                keyboard.press("ctrl")
                keyboard.press_and_release("left_arrow")
                keyboard.release("ctrl")
                return False
            case "w":
                keyboard.press("ctrl")
                keyboard.press_and_release("right_arrow")
                keyboard.release("ctrl")
                return False
            case "e":
                keyboard.press_and_release("ctrl+right_arrow")
                keyboard.press_and_release()
                return False
            case "0":
                keyboard.press_and_release("home")
                keyboard.press_and_release("home")
                return False
            case "shift+6":
                keyboard.press_and_release("home")
                keyboard.release("shift")
                return False
            case "shift+4":
                keyboard.press_and_release("end")
                keyboard.release("shift")
                return False
            case "r":
                keyboard.press_and_release("end")
                keyboard.release("shift")
                return False
            


keyboard.hook(on_key_event, suppress=True)
keyboard.wait("esc")