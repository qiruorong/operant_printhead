import utime
from machine import Pin

valvePinOut = Pin(16,Pin.OUT)
led = Pin(25,Pin.OUT)
lickPinIn = Pin(14,Pin.IN,Pin.PULL_DOWN)
valvePinIn = Pin(15,Pin.IN,Pin.PULL_DOWN)
stimulusPinOut = Pin(0,Pin.OUT)
rewardwinPinIn = Pin(1,Pin.IN,Pin.PULL_DOWN)
trialPinIn = Pin(4,Pin.IN,Pin.PULL_DOWN)

interrupt_flag = 0
valveOpenDuration = 1
trial_counter = 0
trial_ids = []
trialStartTimestamps = []
stimulusStartTimestamps = []
rewardwinOpenTimestamps = []
lick_times = []
valveOpenTimestamps = []
trialEndTimestamps = []

trial_diffs = []
timediff_rewardwinopen = []
timediff_lick = []
timediff_valve = []
timediff_trialEnd = []

trial_counter += 1
trial_ids[trial_counter] = {
    'trialStartTimestamps':trialStartTimestamps[-1],
    'stimulusStartTimestamps':stimulusStartTimestamps[-1],
    'rewardwinOpenTimestamps':rewardwinOpenTimestamps[-1],
    'lick_times':lick_times[-1],
    'valveOpenTimestamps':valveOpenTimestamps[-1],
    'trialEndTimestamps':trialEndTimestamps[-1]
}

with open('timestamps.txt', 'w') as file:
    for i, trial_id in enumerate(trial_ids):
        dict[trial_id] = {}
        dict[trial_id][trialStartTimestamps] = trialStartTimestamps[i]
        dict[trial_id][stimulusStartTimestamps] = stimulusStartTimestamps[i]
        dict[trial_id][rewardwinOpenTimestamps] = rewardwinOpenTimestamps[i]
        dict[trial_id][lick_times] = lick_times[i]
        dict[trial_id][valveOpenTimestamps] = valveOpenTimestamps[i]
        dict[trial_id][trialEndTimestamps] = trialEndTimestamps[i]

with open('time_diffs.txt','w') as file:
    for i, trial_diff in enumerate(trial_diffs):
        dict[trial_diff] = {}
        dict[trial_diff][timediff_rewardwinopen] = timediff_rewardwinopen[i]
        dict[trial_diff][timediff_lick] = timediff_lick[i]
        dict[trial_diff][timediff_valve] = timediff_valve[i]
        dict[trial_diff][timediff_trialEnd] = timediff_trialEnd[i]

trialStartTimestamps = utime.ticks_ms()

timediff_rewardwinopen_num = utime.ticks_diff(rewardwinOpenTimestamps[-1],trialStartTimestamps[-1])
timediff_rewardwinopen.append(timediff_rewardwinopen_num)
# if timediff_rewardwinopen[-1] > 20:
#     trialStartTimestamps[-1] = rewardwinOpenTimestamps[-1]

timediff_lick_num = utime.ticks_diff(lick_times[-1],trialStartTimestamps[-1])
timediff_lick.append(timediff_lick_num)
# if timediff_lick[-1] > 20:
#     trialStartTimestamps[-1] = lick_times[-1]

timediff_valve_num = utime.ticks_diff(valveOpenTimestamps[-1],trialStartTimestamps[-1])
timediff_valve.append(timediff_valve_num)
# if timediff_valve[-1] > 20:
#    trialStartTimestamps[-1] = valveOpenTimestamps[-1]

timediff_trialEnd_num = utime.ticks_diff(trialEndTimestamps[-1],trialStartTimestamps[-1])
timediff_trialEnd.append(timediff_trialEnd_num)
# if timediff_trialEnd[-1] > 1000:
#     trialStartTimestamps[-1] = trialEndTimestamps[-1]

def runTrial():
    if trialPinIn.value(1):
        trialStartTimestamps.append(utime.ticks_ms())
        stimulusPinOut.value(1)
        stimulusStartTimestamps.append(utime.ticks_ms())
        if stimulusPinOut.value(1):
            stimulusPinOut.value(0)
        if rewardwinPinIn.value(1):
            rewardwinOpenTimestamps.append(utime.ticks_ms())
        def lickCallback(lickPinIn):
            global interrupt_flag
            lick_times.append(utime.ticks_ms())
            interrupt_flag = 1
        lickPinIn.irq(trigger=lickPinIn.IRQ_RISING, handler=lickCallback)
    def openValve(duration):
        valvePinOut.value(1)
        valveOpenTimestamps.append(utime.ticks_ms())
        utime.sleep_ms(duration)
        valvePinOut.value(0)

    if interrupt_flag is 1:
        interrupt_flag = 0
        if (rewardwinPinIn.value is 1) & (utime.ticks_diff(utime.ticks_ms,valveOpenTimestamps[-1]) > 1000):
            valveOpenTimestamps.append(utime.ticks_ms())
            openValve(20)
    else:
        utime.sleep(7)

file.write(f"Trial ID: {trial_id}\n")
file.write(f"Trial Start Times: {dict[trial_id]['trialStartTimestamps']}\n")
file.write(f"Stimulus Start Times: {dict[trial_id]['stimulusStartTimestamps']}\n")
file.write(f"Reward Window Open Times: {dict[trial_id]['rewardwinOpenTimestamps']}\n")
file.write(f"Lick Times: {dict[trial_id]['lick_times']}\n")
file.write(f"Valve Open Times: {dict[trial_id]['valveOpenTimestamps']}\n")
file.write(f"Trial End Times: {dict[trial_id]['trialEndTimestamps']}\n")
file.write("\n")
file.flush()

file.write(f"Time Difference: {trial_diffs}\n")
file.write(f"Reward Window Open Time Difference: {dict[trial_id]['timediff_rewardwinopen']}\n")
file.write(f"Lick Time Difference: {dict[trial_id]['lick_times']}\n")
file.write(f"Valve Open Time Difference: {dict[trial_id]['timediff_valve']}\n")
file.write(f"Trial End Time Difference: {dict[trial_id]['timediff_trialEnd']}\n")
file.write("\n")
file.flush()


# main Trial:
while True:
    for i in range(100):
        runTrial()
            
