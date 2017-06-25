import shiftpi

shiftpi.pinsSetup(18, 23, 24)
shiftpi.startupMode(shiftpi.LOW, True)

def _writeDigit(value):
  shiftpi.digitalWrite(shiftpi.ALL, shiftpi.LOW)

  if value == 0:
    _digitalWriteHigh([6, 1, 2, 3, 4, 5])
  if value == 1:
    _digitalWriteHigh([1, 2])
  if value == 2:
    _digitalWriteHigh([6, 1, 7, 3, 4])
  if value == 3:
    _digitalWriteHigh([6, 1, 7, 2, 3])
  if value == 4:
    _digitalWriteHigh([5, 7, 1, 2])
  if value == 5:
    _digitalWriteHigh([6, 5, 7, 2, 3])
  if value == 6:
    _digitalWriteHigh([6, 5, 4, 3, 2, 7])
  if value == 7:
    _digitalWriteHigh([6, 1, 2])
  if value == 8:
    _digitalWriteHigh([1, 2, 3, 4, 5, 6, 7])
  if value == 9:
    _digitalWriteHigh([1, 6, 5, 7, 2])

def _digitalWriteHigh(pins):
  for pin in pins:
    shiftpi.digitalWrite(pin, shiftpi.HIGH)

for digit in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
  _writeDigit(digit)
  shiftpi.delay(500)

shiftpi.digitalWrite(shiftpi.ALL, shiftpi.LOW)

