# taken from https://github.com/mignev/shiftpi because I couldn't figure out how to install the package/module correctly
'''
A library that allows simple access to 74HC595 shift registers on a Raspberry Pi using any digital I/O pins.
'''


import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

version = "0.2"
version_info = (0, 2)

# Define MODES
ALL  = -1
HIGH = 1
LOW  = 0

# Define pins
_SER_pin = 0 #pin 14 on the 75HC595
_RCLK_pin = 0 #pin 12 on the 75HC595
_SRCLK_pin = 0 #pin 11 on the 75HC595

# is used to store states of all pins
_registers = list()

#How many of the shift registers - you can change them with shiftRegisters method
_number_of_shiftregisters = 1

def pinsSetup(ser, rclk, srclk):
    '''
    Allows the user to define custom pins
    '''
    global _SER_pin, _RCLK_pin, _SRCLK_pin
    GPIO.setwarnings(True)

    _SER_pin = ser
    _RCLK_pin = rclk
    _SRCLK_pin = srclk

    print('SER pin: ' + str(_SER_pin))
    print('RCLK pin: ' + str(_RCLK_pin))
    print('SRCLK pin: ' + str(_SRCLK_pin))

    GPIO.setwarnings(False)

    GPIO.setup(_SER_pin, GPIO.OUT)
    GPIO.setup(_RCLK_pin, GPIO.OUT)
    GPIO.setup(_SRCLK_pin, GPIO.OUT)

def startupMode(mode, execute = False):
    '''
    Allows the user to change the default state of the shift registers outputs
    '''
    if isinstance(mode, int):
        if mode is HIGH or mode is LOW:
            _all(mode, execute)
        else:
            raise ValueError("The mode can be only HIGH or LOW or Dictionary with specific pins and modes")
    elif isinstance(mode, dict):
        for pin, mode in mode.iteritems():
            _setPin(pin, mode)
        if execute:
            _execute()
    else:
        raise ValueError("The mode can be only HIGH or LOW or Dictionary with specific pins and modes")


def shiftRegisters(num):
    '''
    Allows the user to define the number of shift registers are connected
    '''
    global _number_of_shiftregisters
    _number_of_shiftregisters = num
    _all(LOW)

def digitalWrite(pin, mode):
    '''
    Allows the user to set the state of a pin on the shift register
    '''
    if pin == ALL:
        _all(mode)
    else:
        if len(_registers) == 0:
            _all(LOW)

        _setPin(pin, mode)
    _execute()

def delay(millis):
    '''
    Used for creating a delay between commands
    '''
    millis_to_seconds = float(millis)/1000
    return sleep(millis_to_seconds)

def _all_pins():
    return _number_of_shiftregisters * 8

def _all(mode, execute = True):
    all_shr = _all_pins()

    for pin in range(0, all_shr):
        _setPin(pin, mode)
    if execute:
        _execute()

    return _registers

def _setPin(pin, mode):
    try:
        _registers[pin] = mode
    except IndexError:
        _registers.insert(pin, mode)

def _execute():
    all_pins = _all_pins()
    GPIO.output(_RCLK_pin, GPIO.LOW)

    for pin in range(all_pins -1, -1, -1):
        GPIO.output(_SRCLK_pin, GPIO.LOW)

        pin_mode = _registers[pin]

        GPIO.output(_SER_pin, pin_mode)
        GPIO.output(_SRCLK_pin, GPIO.HIGH)

    GPIO.output(_RCLK_pin, GPIO.HIGH)

