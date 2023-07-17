import machine
import utime

pin = machine.Pin(15, machine.Pin.OUT)

while True:
    pin.value(1)  # Set the pin HIGH
    utime.sleep(1)  # Wait for 1 second
    pin.value(0)  # Set the pin LOW
    utime.sleep(1)  # Wait for 1 second
