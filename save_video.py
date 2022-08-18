from __future__ import annotations
from typing import *

import pygetwindow as gw
import pynput 
import time
import uuid

from classes.Action import Action

def save_video():
    actions = []

    # record running titles
    titles = [Action("window", title.strip()) for title in gw.getAllTitles() if len(title) > 0]
    for title in titles:
        actions.append(title)

    # create new actions if they differ from the previous one
    def action_factory(action_name: str, exclude_indices: List[int] = []):
        def action(*props):
            props = [prop.char if isinstance(prop, pynput.keyboard.KeyCode) else str(prop) for prop in props]
            for i in exclude_indices:
                props.pop(i)

            new_action = Action(action_name, tuple(props))
            if not new_action.equals(actions[-1]):
                actions.append(new_action)
        
        return 
        
    # record mouse actions
    mouse_listener = pynput.mouse.Listener(
        on_move=action_factory("mouse_move"),
        on_click=action_factory("mouse_click", [2]),
        on_scroll=action_factory("mouse_scroll"),
    )
    
    # record keyboard actions
    keyboard_listener = pynput.keyboard.Listener(
        on_press=action_factory("keyboard_press"),
        on_release=action_factory("keyboard_release")
    )

    mouse_listener.start()
    keyboard_listener.start()


    def dispose():
        # remove event listeners
        mouse_listener.stop()
        keyboard_listener.stop()

        with open(f"videos/{uuid.uuid4()}.txt", "w") as file:
            file.write("\n".join([str(action) for action in actions]))

    return dispose

# record a 5 second video
print("started recording")
dispose = save_video()
time.sleep(10)
dispose()
print("saved video")