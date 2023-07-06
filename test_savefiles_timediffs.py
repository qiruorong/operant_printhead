import utime
from machine import Pin

valve = Pin(16, Pin.OUT)
led = Pin(25, Pin.OUT)
lick = Pin(14, Pin.IN, Pin.PULL_DOWN)
trial_id = []
trial_counter = 0
lickTimestamps = []
valveOpenTimestamps = []
trialEndTimestamps = []
file = open("trial_ids.txt","w")
trialStartTimestamps = []

# trial_diffs = []
# timediff_lick = []
# timediff_valve = []
# timediff_trialEnd = []

with open('timestamps.txt','w') as file:
    for i, trial_id in enumerate(trial_id):
        dict[trial_id] = {}
        dict[trial_id][lickTimestamps] = lickTimestamps[i]
        dict[trial_id][valveOpenTimestamps] = valveOpenTimestamps[i]
        dict[trial_id][trialEndTimestamps] = trialEndTimestamps[i]
        
# with open('timediffs.txt','w') as file:
    # for i, trial_diff in enumerate(trial_diffs):
         # dict[trial_diff] = {}
         # dict[trial_diff][timediff_lick] = timediff_lick[i]
         # dict[trial_diff][timediff_valve] = timediff_valve[i]
         # dict[trial_diff][timediff_trialEnd] = timediff_trialEnd[i]

# trial_diffs_num = utime.ticks_diff(trial_ids[-1],trial_ids[-1])
# trial_diffs.append(trial_diffs_num)

# timediff_lick_num = utime.ticks_diff(lickTimestamps[-1],trial_ids[-1])
# timediff_lick.append(timediff_lick_num)

# timediff_valve_num = utime.ticks_diff(valveOpenTimestamps[-1],trial_ids[-1])
# timediff_valve.append(timediff_valve_num)

# timediff_trialEnd_num = utime.ticks_diff(trialEndTimestamps[-1],trial_ids[-1])
# timediff_trialEnd.append(timediff_trialEnd_num)


while True:
    if lick.value():
        lickTimestamps.append(utime.ticks_ms())
        valve.value(0)
        led.toggle()
        utime.sleep(2)
        valve.value(1)
        valveOpenTimestamps.append(utime.ticks_ms())
        valve.value(0)
        trialEndTimestamps.append(utime.ticks_ms())
        trial_counter = trial_counter + 1
        trial_id.append(trial_counter)
        
        file.write(f"Trial ID:{trial_id}\n")
        file.write(f"Lick Times:{dict[trial_id]['lickTimestamps']}\n")
        file.write(f"Valve Open Times:{dict[trial_id]['valveOpenTimestamps']}\n")
        file.write(f"Trial End Times:{dict[trial_id]['trialEndTimestamps']}\n")
        file.write("\n")
        
        # file.write(f"Trial Time Difference:{trial_diff}\n")
        # file.write(f"Lick Time Difference:{dict[trial_diff]['timediff_lick']}\n")
        # file.write(f"Valve Open Time Difference:{dict[trial_diff]['timediff_valve']}\n")
        # file.write(f"Trial End Time Difference:{dict[trial_diff]['timediff_trialEnd']}\n")

        file.flush()
        utime.sleep(2)
    file.close()
