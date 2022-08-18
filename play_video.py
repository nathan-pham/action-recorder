from __future__ import annotations
from typing import *

from classes.Action import Action
import pynput 
import time

def play_video(video: str):
    with open(f"videos/{video}") as file:
        actions = [Action.parse(action) for action in file.read().split('\n')]
        mouse = pynput.mouse.Controller()

        def mouse_move(props):
            mouse.position = props

        action_map = {
            "mouse_move": mouse_move
        }

        for action in actions:
            method = action_map.get(action.type)
            if method:
                method(action.data)
            
            time.sleep(0.01)

play_video("06abec5b-83c8-4223-a7fe-75dec3909a32.txt")
