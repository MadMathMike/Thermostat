import shiftpi

class TwoDigitDisplay:
  def __init__(self):
    shiftpi.pinsSetup(18, 23, 24)
    shiftpi.shiftRegisters(2)
    shiftpi.startupMode(shiftpi.LOW, True)

  def show(self, number):
    firstDigit = (number % 100)/10
    secondDigit = number % 10

    shiftpi.digitalWrite(shiftpi.ALL, shiftpi.LOW)
    self._writeDigit(firstDigit)
    self._writeDigit(secondDigit, 1)

  def clear(self):
    shiftpi.digitalWrite(shiftpi.ALL, shiftpi.LOW)

  def _writeDigit(self, value, position = 0):
    pins = [];

    if value == 0:
      pins = [6, 1, 2, 3, 4, 5]
    if value == 1:
      pins = [1, 2]
    if value == 2:
      pins = [6, 1, 7, 3, 4]
    if value == 3:
      pins = [6, 1, 7, 2, 3]
    if value == 4:
      pins = [5, 7, 1, 2]
    if value == 5:
      pins = [6, 5, 7, 2, 3]
    if value == 6:
      pins = [6, 5, 4, 3, 2, 7]
    if value == 7:
      pins = [6, 1, 2]
    if value == 8:
      pins = [1, 2, 3, 4, 5, 6, 7]
    if value == 9:
      pins = [1, 6, 5, 7, 2]

    for pin in pins:
      shiftpi.digitalWrite(pin + position * 8, shiftpi.HIGH)

