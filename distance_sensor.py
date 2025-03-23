import RPi.GPIO as GPIO 
import time


"""
Description: Measure and log distance using HC-SR04 Distance Sensor. 
"""

# TODO: Create a loop to continously display the distance values. 
# TODO: Convert to inches



try:
    GPIO.setmode(GPIO.BOARD)


    PIN_TRIGGER = 7
    PING_ECHO = 11


    GPIO.setup(PIN_TRIGGER, GPIO.OUT)
    GPIO.setup(PING_ECHO, GPIO.IN)

    GPIO.output(PIN_TRIGGER, GPIO.LOW)

    print ("Waiting for sensor to settle...")

    time.sleep(2)

    print("calculating distance....")

    GPIO.output(PIN_TRIGGER, GPIO.HIGH)

    time.sleep(0.00001)

    GPIO.output(PIN_TRIGGER, GPIO.LOW)

    while GPIO.input(PING_ECHO)==0:
        pulse_start_time = time.time()

    while GPIO.input(PING_ECHO)==1:
        pulse_end_time = time.time()




    pulse_duration = pulse_end_time - pulse_start_time
    distance = round(pulse_duration * 17150, 2)
    print("Distance: ", distance, "cm")

finally:

    GPIO.cleanup()


