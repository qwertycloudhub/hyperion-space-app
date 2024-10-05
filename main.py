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
st = []
for file in mseed_files:
    st.append(ob.read(file))

#Stats

print(st[75][0].stats)
tr=st[0].traces[0].copy()
tr_filt = tr.copy()
tr_filt.filter('lowpass', freq=1.0, corners=2, zerophase=True)
t = np.arange(0, tr.stats.npts / tr.stats.sampling_rate, tr.stats.delta)







#Arrival Time
cat_directory = './data/lunar/training/catalogs/'
cat_file = cat_directory + 'apollo12_catalog_GradeA_final.csv'
cat = pd.read_csv(cat_file)
print(cat.to_string())  



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
    print(data_cat)
    print(arrival_time_rel)
    print(arrival_time_absolute)

for file in st:
    print(st)
        
