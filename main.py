import os
import ctypes
import time

directory = 'D:/Wallpapers/'  # change to your directory must end with '/'
folder = os.listdir(directory)
while True:
	for element in folder:
		time.sleep(1800)  # time in seconds (default 30min)
		ctypes.windll.user32.SystemParametersInfoW(20, 0, directory+element, 0)
