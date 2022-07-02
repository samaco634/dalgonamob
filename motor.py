import RPi.GPIO as GPIO
import time

PWMA = 18
AIN1 = 24
AIN2 = 25

PWMB = 23
BIN1 = 22
BIN2 = 27

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(PWMA,GPIO.OUT)
GPIO.setup(AIN1,GPIO.OUT)
GPIO.setup(AIN2,GPIO.OUT)

GPIO.setup(PWMB,GPIO.OUT)
GPIO.setup(BIN1,GPIO.OUT)
GPIO.setup(BIN2,GPIO.OUT)


L_Motor = GPIO.PWM(PWMA,500)
L_Motor.start(0)

R_Motor = GPIO.PWM(PWMB,500)
R_Motor.start(0)

def motor_forward(speed):
    GPIO.output(AIN1,0)
    GPIO.output(AIN2,1)
    L_Motor.ChangeDutyCycle(speed)


def motor_backward(speed):
	pass

    
def motor_left(speed):
	pass
    
def motor_right(speed):
	pass


def motor_stop():
	pass

if __name__ == '__main__':

	try:
    	while True:
			motor_forward(100)
			time.sleep(2)
			motor_stop()
			time.sleep(2)
			motor_left(100)
			time.sleep(2)
			motor_stop()
			time.sleep(2)

			car.motor_backward(100)
			time.sleep(2)
			car.motor_stop()
			time.sleep(2)
	except KeyboardInterrupt:
    	pass

    GPIO.cleanup()
