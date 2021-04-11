# Write your code here :-)
import RPi.GPIO as GPIO   # Import the GPIO library.

flag = False

def init():
    flag = True
    GPIO.setmode(GPIO.BOARD)  # Set Pi to use pin number when referencing GPIO pins.
                              # Can use GPIO.setmode(GPIO.BCM) instead to use
                              # Broadcom SOC channel names.

    GPIO.setup(12, GPIO.OUT)  # Set GPIO pin 12 to output mode.
    GPIO.setup(18, GPIO.OUT)  # Set GPIO pin 12 to output mode.
    GPIO.setup(24, GPIO.OUT)

    redpwm = GPIO.PWM(12, 100)   # Initialize PWM on pwmPin 100Hz frequency
    greenpwm = GPIO.PWM(18, 100)   # Initialize PWM on pwmPin 100Hz frequency
    bluepwm = GPIO.PWM(24, 100)

    redpwm.start(0)                      # Start PWM with 0% duty cycle
    greenpwm.start(0)
    bluepwm.start(0)

def displayColor(r, g, b): #Accepts RGB values on 255 scale
    if not flag:
      init()
      
    redRequest = int(r)
    redpwm.ChangeDutyCycle(redRequest)

    greenRequest = int(g)
    greenpwm.ChangeDutyCycle(greenRequest)

    blueRequest = int(b)
    bluepwm.ChangeDutyCycle(blueRequest)

if __name__ == "__main__":
    print('loaded')
    init()