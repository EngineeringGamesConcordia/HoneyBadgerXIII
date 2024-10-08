# No clue what I am doing
# This is the first time I am working with a servo
# Controlling servo rotation with keyboard inputs

import time
import keyboard

class ServoController:
    """
    Initialize the ServoController with a specific pin and optional angle limits.
        pin: GPIO pin connected to the servo motor.
        min_angle: Minimum allowed angle for the servo (default is 0).
        max_angle: Maximum allowed angle for the servo (default is 180).
    """
    def __init__(self, pin: int, min_angle: int = 0, max_angle: int = 180):
        self.pin = pin
        self.min_angle = min_angle
        self.max_angle = max_angle
        self.current_angle = 0  # Default starting position


    """
    Move the servo to the specified angle if within allowed range.
        angle: Target angle to move the servo to.
    """
    def move_to(self, angle: int):
        if self.min_angle <= angle <= self.max_angle:
            self.current_angle = angle
            # TODO Code to move the servo
            print(f"Servo moved to {self.current_angle} degrees")
        else:
            print(f"Angle {angle} is out of range ({self.min_angle} - {self.max_angle})")
    

    """
    Continuously move the servo to the right (increasing angle) while the right arrow key is held down.
        step_size: The amount by which the servo angle increases with each step (default is 1 degree).
        delay: Time delay between steps (default is 0.1 seconds).
    """
    def move_continuously(self, step_size: int = 1, delay: float = 0.1):
        print("Press and hold the right arrow key to move the servo. Release to stop.")
        try:
            while True:
                # Move the servo to the right while the right arrow key is pressed
                if keyboard.is_pressed("right"):
                    if self.current_angle + step_size <= self.max_angle:
                        self.current_angle += step_size
                        print(f"Moving to {self.current_angle}°")
                        # TODO code to physically move the servo
                    else:
                        print("Reached maximum angle.")
                
                # Move the servo to the left while the left arrow key is pressed
                elif keyboard.is_pressed('left'):
                    if self.current_angle - step_size >= self.min_angle:
                        self.current_angle -= step_size
                        print(f"Moving to {self.current_angle} degrees (left)")
                        # TODO code to physically move the servo
                    else:
                        print("Reached minimum angle.")
                
                # Sleep for a short time to avoid overwhelming the CPU and servo motor
                time.sleep(delay)
        
        except KeyboardInterrupt:
            print("Movement stopped.")
    

    def get_current_angle(self) -> int:
        return self.current_angle
    
    
    """String representation of a ServoController object"""
    def __repr__(self):
        return f"ServoController(pin={self.pin}, min_angle={self.min_angle}°, max_angle={self.max_angle}°)"

# Test:
servo = ServoController(pin=0)
servo.move_continuously()
servo.move_to(90)
print(f"Current angle: {servo.get_current_angle()} degrees")
