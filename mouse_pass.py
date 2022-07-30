#!/usr/bin/env python3
from getpass import getpass
from pynput.mouse import Listener, Button

print("Type 'l' for left click and 'r' for right click")
print("Example: rrlr, llllr")
print()
PASSWORD = getpass("Enter password: ")
PASS_LENGTH = len(PASSWORD)
user_pin = ""


def on_click(x, y, button, pressed):
    global user_pin
    # Detect left and right mouse clicks
    if pressed and button == Button.left:
        user_pin = user_pin + "l"
        # print(user_pin)     # debugging
    elif pressed and button == Button.right:
        user_pin = user_pin + "r"
        # print(user_pin)     # debugging

    # Stop monitoring mouse clicks when max pin length is reached
    if len(user_pin) == PASS_LENGTH:
        # Show whether password is right or not
        if user_pin == PASSWORD:
            print("Correct password")
        else:
            print("Wrong password")
        return False


with Listener(on_click=on_click) as listener:
    listener.join()
