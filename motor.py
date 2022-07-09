import RPi.GPIO as GPIO
import time

class CarMotor():

    def __init__(self):
       self.PWMA = 18
       self.AIN1 = 24 #27
       self.AIN2 = 25 #22

       self.PWMB = 23
       self.BIN1 = 22 #25
       self.BIN2 = 27 #24


       GPIO.setwarnings(False)
       GPIO.setmode(GPIO.BCM)
       GPIO.setup(self.PWMA, GPIO.OUT)
       GPIO.setup(self.AIN1, GPIO.OUT)
       GPIO.setup(self.AIN2, GPIO.OUT)

       GPIO.setup(self.PWMB, GPIO.OUT)
       GPIO.setup(self.BIN1, GPIO.OUT)
       GPIO.setup(self.BIN2, GPIO.OUT)

       self.L_Motor = GPIO.PWM(self.PWMA, 500)
       self.L_Motor.start(0)

       self.R_Motor = GPIO.PWM(self.PWMB, 500)
       self.R_Motor.start(0)


    def motor_forward(self, speed):
        if speed > 100:
            speed = 100
        GPIO.output(self.AIN1, 0)
        GPIO.output(self.AIN2, 1)
        
        self.L_Motor.ChangeDutyCycle(speed)
 
    def motor_stop(self):   
        self.L_Motor.ChangeDutyCycle(0)
        self.R_Motor.ChangeDutyCycle(0)
        
    def motor_backward(self, speed):
        if speed > 100:
            speed = 100

        
    def  motor_left(self, speed):
        if speed > 100:
            speed = 100
    
    def  motor_right(self, speed):
        if speed > 100:
            speed = 100

if __name__ == '__main__':

    car = CarMotor()
    try:
        while True:
            car.motor_forward(100)
            time.sleep(2)
            car.motor_stop()
            time.sleep(2)
            car.motor_left(100)
            time.sleep(2)
            car.motor_stop()
            time.sleep(2)        
            car.motor_backward(100)
            time.sleep(2)
            car.motor_stop()
            time.sleep(2)
    except KeyboardInterrupt:
        pass
    GPIO.cleanup()
