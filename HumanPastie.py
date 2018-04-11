import keyboard
import pdb
import pyperclip
import time
import random


def main():
    def human_ctrl_v():
        random.seed(time.time())
        clip = pyperclip.paste().strip()
        print(clip)
        for word in clip:
            time.sleep(random.uniform(0.2, 0.3))
            keyboard.write(word)

    keyboard.add_hotkey('ctrl+b', human_ctrl_v)
    keyboard.wait('esc+ctrl+R')


if __name__ == "__main__":
    while 1:
        main()
