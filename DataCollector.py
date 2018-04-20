
from KeyBoardListner import KeyBoardListner

import grab
from datetime import datetime
import cv2


class DataCollector:



    def __init__(self, save_dir):
        self.q = Queue()
        self.save_dir = save_dir
        self.keyboard_listner = KeyBoardListner()
        self.resolution = 200

        while True:
            time_stamp = datetime.now()
            compressed_screen_img = grab_and_compress_screen(self.resolution)
            self.save_image(self.save_dir, time_stamp, compressed_screen_img)

    def datetime_to_string(self, time_stamp):
        return time_stamp.strftime('%Y_%m_%d_%H_%M_%S_%f')


    def save_image(save_dir, time_stamp, image):
        save_path = '{}/{}.png'.format(save_dir, self.datetime_to_string(time_stamp))
        cv2.imwrite(save_path, image)


    #def worker(self, save_path)
