#!/usr/bin/env python3
from pynput.mouse import Listener, Button


def on_click(x, y, button, pressed):
    # Detect left and right mouse clicks
    if pressed and button == Button.left:
        print("Left click")
    elif pressed and button == Button.right:
        print("Right click")


with Listener(on_click=on_click) as listener:
    listener.join()
