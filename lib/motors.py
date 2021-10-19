# Raspberry Pi + MG90S Servo PWM Control Python Code
#
#
import RPi.GPIO as GPIO
import time

def setup(servo_left, servo_right):

# setup the GPIO pin for the servo
	#servo_pin = 13
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(servo_left,GPIO.OUT)
	GPIO.setup(servo_right,GPIO.OUT)

# setup PWM process
	pwm_left = GPIO.PWM(servo_left,50) # 50 Hz (20 ms PWM period)
	pwm_right = GPIO.PWM(servo_right,50) # 50 Hz (20 ms PWM period)

def closeHelmet ():
	pwm_left.ChangeDutyCycle(2.0)
	pwm_right.ChangeDutyCycle(12.0)
	time.sleep(0.5)
	pwm_left.ChangeDutyCycle(0) # this prevents jitter
	pwm_right.ChangeDutyCycle(0) # this prevents jitter	

def openHelmet ():
	pwm_left.ChangeDutyCycle(12.0)
	pwm_right.ChangeDutyCycle(2.0)
	time.sleep(0.5)
	pwm_left.ChangeDutyCycle(0) # this prevents jitter
	pwm_right.ChangeDutyCycle(0) # this prevents jitter	

def destroy():
	pwm_left.stop()
	pwm_right.stop()
