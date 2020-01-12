import picamera
import pygame
import RPi.GPIO as GPIO
from threading import Thread
import time

pygame.init()
pygame.mouse.set_visible(False)
info_object = pygame.display.Info()

screen = pygame.display.set_mode((info_object.current_w, info_object.current_h), pygame.FULLSCREEN)   
background = pygame.Surface(screen.get_size()) 
background = background.convert()  

screenPicture = pygame.display.set_mode((info_object.current_w, info_object.current_h), pygame.FULLSCREEN)  
backgroundPicture = pygame.Surface(screenPicture.get_size()) 
backgroundPicture = background.convert()  

transform_x = info_object.current_w 
transfrom_y = info_object.current_h 

camera = picamera.PiCamera()
camera.resolution = (info_object.current_w, info_object.current_h)
camera.rotation              = 0
camera.hflip                 = True
camera.vflip                 = False
camera.brightness            = 50
camera.preview_alpha = 120
camera.preview_fullscreen = True

def show_image(image_path):	
	screen.fill(pygame.Color("white")) 
	img = pygame.image.load(image_path) 
	img = img.convert()	
	# set_demensions(img.get_width(), img.get_height()) 
	x = (info_object.current_w / 2) - (img.get_width() / 2)
	y = (info_object.current_h / 2) - (img.get_height() / 2)
	screen.blit(img,(x,y))
	pygame.display.flip()

def main(threadName, *args):
    while True:
            show_image('images/rick.jpeg')
            time.sleep(0.2)
    GPIO.cleanup()

# launch the main thread
Thread(target=main, args=('Main', 1)).start()
