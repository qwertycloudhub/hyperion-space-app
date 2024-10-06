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
from obspy.signal.trigger import classic_sta_lta, trigger_onset
#hello
data_directory = './data/lunar/training/data/S12_GradeA/'
cat_directory = './data/lunar/training/catalogs/'
cat_file = cat_directory + 'apollo12_catalog_GradeA_final.csv'
cat = pd.read_csv(cat_file)

# for i in range(0, len(cat.index)):
#     row = cat.iloc[i]
#     test_filename = row.filename
#     data_directory = './data/lunar/training/data/S12_GradeA/'
#     csv_file = f'{data_directory}{test_filename}.csv'
#     data_cat = pd.read_csv(csv_file)
def get_all_mseed_files(dir=""):
    return [join(dir, file) for file in os.listdir(dir) if file.endswith("mseed")]


def filter1(trace):
    tr_filt = trace.copy()
    tr_filt.filter('bandpass', freqmin = .9, freqmax = 1, corners=1, zerophase=False)
    tr_filt.filter('lowpass', freq=0.1, corners=0, zerophase=False)
    return tr_filt

def filter2(trace):
    df = trace.stats.sampling_rate
    sta = 120 
    lta = 600
    cft = classic_sta_lta(trace, int(sta * df), int(lta * df))
    thr_on = 4
    thr_off = 1.5
    on_off = np.array(trigger_onset(cft, thr_on, thr_off))
    return on_off

def main_compiler():
    print("main")
    streams = get_all_mseed_files(dir="./data/lunar/training/data/S12_GradeA")
    data_list = []

    for file in streams:
        data_stream = read(file)
        traces = data_stream.traces
        stats = data_stream[0].stats
        channel = stats.channel

        filtered_trace = filter1(traces[0])
        tr_times = filtered_trace.times()
        tr_data = filtered_trace.data
        values = filter2(filtered_trace)
        fig , ax = plt.subplots(1,1,figsize=(10,3))

        for i in np.arange(0,len(values)):
            triggers = values[i]
            ax.axvline(x = tr_times[triggers[0]], color='red', label='Trig. On')
            ax.axvline(x = tr_times[triggers[1]], color='purple', label='Trig. Off')

        data_list.append(
            {
                "channel": channel,
                "Trace": filtered_trace,
            }
        )


        # Initialize figure
            # Plot trace
        ax.plot(tr_times,tr_data)
            # Mark detection
        ax.legend(loc='upper left')
            # Make the plot pretty
        ax.set_xlim([min(tr_times),max(tr_times)])
        ax.set_ylabel('Velocity (m/s)')
        ax.set_xlabel('Time (s)')
        ax.set_title(f'{file}', fontweight='bold') #Test_Filename isn't defined

        fig.savefig(f"./imgs/{file.split("\\").pop().replace(".mseed", ".png")}")
        plt.close()
       
    
main_compiler()

