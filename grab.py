from PIL import ImageGrab
import os
import numpy as np
from time import strftime, localtime, time
import cv2

from datetime import datetime




def process_img(original_image):
	processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
	return processed_img




def screenGrab():
	printscreen_pil = ImageGrab.grab(bbox=(0,40,800,640))
	printscreen_numpy = np.array(printscreen_pil)
	return printscreen_numpy
	
		

save_dir = "{}\\{}\\".format(os.getcwd(), "screen_dumps")

while True:
	screen = screenGrab()
	gray_scale_screen = process_img(screen)
	cv2.imshow("window", gray_scale_screen)
	if cv2.waitKey(25) & 0xFF == ord("q"):
		cv2.destroyAllWindows()
