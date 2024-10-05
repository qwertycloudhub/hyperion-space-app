import numpy as np
import pandas as pd
#import matplotlib as plt
import matplotlib.pyplot as plt
from scipy import signal
from matplotlib import cm
import obspy as ob

from datetime import datetime, timedelta
data_directory = './data/lunar/training/data/S12_GradeA/'
mseed_file = f'{data_directory}{test_filename}.mseed'
st = read(mseed_file)
st
st[0].stats
tr = st.traces[0].copy()
5
tr_times = tr.times()
tr_data = tr.data
# Start time of trace (another way to get the relative arrival time using␣
starttime = tr.stats.starttime.datetime
arrival = (arrival_time - starttime).total_seconds()
arrival
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
ax.set_title(f'{test_filename}', fontweight='bold')