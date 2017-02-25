import subprocess
import time
import sys
from pykeyboard import PyKeyboard


def write_text(text):

    text = text.strip()

    for ch in text:
        subprocess.call(["xdotool", "type", ch])
        time.sleep(0.1)


def new_line():

    k = PyKeyboard()
    k.press_key(k.enter_key)
    k.release_key(k.enter_key)


def tab():

    k = PyKeyboard()
    k.press_key(k.tab_key)
    k.release_key(k.tab_key)
