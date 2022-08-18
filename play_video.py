from __future__ import annotations
from typing import *

from classes.Action import Action
import pynput 
import time

def play_video(video: str):
    with open(f"videos/{video}.txt") as file:
        actions = [Action.parse(action) for action in file.read().split('\n')]
        mouse = pynput.mouse.Controller()
        keyboard = pynput.keyboard.Controller()

        # actions
        def mouse_move(props):
            mouse.position = tuple([round(int(prop) / 2) for prop in props])

        def mouse_click(props):
            if props[-1]:
                mouse.click(pynput.mouse.Button.left)

        def mouse_scroll(props):
            mouse.scroll(props[2], props[3])

        def keyboard_press(props):
            char = props[0]
            keyboard.press(pynput.keyboard.Key[char.split('.')[-1]] if char.startswith("Key") else char)
            
        def keyboard_release(props):
            char = props[0]
            keyboard.release(pynput.keyboard.Key[char.split('.')[-1]] if char.startswith("Key") else char)

        action_map = {
            "mouse_move": mouse_move,
            "mouse_click": mouse_click,
            "mouse_scroll": mouse_scroll,
            "keyboard_press": keyboard_press,
            "keyboard_release": keyboard_release
        }

        for action in actions:
            method = action_map.get(action.type)
            if method:
                try:
                    method(action.data)
                except:
                    pass

            time.sleep(0.01)

play_video("51d22074-4bd9-430e-a33d-be3ed282b65c")
print("done playing video")