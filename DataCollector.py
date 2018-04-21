
from KeyboardListener import KeyboardListener
import ScreenGrabber
import os
from datetime import datetime
import cv2
import time


class DataCollector:

    def __init__(self, save_dir, session_id):
        self.save_dir = "{}\\session_id_{}".format(save_dir, session_id)
        #self.ensure_dir(save_dir)
        self.keyboard_listener = KeyboardListener()
        self.keyboard_listener.run()
        self.resolution = 200

    def save_image(self, save_dir, time_stamp, active_keys, image):
        save_path = '{}\\{}-{}.png'.format(save_dir, 
                                    self.datetime_to_string(time_stamp), 
                                    self.active_keys_to_string(active_keys))
        cv2.imwrite(save_path, image)

    def datetime_to_string(self, time_stamp):
        return time_stamp.strftime('%Y_%m_%d_%H_%M_%S_%f')

    def active_keys_to_string(self, active_keys):
        if not active_keys:
            return "none"
        else:
            return "_".join(active_keys)


    #def ensure_dir(self, file_path):
    #    directory = os.path.dirname(file_path)
    #    if not os.path.exists(directory):
    #        os.makedirs(directory)

    def artistic_sleep(self, duration):
        for i in range(duration):
            print(i)
            time.sleep(1)


    def run(self):
        self.artistic_sleep(5)
        while True:
            time_stamp = datetime.now()
            compressed_screen_img = ScreenGrabber.grab_and_compress_screen(self.resolution)
            active_keys = self.keyboard_listener.get_active_keys()
            self.save_image(self.save_dir, time_stamp, active_keys, compressed_screen_img)

d = DataCollector("screen_dumps", 2)
d.run()