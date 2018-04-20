

#from msvcrt import getch
#while True:
#    print(ord(getch()))


from pynput import keyboard

def on_press(key):
    try:
    	print(key.char, "press")
    	return key.char, 1
    except AttributeError:
        pass

def on_release(key):
   	
    if key == keyboard.Key.esc:
        return False# Stop listener
    else:
    	print(key.char, "release")
    	return key, -1

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()