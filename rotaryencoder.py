#Lifted from SunFounder code: https://www.sunfounder.com/learn/Super_Kit_V2_for_RaspberryPi/lesson-8-rotary-encoder-super-kit-for-raspberrypi.html
import RPi.GPIO as GPIO
import time
import threading

RoAPin = 27
RoBPin = 17

flag = 0
Last_RoB_Status = 0
Current_RoB_Status = 0

stopInputThread = 0
inputThread = None

clockwiseCallBack = None
counterClockwiseCallBack = None

GPIO.setmode(GPIO.BCM)       # Numbers GPIOs by physical location
GPIO.setup(RoAPin, GPIO.IN)    # input mode
GPIO.setup(RoBPin, GPIO.IN)


def setup(clockwiseCB, counterClockwiseCB):
	global clockwiseCallBack
	global counterClockwiseCallBack

	clockwiseCallBack = clockwiseCB
	counterClockwiseCallBack = counterClockwiseCB

def rotaryDeal():
	global flag
	global Last_RoB_Status
	global Current_RoB_Status
	global globalCounter
	global clockwiseCallBack
	global counterClockwiseCallBack

	Last_RoB_Status = GPIO.input(RoBPin)

	while(not GPIO.input(RoAPin)):
		Current_RoB_Status = GPIO.input(RoBPin)
		flag = 1
	if flag == 1:
		flag = 0
		if (Last_RoB_Status == 0) and (Current_RoB_Status == 1):
			clockwiseCallBack()
		if (Last_RoB_Status == 1) and (Current_RoB_Status == 0):
			counterClockwiseCallBack()

def loop():
	global stopInputThread

	while not stopInputThread:
		rotaryDeal()

	stopInputThread = 0

def listenForInput():
	global stopInputThread
	global inputThread

	stopInputThread = 0

	inputThread = threading.Thread(target = loop)
	inputThread.start()

def stopListeningForInput():
	global stopInputThread

	stopInputThread = 1

# def destroy():
#	GPIO.cleanup()

#if __name__ == '__main__':     # Program start from here
#	setup()
#	try:
#		loop()
#	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
#		destroy()
