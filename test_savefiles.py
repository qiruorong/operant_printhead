import utime
from machine import Pin

solenoid = Pin(16, Pin.OUT)
led = Pin(25, Pin.OUT)
lick = Pin(14, Pin.IN, Pin.PULL_DOWN)
solenoidOpenTimestamps = []
# lickTimestamps = []
file = open("solenoidOpenTimestamps.txt","w")

while True:
    if lick.value():
        led.toggle()
        solenoid.value(0)
        utime.sleep(2)
        solenoid.value(1)
        solenoidOpenTimestamps.append(utime.time())
        file.write(str(solenoidOpenTimestamps)+", ")
        file.flush()
        utime.sleep(2)
file.close()
