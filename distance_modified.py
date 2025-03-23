import RPi.GPIO as GPIO
import time

"""
Distance Measurement with HC-SR04 Sensor
----------------------------------------
This script measures and logs distance using an HC-SR04 ultrasonic sensor 
connected to a Raspberry Pi.

Features:
- Continuously displays distance readings.
- Converts distance from centimeters to inches.
- Includes a sensor initialization delay for accuracy.
- Proper GPIO cleanup on exit.

Author: Modified by Keith Thomson
"""

# Define GPIO pins
TRIGGER_PIN = 7
ECHO_PIN = 11

# Speed of sound in air (34300 cm/s divided by 2 for one-way travel)
SPEED_OF_SOUND_CM = 34300 / 2  
CM_TO_INCH = 0.393701  # Conversion factor

def setup():
    """Initialize GPIO settings."""
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(TRIGGER_PIN, GPIO.OUT)
    GPIO.setup(ECHO_PIN, GPIO.IN)
    GPIO.output(TRIGGER_PIN, GPIO.LOW)

    print("Initializing sensor...")
    time.sleep(2)  # Allow sensor to settle

def get_distance():
    """Measures distance using HC-SR04 and returns it in cm and inches."""
    # Send trigger pulse
    GPIO.output(TRIGGER_PIN, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(TRIGGER_PIN, GPIO.LOW)

    # Record the last low and high timestamps
    pulse_start = pulse_end = time.time()

    while GPIO.input(ECHO_PIN) == 0:
        pulse_start = time.time()

    while GPIO.input(ECHO_PIN) == 1:
        pulse_end = time.time()

    # Calculate pulse duration and convert to distance
    pulse_duration = pulse_end - pulse_start
    distance_cm = round(pulse_duration * SPEED_OF_SOUND_CM, 2)
    distance_in = round(distance_cm * CM_TO_INCH, 2)

    return distance_cm, distance_in

def main():
    """Continuously reads and displays distance measurements."""
    setup()
    try:
        while True:
            cm, inches = get_distance()
            print(f"Distance: {cm} cm | {inches} inches")
            time.sleep(1)  # Adjust frequency of measurements
    except KeyboardInterrupt:
        print("\nMeasurement stopped by user. Cleaning up GPIO...")
        GPIO.cleanup()

if __name__ == "__main__":
    main()
