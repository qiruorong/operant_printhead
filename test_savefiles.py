import utime
from machine import Pin

solenoid = Pin(16, Pin.OUT)
led = Pin(25, Pin.OUT)
lick = Pin(14, Pin.IN, Pin.PULL_DOWN)
solenoidOpenTimestamps = []
# lickTimestamps = []
file = open("solenoidOpenTimestamps5.txt","w")
start_time = utime.ticks_ms()

while True:
    if lick.value():
        led.toggle()
        solenoid.value(0)
        utime.sleep(2)
        solenoid.value(1)
        solenoidOpenTimestamps.append(utime.ticks_diff(utime.ticks_ms(),start_time))
       
        # ticks
        # trial start time
        # close trial and start running, write in same file
        with open("solenoidOpenTimestamps5.txt","r") as file:
            file.write(str(solenoidOpenTimestamps)+", ")
            file.flush()
        utime.sleep(2)
    file.close()

