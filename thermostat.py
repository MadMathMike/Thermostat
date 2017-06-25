#depends on library w1thermsensor library found here:  https://github.com/timofurrer/w1thermsensor
#relevant command from above link: sudo apt-get install python-w1thermsensor
from w1thermsensor import W1ThermSensor

sensor = W1ThermSensor()
temperature_in_fahrenheit = sensor.get_temperature(W1ThermSensor.DEGREES_F)

print(temperature_in_fahrenheit)

