#Imports
from os.path import join
import os
from obspy import read
import numpy as np
import pandas as pd
#import matplotlib as plt
import matplotlib.pyplot as plt
from matplotlib import cm
from datetime import datetime, timedelta
from os.path import join
from obspy.signal.trigger import classic_sta_lta, trigger_onset, recursive_sta_lta
#hello
data_directory = './data/lunar/training/data/S12_GradeA/'
cat_directory = './data/lunar/training/catalogs/'
cat_file = cat_directory + 'apollo12_catalog_GradeA_final.csv'
cat = pd.read_csv(cat_file)

def get_all_mseed_files(dir=""):
    return [join(dir, file) for file in os.listdir(dir) if file.endswith("mseed")]

def filter(raw_trace):
    trace = raw_trace.copy()
    sampling_rate = trace.stats["sampling_rate"]

    trace.filter('lowpass', freq=0.4)
    trace.filter('bandpass', freqmin=0.7, freqmax=1.5)

    sta = 120 
    lta = 1000
    cft = classic_sta_lta(trace, int(sta * sampling_rate), int(lta * sampling_rate))

    thr_on = 4
    thr_off = 1.5
    on_off = np.array(trigger_onset(cft, thr_on, thr_off))
    
    window_offset = 20

    while len(on_off) < 1:
        cft = classic_sta_lta(trace, int(sta + window_offset * sampling_rate), int(lta * sampling_rate))
        on_off = np.array(trigger_onset(cft, thr_on, thr_off))
        window_offset += 20

    greatest_trigger = 0
    corresponding_x = -1

    for i in on_off:
        if i[0] < len(trace.data):
            abs_data = np.abs(trace.data[i[0]])
            if greatest_trigger < abs_data:
                greatest_trigger = abs_data
                corresponding_x = i[0]

            

    return raw_trace, corresponding_x

def main_compiler():
    #streams = get_all_mseed_files(dir="./data/lunar/training/data/S12_GradeA")
    streams = get_all_mseed_files(dir="./data/mars/training/data")


    for file in streams:
        data_stream = read(file)
        traces = data_stream.traces

        filtered_trace, arrival = filter(traces[0])
        tr_times = filtered_trace.times()
        tr_data = filtered_trace.data
        fig , ax = plt.subplots(1,1,figsize=(10,3))
        ax.axvline(x = tr_times[arrival], color='red', label='Trig. On')
      
        ax.plot(tr_times,tr_data)
        ax.legend(loc='upper left')
        ax.set_xlim([min(tr_times),max(tr_times)])
        ax.set_ylabel('Velocity (m/s)')
        ax.set_xlabel('Time (s)')
        ax.set_title(f'{file}', fontweight='bold') #Test_Filename isn't defined
    
        fig.savefig(f"./imgs/mars/{file.split("\\").pop().replace(".mseed", ".png")}")
    plt.close()

       
    
main_compiler()

