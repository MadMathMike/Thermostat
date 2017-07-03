#depends on library w1thermsensor library found here:  https://github.com/timofurrer/w1thermsensor
#relevant command from above link: sudo apt-get install python-w1thermsensor
import time
import RPi.GPIO as GPIO
from w1thermsensor import W1ThermSensor
from rotaryencoder import RotaryEncoder
from twodigitdisplay import TwoDigitDisplay

switchpin = 22
minTemp = 60
maxTemp = 80
targetTemp = 73
thermostatIsOn = 0

sensor = W1ThermSensor()
display = TwoDigitDisplay()

GPIO.setmode(GPIO.BCM)
GPIO.setup(switchpin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def getTemp():
  temp = sensor.get_temperature(W1ThermSensor.DEGREES_F)
  return int(round(temp))

def dialTurnedUp():
  global maxTemp
  global targetTemp
  global display

  if(targetTemp < maxTemp):
    targetTemp += 1

  display.show(targetTemp)

def dialTurnedDown():
  global minTemp
  global targetTemp
  global display

  if(targetTemp > minTemp):
    targetTemp -= 1

  display.show(targetTemp)

def turnThermostatOn():
  global targetTemp
  global thermostatIsOn
  global encoder

  display.show(targetTemp)
  time.sleep(3)

  # turn on background thread to read rotary input
  encoder.listenForInput()

  thermostatIsOn = 1

  # turn on background threads for temp display and ac unit management

def turnThermostatOff():
  global thermostatIsOn
  global encoder
  global display

  # turn off background thread for rotary input
  encoder.stopListeningForInput()

  # turn off background thread for temp display and turning on/off ac

  display.clear()

  thermostatIsOn = 0

def turnThermostatOnOff(channel):
  global thermostatIsOn

  if(thermostatIsOn):
    turnThermostatOff()
  else:
    turnThermostatOn()

GPIO.add_event_detect(switchpin, GPIO.FALLING, callback=turnThermostatOnOff)

encoder = RotaryEncoder(27, 17, dialTurnedUp, dialTurnedDown)

turnThermostatOn()
