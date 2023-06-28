import numpy as np
from machine import Pin
import utime

valvePinOut = Pin(16,Pin.OUT)
led = Pin(25,Pin.OUT)
lickPinIn = Pin(14,Pin.IN,Pin.PULL_DOWN)
rewardPinIn = Pin(15,Pin.IN,Pin.PULL_DOWN)
trialPin = Pin(0,Pin.IN)
interrupt_flag = 0
valveOpenDuration = 1
TrialEndTime = []
stimulusStartTimes = []
lickTimes = []
rewardTimes = []


if trialPin.value(1):
    stimulusStartTimes.append(utime.ticks_ms())
    def lickCallback(lickPinIn):
        global interrupt_flag
        lickTimes.append(utime.ticks_ms())
        interrupt_flag = 1
    lickPinIn.irq(trigger=lickPinIn.IRQ_RISING, handler=lickCallback)
def openValve(duration):
    valvePinOut.value(1)
    utime.sleep_ms(duration)
    valvePinOut.value(0)

    
while True:
    if interrupt_flag is 1:
        interrupt_flag = 0
        if (rewardPinIn.value is 1) & (utime.ticks_diff(utime.ticks_ms,rewardTimes[-1]) > 1000):
            rewardTimes.append(utime.ticks_ms())
            openValve(20)
        
    trialPin.value(0)
    printTrialEndtime = utime.time()
    np.save('TrialEndTimeFile.npy',np.array(printTrialEndtime))
    utime.sleep(10)
