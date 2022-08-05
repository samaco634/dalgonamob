import time
import cv2
import RPi.GPIO as GPIO
import numpy as np

from tensorflow.keras.models import load_model
from motor import CarMotor


motors = CarMotor()
speedSet = 35
turnSpeedSet = 35

def img_preprocess(image):
    image_array = np.asarray(image)
# Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
# Load the image into the array
    data = np.array([normalized_image_array])
    
    return data


        
def main():
    
    model_path = './keras_model.h5'
    model = load_model(model_path)
    
    carState = "stop"
 
  
    camera = cv2.VideoCapture(-1)
    camera.set(3, 224)
    camera.set(4, 224)
    camera.set(cv2.CAP_PROP_BUFFERSIZE, 1)
        
    try:
        while True:
            keyValue = cv2.waitKey(1)
        
            if keyValue == ord('q') :
                break
            elif keyValue == 82 :
                print("go")
                carState = "go"
            elif keyValue == 84 :
                print("stop")
                carState = "stop"
                motors.motor_stop()
                
            if 1:
                getNewFrame, image = camera.read()

                if getNewFrame == True :
                    X = img_preprocess(image)
            
                    prediction = int(model.predict(X)[0])
                    print("predicted :",prediction, time.ctime())
                
                    if carState == "go":
                        if np.argmax(prediction) == 0:
                            print("go")
                            motors.motor_forward(speedSet)

                        elif np.argmax(prediction) == 1:
                             print("left")
                             motors.motor_left(turnSpeedSet)
                        elif np.argmax(prediction) ==2:
                             print("right")
                             motors.motor_right(turnSpeedSet)
                 
                    cv2.imshow('org', image)
                
        camera.release()
  
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    main()
    GPIO.cleanup()
    cv2.destroyAllWindows()
