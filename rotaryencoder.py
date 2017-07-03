#Heavily modified from SunFounder code: https://www.sunfounder.com/learn/Super_Kit_V2_for_RaspberryPi/lesson-8-rotary-encoder-super-kit-for-raspberrypi.html
import threading
import RPi.GPIO as GPIO

class RotaryEncoder:
	_dtPin = 0
	_clkPin = 0
	_clockwiseCallback = None
	_counterClockwiseCallback = None
	_inputThread = None
	_threadStopEvent = None

	def __init__(self, dtPin, clkPin, clockwiseCallback, counterClockwiseCallback):
		self._dtPin = dtPin
		self._clkPin = clkPin
		self._clockwiseCallback = clockwiseCallback
		self._counterClockwiseCallback = counterClockwiseCallback
		self._threadStopEvent = threading.Event()

		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self._dtPin, GPIO.IN)
		GPIO.setup(self._clkPin, GPIO.IN)

	def listenForInput(self):
		self._inputThread = threading.Thread(target=self._listenForInput)
		self._inputThread.start()

	def stopListeningForInput(self):
		self._threadStopEvent.set()
		self._inputThread.join()		
	
	def _listenForInput(self):
		while not self._threadStopEvent.is_set():
			self._rotaryDeal()
		
		self._threadStopEvent.clear()

	def _rotaryDeal(self):
		lastClkStatus = GPIO.input(self._clkPin)
		currentClkStatus = 0
		flag = 0

		while(not GPIO.input(self._dtPin)):
			currentClkStatus = GPIO.input(self._clkPin)
			flag = 1

			if self._threadStopEvent.is_set():
				flag = 0
				break
		if flag == 1:
			flag = 0
			if (lastClkStatus == 0) and (currentClkStatus == 1):
				self._clockwiseCallback()
			if (lastClkStatus == 1) and (currentClkStatus == 0):
				self._counterClockwiseCallback()

