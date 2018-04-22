
import ScreenGrabber
import direct_input
from keras.models import load_model
import time
import numpy as np

class Drive:

    def __init__(self, model_path, resolution=200):
        self.model = load_model(model_path)
        self.resolution = resolution
        self.prediction_threshold = 0.7
        self.pos_to_key_dict = {0: 'w', 1: 's', 2: 'a', 3: 'd'}

    def prediction_to_keys(self, prediction_array):
        predicted_keys = []
        for i in range(len(prediction_array)):
            if prediction_array[i] > self.prediction_threshold:
                predicted_keys.append(self.pos_to_key_dict[i])
        return predicted_keys



    def artistic_sleep(self, duration):
        for i in range(duration):
            print(i)
            time.sleep(1)

    def run(self):
        self.artistic_sleep(5)
        while True:
            compressed_screen_img = ScreenGrabber.grab_and_compress_screen(self.resolution)
            compressed_screen_img = np.expand_dims(compressed_screen_img, axis=0)
            prediction_array = self.model.predict(compressed_screen_img)
            prediction_array = np.squeeze(prediction_array, axis=0)
            predicted_keys = self.prediction_to_keys(prediction_array)
            #direct_input.press_predicted_keys(predicted_keys)
            direct_input.press_predicted_key(predicted_keys[0])
d = Drive("models\\shitty_model.h5")
d.run()
