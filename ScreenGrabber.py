from PIL import ImageGrab
import numpy as np
import scipy.misc
import cv2

def process_img(original_image, resolution):
	processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
	processed_img = compress_img(processed_img, resolution, resolution)
	return processed_img

def compress_img(image, height, width):
	return scipy.misc.imresize(image, (height, width))

def screenGrab():
	printscreen_pil = ImageGrab.grab()
	printscreen_numpy = np.array(printscreen_pil)
	return printscreen_numpy

def grab_and_compress_screen(resolution):
	screen_img = screenGrab()
	return process_img(screen_img, resolution)
