# Thermostat
The main AC unit in my apartment is not performing very well: The upstairs gets way too hot. There is a separate, in-window AC unit upstairs though, but that unit does not have a working thermostat. So I figured I'd build a thermostat with a raspberry pi zero w that can control (through RF) the socket that the AC unit is plugged into.

Requires adding OneWire support: https://learn.adafruit.com/adafruits-raspberry-pi-lesson-11-ds18b20-temperature-sensing?view=all

Requires installing the python 2 version of w1thermsensor: https://github.com/timofurrer/w1thermsensor
