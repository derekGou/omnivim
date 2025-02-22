from pynput.mouse import Button, Controller
from pynput.keyboard import Controller, Key
import keyboard
mouse = Controller()
kb_controller = Controller()
def normal_on_key_event(event):
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
                keyboard.press_and_release("ctrl+left_arrow")
                return False
            case "w":
                keyboard.press_and_release("ctrl+right_arrow")
                return False
            case "0":
                keyboard.press_and_release("home")
                keyboard.press_and_release("home")
                return False
            case "^":
                keyboard.press_and_release("home")
                return False
            case "$":
                keyboard.press_and_release("end")
                return False
keyboard.hook(normal_on_key_event, suppress=True)
keyboard.wait("esc")