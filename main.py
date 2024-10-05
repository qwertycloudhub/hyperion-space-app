#IMPORTS
import numpy as np
import pandas as pd
#import matplotlib as plt
import matplotlib.pyplot as plt
from scipy import signal
from matplotlib import cm
import obspy as ob
import os
from datetime import datetime, timedelta
from os.path import join
data_directory = './data/lunar/training/data/S12_GradeA/'



def get_all_files(training_dir=""):
    files = os.listdir(training_dir)
    return [join(training_dir, file) for file in files if file.endswith("mseed")]
mseed_files = get_all_files(training_dir=data_directory)
#print(mseed_files)
streams = []
for file in mseed_files:
    streams.append(ob.read(file))

#Stats

#print(st[75][0].stats)



# tr=st[0].traces[0].copy()
# tr_filt = tr.copy()
# tr_filt.filter('lowpass', freq=1.0, corners=2, zerophase=True)
# t = np.arange(0, tr.stats.npts / tr.stats.sampling_rate, tr.stats.delta)
# tr_times = tr.times()
# tr_data = tr.data
# starttime = tr.stats.starttime.datetime
# arrival = (arrival_time - starttime).total_seconds() #Define Arrival_Time





#Arrival Time
cat_directory = './data/lunar/training/catalogs/'
cat_file = cat_directory + 'apollo12_catalog_GradeA_final.csv'
cat = pd.read_csv(cat_file)
#print(cat.to_string())  



#For Loop to open files
#Empty Dictionary for Data

all_data = {}

for i in range(0, len(cat.index)):
    row = cat.iloc[i]
    test_filename = row.filename
    data_directory = './data/lunar/training/data/S12_GradeA/'
    csv_file = f'{data_directory}{test_filename}.csv'
    data_cat = pd.read_csv(csv_file)
    arrival_time_rel = row['time_rel(sec)']#important
    arrival_time_absolute = datetime.strptime(row['time_abs(%Y-%m-%dT%H:%M:%S.%f)'], '%Y-%m-%dT%H:%M:%S.%f') #Not Working
    #print(data_cat)
    #print(arrival_time_rel)
    #print(arrival_time_absolute)


    stats = streams[i][0].stats
    sampling_rate = stats["sampling_rate"]
    tr=streams[i].traces[0].copy()
    tr_filt = tr.copy()

    print(f"Sampling rate {sampling_rate}")
    tr_filt.filter('bandpass', freqmin = .9, freqmax = 1, corners=1, zerophase=False)
    tr_filt.filter('lowpass', freq=0.1, corners=0, zerophase=False)
    #tr_filt.filter('highpass', freq=0.1, corners=2, zerophase=False)
    #tr_filt.filter('bandstop', freqmin = 0.1, freqmax = 0.2, corners=2, zerophase=False)


    t = np.arange(0, tr.stats.npts / tr.stats.sampling_rate, tr.stats.delta)

    tr_times = tr_filt.times()
    tr_data = tr_filt.data

    starttime = tr.stats.starttime.datetime
    arrival = arrival_time_rel

        # Initialize figure
    fig,ax = plt.subplots(1,1,figsize=(10,3))
        # Plot trace
    ax.plot(tr_times,tr_data)
        # Mark detection
    ax.axvline(x = arrival, color='red',label='Rel. Arrival')
    ax.legend(loc='upper left')
        # Make the plot pretty
    ax.set_xlim([min(tr_times),max(tr_times)])
    ax.set_ylabel('Velocity (m/s)')
    ax.set_xlabel('Time (s)')
    ax.set_title(f'{test_filename}', fontweight='bold') #Test_Filename isn't defined

    plt.show()