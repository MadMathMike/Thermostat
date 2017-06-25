#depends on library w1thermsensor library found here:  https://github.com/timofurrer/w1thermsensor
#relevant command from above link: sudo apt-get install python-w1thermsensor
from w1thermsensor import W1ThermSensor
from twodigitoutput import writeNumber, clearOutput

sensor = W1ThermSensor()

def displayTemp():
  temp = sensor.get_temperature(W1ThermSensor.DEGREES_F)
  writeNumber(int(round(temp)))

def clearDisplay():
  clearOutput()

