import RPi.GPIO as GPIO
import cv2
import time
import pygame

#CarMotor import하기

import os

# pygame setup
pygame.init()
screen = pygame.display.set_mode((320, 240))
pygame.display.set_caption("myRCcar")

pygame.display.update()

#CarMotor 객체 만들기

speedSet = 50
trunSpeedSet = 30

def main():
    i = 0
    carState = "stop"
    run = True
   
    while( True ):            
        for event in pygame.event.get():
            if (event.type == pygame.QUIT
            or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                  #전진하기
                elif event.key == pygame.K_DOWN:
                  #후진하기
                elif event.key == pygame.K_LEFT:
                  #좌회전
                elif event.key == pygame.K_RIGHT:
                   #우회전
            elif event.type == pygame.KEYUP:
                #정지
        
        if run == False:
            break;
    
    pygame.quit()
    
if __name__ == '__main__':
    main()
    GPIO.cleanup()
