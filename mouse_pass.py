#!/usr/bin/env python3
from pynput.mouse import Listener, Button

PIN = "1101"
PIN_LENGTH = len(PIN)
user_pin = ""


def on_click(x, y, button, pressed):
    global user_pin
    # Detect left and right mouse clicks
    if pressed and button == Button.left:
        user_pin = user_pin + "1"
        print(user_pin)     # debugging
    elif pressed and button == Button.right:
        user_pin = user_pin + "0"
        print(user_pin)     # debugging

    # Stop monitoring mouse clicks when max pin length is reached
    if len(user_pin) == PIN_LENGTH:
        # Show whether password is right or not
        if user_pin == PIN:
            print("Correct password")
        else:
            print("Wrong password")
        return False


with Listener(on_click=on_click) as listener:
    listener.join()
