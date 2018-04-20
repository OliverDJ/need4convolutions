

from pynput import keyboard
class KeyBoardListner:
    def __init__(self):
        self.key_dict = {'w':False, 's': False, 'a':False, 'd':False}
        self.run()

    def on_press(key):
        try:
        	if key in self.key_dict:
        	       self.key_dict[key] = True
        except AttributeError:
            pass

    def on_release(key):
        if key == keyboard.Key.esc:
            return False# Stop listener
        else:
            if key in self.key_dict:
                self.key_dict[key] = False

    def run(self):
        with keyboard.Listener(
                on_press=on_press,
                on_release=on_release) as listener:
            listener.join()
