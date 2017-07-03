#depends on library w1thermsensor library found here:  https://github.com/timofurrer/w1thermsensor
#relevant command from above link: sudo apt-get install python-w1thermsensor
import time
import rotaryencoder
import RPi.GPIO as GPIO
import twodigitdisplay as display
from w1thermsensor import W1ThermSensor

switchpin = 22
minTemp = 60
maxTemp = 80
targetTemp = 73
thermostatIsOn = 0

sensor = W1ThermSensor()
GPIO.setmode(GPIO.BCM)
GPIO.setup(switchpin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def getTemp():
  temp = sensor.get_temperature(W1ThermSensor.DEGREES_F)
  return int(round(temp))

def dialTurnedUp():
  global maxTemp
  global targetTemp

  if(targetTemp < maxTemp):
    targetTemp += 1

  display.show(targetTemp)

def dialTurnedDown():
  global minTemp
  global targetTemp

  if(targetTemp > minTemp):
    targetTemp -= 1

  display.show(targetTemp)

def turnThermostatOn():
  global targetTemp
  global thermostatIsOn

  display.show(targetTemp)
  time.sleep(3)

  # turn on background thread to read rotary input
  rotaryencoder.listenForInput()

  thermostatIsOn = 1

  # turn on background threads for temp display and ac unit management

def turnThermostatOff():
  global thermostatIsOn

  # turn off background thread for rotary input
  rotaryencoder.stopListeningForInput()

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

rotaryencoder.setup(dialTurnedUp, dialTurnedDown)

turnThermostatOn()
