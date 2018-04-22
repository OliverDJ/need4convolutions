
import ScreenGrabber
import direct_input
from keras.models import load_model
import time


class Drive:

    def __init__(self, model_path, resolution=200):
        self.model = load_model(model_path)
        self.resolution = resolution

    def artistic_sleep(self, duration):
        for i in range(duration):
            print(i)
            time.sleep(1)

    def run(self):
        self.artistic_sleep(5)
        while True:
            compressed_screen_img = ScreenGrabber.grab_and_compress_screen(self.resolution)
            prediction = self.model.predict(compressed_screen_img)
            print(prediction)
