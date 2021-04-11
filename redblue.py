# Write your code here :-)
import RPi.GPIO as GPIO   # Import the GPIO library.
import time               # Import time library

GPIO.setmode(GPIO.BOARD)  # Set Pi to use pin number when referencing GPIO pins.
                          # Can use GPIO.setmode(GPIO.BCM) instead to use
                          # Broadcom SOC channel names.

GPIO.setup(12, GPIO.OUT)  # Set GPIO pin 12 to output mode.
redpwm = GPIO.PWM(12, 100)   # Initialize PWM on pwmPin 100Hz frequency
bluepwm = GPIO.PWM(18, 100)   # Initialize PWM on pwmPin 100Hz frequency



redpwm.start(0)                      # Start PWM with 0% duty cycle
bluepwm.start(0)

try:
  while True:                      # Loop until Ctl C is pressed to stop.
      redpwm.ChangeDutyCycle(50)
      time.sleep(22)
      print("half red")

      redpwm.ChangeDutyCycle(100)
      time.sleep(22)
      print("full red")

      redpwm.ChangeDutyCycle(50)
      time.sleep(22)
      print("half blue")

      redpwm.ChangeDutyCycle(100)
      time.sleep(22)
      print("full blue")

except KeyboardInterrupt:
  print("Ctl C pressed - ending program")

pwm.stop()                         # stop PWM
GPIO.cleanup()