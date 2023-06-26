
############## when to give reward ############
rewardPinIn = Pin(1, Pin.IN)
valvePinOut = Pin(0,Pin.OUT)
lickPinIn = Pin(4,Pin.IN)

GPIO.setmode(GPIO.BCM)
GPIO.setup(lickPinIn, GPIO.IN)
GPIO.setup(rewardPinIn, GPIO.IN)
GPIO.setup(valvePinOut, GPIO.OUT)

while True:
    # lickPinIn = GPIO.input(lickPinIn)
    # rewardPinIn = GPIO.input(rewardPinIn)
    # valvePinOut = GPIO.output(valvePinOut)
    
    if lickPinIn == GPIO.HIGH and rewardPinIn == GPIO.HIGH:
        GPIO.output(valvePinOut, GPIO.HIGH)
    else:
        GPIO.output(valvePinOut, GPIO.LOW)
    utime.sleep(10)
    
    # if abortIn == GPIO.HIGH and lickPinIn == GPIO.HIGH:
        # utime.sleep(10)
## interupt
# if a value change, do a sequence of event
# check the value of reward pin
# if high -> reward,record time,save

lickTimestamps = []
def lickCallback():
    lickTimestamps.append(utime.time())
    if rewardPinIn.value() == 1:
        valvePinOut.high()
        utime.sleep(valveOpenDuration)
        valvePinOut.low()
    ## save timestamps
    np.save('filenameTBD.npy',np.array(lickTimestamps))
    
    
## key items to save
# lick times
# trial starts
# reward window (maybe base on trial starts)
# trial identity (go/nogo)
