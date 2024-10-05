import numpy as np
import pandas as pd
import obspy
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import os
from os.path import join, isfile
from datetime import datetime, timedelta
#import sklearn  as sk

#It doesn't have all the data in it
cat_directory = './data/lunar/training/catalogs/'
cat_file = cat_directory + 'apollo12_catalog_GradeA_final.csv'
cat = pd.read_csv(cat_file)
print(cat.to_string())

data_directory = './data/lunar/training/data/S12_GradeA/'

def get_all_files(training_dir=""):
    files = os.listdir(training_dir)
    return [join(training_dir, file) for file in files if file.endswith("mseed")]
mseed_files = get_all_files(training_dir=data_directory)
#print(mseed_files)
st = []
count = 0
for file in mseed_files:
    count+=1
    st.append(obspy.read(file))

#print(st[1][0].stats)
tr = st[0].traces.copy()
print(tr)
tr_times = tr.times()
tr_data = tr.data
starttime = tr.stats.starttime.datetime
arrival_time = st[1][0].stats.starttime - st[1][0].stats.endtime

print(tr_times)

arrival = (arrival_time - starttime).total_seconds()

