# Write your code here :-)
import RPi.GPIO as GPIO   # Import the GPIO library.
import time               # Import time library

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

try:
  while True:                      # Loop until Ctl C is pressed to stop.

    redRequest = int(input("RED:"))
    redpwm.ChangeDutyCycle(redRequest)

    greenRequest = int(input("GREEN:"))
    greenpwm.ChangeDutyCycle(greenRequest)

    blueRequest = int(input("BLUE:"))
    bluepwm.ChangeDutyCycle(blueRequest)

except KeyboardInterrupt:
  print("Ctl C pressed - ending program")
  GPIO.cleanup()

redpwm.stop() # stop PWM
bluepwm.stop()
GPIO.cleanup()