import numpy as np
import pandas as pd
#import matplotlib as plt
import matplotlib.pyplot as plt
from scipy import signal
from matplotlib import cm

import obspy as ob

from datetime import datetime, timedelta
#import sklearn  as sk

#It doesn't have all the data in it
cat_directory = './data/lunar/training/catalogs/'
cat_file = cat_directory + 'apollo12_catalog_GradeA_final.csv'
cat = pd.read_csv(cat_file)
print(cat.to_string())

#Relative Arrival Time
# row = cat.iloc[6]
# arrival_time_rel = row['time_rel(sec)']
# arrival_time_rel

#For Loop that iterates through all files

for i in range(0, len(cat.index)):
    row = cat.iloc[i]
    arrival_time_rel = row['time_rel(sec)']#important
    test_filename = row.filename
    data_directory = './data/lunar/training/data/S12_GradeA/'
    csv_file = f'{data_directory}{test_filename}.csv'
    data_cat = pd.read_csv(csv_file)


# # Read in time steps and velocities
# csv_times = np.array(data_cat['time_rel(sec)'].tolist())
# csv_data = np.array(data_cat['velocity(m/s)'].tolist())
# # Plot the trace!
# fig,ax = plt.subplots(1,1,figsize=(10,3))
# ax.plot(csv_times,csv_data)
# # Make the plot pretty
# ax.set_xlim([min(csv_times),max(csv_times)])
# ax.set_ylabel('Velocity (m/s)')
# ax.set_xlabel('Time (s)')
# ax.set_title(f'{test_filename}', fontweight='bold')
# # Plot where the arrival time is
# arrival_line = ax.axvline(x=arrival_time_rel, c='red', label='Rel. Arrival')
# ax.legend(handles=[arrival_line])

fig = plt.figure(figsize=(10, 10))
ax = plt.subplot(2, 1, 1)
# Plot trace
ax.plot(tr_times_filt,tr_data_filt)
# Mark detection
ax.axvline(x = arrival_time_rel, color='red',label='Detection')
ax.legend(loc='upper left')
# Make the plot pretty
ax.set_xlim([min(tr_times_filt),max(tr_times_filt)])
ax.set_ylabel('Velocity (m/s)')
ax.set_xlabel('Time (s)')
ax2 = plt.subplot(2, 1, 2)
vals = ax2.pcolormesh(t, f, sxx, cmap=cm.jet, vmax=5e-17)
ax2.set_xlim([min(tr_times_filt),max(tr_times_filt)])
ax2.set_xlabel(f'Time (Day Hour:Minute)', fontweight='bold')
ax2.set_ylabel('Frequency (Hz)', fontweight='bold')
ax2.axvline(x=arrival_time_rel, c='red')
cbar = plt.colorbar(vals, orientation='horizontal')
cbar.set_label('Power ((m/s)^2/sqrt(Hz))', fontweight='bold')
    

plt.show()