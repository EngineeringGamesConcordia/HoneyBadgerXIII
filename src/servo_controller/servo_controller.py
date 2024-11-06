# no clue what I am doing
# this is the first time I am working with a servo
# pls don't clown me

import serial
import time
import RPi.GPIO as GPIO

# Set up the servo GPIO pin
SERVO_PIN = 0 # change depending on pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)

# Create a PWM instance
servo_pwm = GPIO.PWM(SERVO_PIN, 50) # change if servo uses different frequency
servo_pwm.start(0) # Start with 0 duty cycle ?

# Function to move the servo based on the IBus input
# For IBus values from 0 to 1000
def move_servo(position):
    # Convert 1000 scale to 180 degrees (1000 / 180 ≈ 5.555)
    angle = position / 5.555 # Change scale if IBus values are different
    duty_cycle = angle / 18 + 2.5 # Map 0-180 degrees to duty cycle (2.5-12.5%)
    servo_pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(0.1) # Allow time for the servo to move

# Set up the serial connection to the Arduino
arduino_port = 'COM3' # Change depending on Arduino port
baud_rate = 9600 # Change to match the baud rate in the Arduino sketch
ser = serial.Serial(arduino_port, baud_rate)

ser.timeout = 1 # Set a timeout for the serial connection

try:
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').strip() # Read a line
            values = line.split(',') # Split the line into channel values

            # Assuming the servo moves based on a specific channel
            if len(values) > 0 and values[0].isdigit(): # Check if the first value is a digit
                channel_value = int(values[0]) # Convert the first channel value to an integer
                move_servo(channel_value) # Move the servo based on the channel value

except KeyboardInterrupt:
    print("Exiting...")

finally:
    servo_pwm.stop() # Stop the PWM
    GPIO.cleanup() # Clean up GPIO settings
    ser.close() # Close the serial connection
