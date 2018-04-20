from PIL import ImageGrab
import numpy as np
import scipy.misc

def process_img(original_image, resolution):
	processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
	processed_img = compress_img(gray_scale, resolution, resolution)
	return processed_img

def compress_img(height, width):
	return scipy.misc.imresize(original_image, (height, width))

def screenGrab():
	printscreen_pil = ImageGrab.grab()
	printscreen_numpy = np.array(printscreen_pil)
	return printscreen_numpy

def grab_and_compress_screen(resolution):
	screen_img = screenGrab()
	return process_img(screen_img, resolution)


# save_dir = "{}\\{}\\".format(os.getcwd(), "screen_dumps")
#
# 	def run(self, resolution):
# 		while True:
# 			screen_img = screenGrab()
# 			processed_img = process_img(screen_img)
#
# 			cv2.imshow("window", gray_scale_screen)
# 			if cv2.waitKey(25) & 0xFF == ord("q"):
# 				cv2.destroyAllWindows()
