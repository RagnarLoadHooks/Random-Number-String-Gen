##generated random string of numbers based on date,time,cpufreq,memory usage. 


from datetime import datetime
import psutil
import random

def rand_numstring_gen():
    rsgen=datetime.now(),psutil.cpu_freq().current,psutil.virtual_memory().used
    for char in " datetimedatetime().,":
        rsgen=str(rsgen).replace(char, '')
    return(rsgen)

print(''.join(random.sample(rand_numstring_gen(),len(rand_numstring_gen()))))
