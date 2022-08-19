import RPi.GPIO as GPIO
import cv2
import time
import pygame

from motor import CarMotor

import os

from camera_buffer_thread import CameraBufferCleanerThread


def makedirs(path): 
   try: 
        os.makedirs(path) 
   except OSError: 
       if not os.path.isdir(path): 
           raise
# pygame setup
pygame.init()
screen = pygame.display.set_mode((320, 240))
pygame.display.set_caption("myRCcar")
pygame.key.set_repeat(10)

key="no key"
font = pygame.font.SysFont("arial",16)  
text1 = font.render("My Car",True,(255,255,255)) 
text2 = font.render("Up: start car",True,(255,255,255))  
text3 = font.render("Down: stop car",True,(255,255,255))
text4 = font.render("Left: left turn",True,(255,255,255))  
text5 = font.render("Right: right turn",True,(255,255,255))
text6 = font.render("Esc: Quit",True,(255,255,255)) 
text7 = font.render(key,True,(255,255,255))

screen.fill((0,0,0))
screen.blit(text1, (30, 30))
screen.blit(text2, (30, 60))
screen.blit(text3, (30, 90))
screen.blit(text4, (30, 120))
screen.blit(text5, (30, 150))
screen.blit(text6, (30, 180))
screen.blit(text7, (30, 210))

pygame.display.update()

motors = CarMotor()

speedSet = 50
trunSpeedSet = 50

def main():
    # Start the camera
    camera = cv2.VideoCapture(0)
    camera.set(3, 160)
    camera.set(4, 120)
    camera.set(cv2.CAP_PROP_BUFFERSIZE, 1)

    # Start the cleaning thread
    cam_cleaner = CameraBufferCleanerThread(camera)

    makedirs("./video/")
    filepath = "./video/train"

    i = 0
    carState = "stop"
    run = True
   
    while( True ):
        
        getNewFrame, image = cam_cleaner.getFrame()
        
        if getNewFrame == True :
            cv2.imshow('Original', image)
        #image = cv2.flip(image,-1)
            
        for event in pygame.event.get():
            if (event.type == pygame.QUIT
            or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    print("go")
                    carState = "go"
                    cv2.imwrite("%s_%05d_%03d.png" % (filepath, i, 90), image)
                    i += 1
                    motors.motor_forward(speedSet)
                elif event.key == pygame.K_DOWN:
                    print("stop")
                    carState = "stop"
                    motors.motor_stop()
                elif event.key == pygame.K_LEFT:
                    print("left")
                    carState = "left"
                    cv2.imwrite("%s_%05d_%03d.png" % (filepath, i, 45), image)
                    i += 1
                    motors.motor_left(trunSpeedSet)

                elif event.key == pygame.K_RIGHT:
                    print("right")
                    carState = "right"
                    cv2.imwrite("%s_%05d_%03d.png" % (filepath, i, 135), image)
                    i += 1
                    motors.motor_right(trunSpeedSet)
            elif event.type == pygame.KEYUP:
                carState = "stop"
                motors.motor_stop()
        
        if run == False:
            break;
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cam_cleaner.terminate()   

    cv2.destroyAllWindows()
    pygame.quit()
    
    cam_cleaner.join()
    camera.release()
    
if __name__ == '__main__':
    main()
    GPIO.cleanup()
