
from KeyboardListener import KeyboardListener
import ScreenGrabber
import os
from datetime import datetime
import cv2
import time
import scipy.misc
from queue import Queue
from threading import Thread

class DataCollector:
    def __init__(self, save_dir, session_id):
        self.save_dir = "{}\\session_id_{}".format(save_dir, session_id)
        #self.ensure_dir(save_dir)
        self.keyboard_listener = KeyboardListener()
        self.keyboard_listener.run()
        self.resolution = 200
        self.image_queue = Queue()
        self.thread = Thread(target=self.save_images_from_queue, args=(self.image_queue, self.save_dir))



    def save_images_from_queue(self, q, save_dir):
        while True:
            if q:
                image, time_stamp, active_keys = self.image_queue.get()
                save_path = '{}\\{}-{}.png'.format(save_dir, 
                                            self.datetime_to_string(time_stamp), 
                                            self.active_keys_to_string(active_keys))
                scipy.misc.imsave(save_path, image)

    def datetime_to_string(self, time_stamp):
        return time_stamp.strftime('%Y_%m_%d_%H_%M_%S_%f')

    def active_keys_to_string(self, active_keys):
        if not active_keys:
            return "none"
        else:
            return "_".join(active_keys)

    def artistic_sleep(self, duration):
        for i in range(duration):
            print(i)
            time.sleep(1)


    def run(self):
        self.artistic_sleep(5)
        self.thread.start()
        while True:
            time_stamp = datetime.now()
            compressed_screen_img = ScreenGrabber.grab_and_compress_screen(self.resolution)
            active_keys = self.keyboard_listener.get_active_keys()
            self.image_queue.put((compressed_screen_img, time_stamp, active_keys))
            #self.save_image(self.save_dir, time_stamp, active_keys, compressed_screen_img)

d = DataCollector("screen_dumps", 6)
d.run()