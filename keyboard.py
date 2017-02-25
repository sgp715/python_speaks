import subprocess
import time
import sys


def write_text(text):

    text = text.strip()

    for ch in text:
        subprocess.call(["xdotool", "type", ch])
        time.sleep(0.1)
