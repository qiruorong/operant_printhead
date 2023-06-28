import numpy as np
from machine import Pin
import utime
import RPi.GPIO as GPIO



#def Pi1():
    # GPIO.setmode(GPIO.BOARD)
    pinDict = {}
    pins = [4,5,6,7,9,10,11,12,13,14,15,16,17,19,20,21,22,24,25,26,27,29,31,32,34]
    for pin in pins:
        pinDict[pin] = Pin(pin,Pin.OUT,Pin.PULL_DOWN)
    rewardPinOut = Pin(1,Pin.OUT,Pin.PULL_DOWN)
    trialPin = Pin(0,Pin.OUT,Pin.PULL_DOWN)

rewardPinIn = Pin(1,Pin.IN,Pin.PULL_DOWN)
valvePinOut = Pin(16,Pin.OUT,Pin.PULL_DOWN)
lickPinIn = Pin(17,Pin.IN,Pin.PULL_DOWN)

#def Pi2():
    # GPIO.setmode(GPIO.BOARD)
     rewardPinIn = Pin(1,Pin.IN,Pin.PULL_DOWN)
     valvePinOut = Pin(5,Pin.OUT,Pin.PULL_DOWN)
     lickPinIn = Pin(4,Pin.IN,Pin.PULL_DOWN)


############ trial start #############
trialstartTimestamps = []
user_input = input("Press Enter to start the trail")
if user_input == "":
    trialPin.value() == 1
    trialstartTimestamps.append(utime.time())
    print("Trail begin")
np.save('filenameTBD.npy',np.array(trialstartTimestamps))


############ activating printHead ############
# pinIn
# sweep
# pinOut
# save pin end time

for i, pin in enumerate(pins):
    pins[i] = 'Dev1/' + pin

# Define parameters
tone_duration = 0.5  # seconds
Fs = 200
speed = 0.1 # in mm/s
time_stim = 1/speed 
overlap = 3 # #of pins to have activated at once
pinOrder = [1, 13, 2, 14, 3, 15, 4, 16, 5, 17, 6, 18, 7, 19, 8, 20, 9, 21, 10, 22, 11, 23, 12, 24]
time_pin = (overlap * time_stim) / (24 + overlap - 1)
time_pin_samples = int(np.floor(time_pin * Fs))
numSamples = int(time_stim*Fs)
stim = np.zeros((24, numSamples))
    
for i in range(24): # for each pin
    if i == 0:
        indentStart = 0
    else:
        indentStart = int(np.floor((i-1)/(24+overlap-1) * time_stim * Fs))
    indentEnd = indentStart + time_pin_samples
    if indentEnd > time_stim * Fs:
        indentEnd = int(np.floor(time_stim * Fs - 1))
    stim[pinOrder[i]-1, indentStart:indentEnd] = 1

    # fullStim = np.tile(np.concatenate(stim,axis = 1), (1, num_sweeps))
    # fullTrigger = np.zeros((len(fullStim), 1))
    # fullTrigger[1:-1] = 1

for sample in range(numSamples):
    for i, pin in enumerate(pins):
        pinDict[pin].value(stim[i,sample])
    utime.sleep(1/Fs)
    
# digital_signal = stim
# task.write(digital_signal, auto_start=True)

printEndtime = utime.time()
np.save('filenameTBD.npy',np.array(printEndtime))


############ activating reward window ###########
# if pin end, rewardWindow open
# sleep()
# save rewardWindow open time

rewardWindowStart = []
rewardWindowStart = utime.time()
print("Reward Window open")
np.save('filenameTBD.npy',np.array(rewardWindowStart))


############ interrupt when lick ###########
# interrupt rewardWindow sleep() when lickPinIn
# save lick time

lickPinIn = 0
debounce_time = 0
pin = Pin(4, Pin.IN, Pin.PULL_DOWN)
valvePinOut = Pin(0,Pin.OUT)
# count=0
# creates a list of timestamps
lickTimestamps = []
# an interrupt to give water when lick is registered (valve is opened and timestamp is recorded)
def lickCallback():
    # adds current timestamp to the list
    lickTimestamps.append(utime.time())
    global lickPinIn, debounce_time
    if (time.ticks_ms()-debounce_time) > 100:
        lickPinIn = 1
        debounce_time = time.ticks_ms()
pin.irq(trigger=Pin.IRQ_RISING, handler=callback)

             
############ reward when lick in reward window ##########
# lickPinIn + rewardPinOut -> valvePinIn
# save reward time
# mice lick one time in one trail

stimulus_duration = 7
valveOpenDuration = 1

while utime.time() - start_time < stimulus_duration:
     if lickPinIn.value() == 1 and rewardPinIn.value() == 1:
        valvePinOut.value(1)
        utime.sleep(valveOpenDuration)
        valvePinOut.value(0)
        print('Lick Detected')
        np.save('filenameTBD.npy',np.array(lickTimestamps))


############ end trail ###########
# close reward window
# trail end

trialPin.value() == 0
utime.sleep(10)
