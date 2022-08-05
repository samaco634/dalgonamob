import cv2
import pygame

from motor import CarMotor

import os


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
pygame.display.update()

motors = CarMotor()

speedSet = 50
trunSpeedSet = 50

def main():
    # Start the camera
    camera = cv2.VideoCapture(0)
    camera.set(3, 224)
    camera.set(4, 224)
    #camera.set(cv2.CAP_PROP_BUFFERSIZE, 2)

    dirname = "./data/"
    makedirs(dirname)
    makedirs(dirname +"Left")
    makedirs(dirname +"Right")
    makedirs(dirname +"Forward")

    i = 0
    run = True
   
    while( True ):
        
        getNewFrame, image = camera.read()
        
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
                    motors.motor_forward(speedSet)
                    filepath = dirname + "Forward/"
                    cv2. ("%s%05d_%03d.png" % (filepath, i, 90), image)
                    i += 1
                elif event.key == pygame.K_DOWN:
                    print("stop")
                    motors.motor_stop()
                elif event.key == pygame.K_LEFT:
                    print("left")
                    motors.motor_left(trunSpeedSet)
                    filepath = dirname + "Left/"
                    cv2. ("%s%05d_%03d.png" % (filepath, i, 45), image)
                    i += 1
                elif event.key == pygame.K_RIGHT:
                    print("right")
                    motors.motor_right(trunSpeedSet)
                    filepath = dirname + "Right/"
                    cv2. ("%s%05d_%03d.png" % (filepath, i, 135), image)
                    i += 1
            elif event.type == pygame.KEYUP:
                motors.motor_stop()
        
        if run == False:
            break;
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
     

    cv2.destroyAllWindows()
    pygame.quit()

    camera.release()
    
if __name__ == '__main__':
    main()
