

from pynput import keyboard

import threading

class KeyboardListener:
    def __init__(self):
        self.key_dict = {"w":False, "s": False, "a":False, "d":False}
        self.thread = threading.Thread(target = self.listen_to_keyboard)

    def on_press(self, key):
        try:
            if key.char in self.key_dict:
                self.key_dict[key] = True
        except AttributeError:
            pass

    def on_release(self, key):
        if key == keyboard.Key.esc:
            return False# Stop listener
        else:
            if key in self.key_dict:
                self.key_dict[key] = False

    def listen_to_keyboard(self):
        with keyboard.Listener(
                on_press=self.on_press,
                on_release=self.on_release) as listener:
            listener.join()

    def get_active_keys(self):
        active_key_list = []
        for key in  self.key_dict:
            if self.key_dict[key]:
                active_key_list.append(key.char)
        return active_key_list

    def run(self):
        self.thread.start()
