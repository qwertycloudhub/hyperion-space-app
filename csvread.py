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
#print(cat.to_string())

#Relative Arrival Time
row = cat.iloc[6]
arrival_time = datetime.strptime(row['time_abs(%Y-%m-%dT%H:%M:%S.↪%f)'],'%Y-%m-%dT%H:%M:%S.%f')
arrival_time_rel = row['time_rel(sec)']


#For Loop that iterates through all files

for i in range(0, len(cat.index)):
    row = cat.iloc[i]
    arrival_time_rel = row['time_rel(sec)']#important
    test_filename = row.filename
    data_directory = './data/lunar/training/data/S12_GradeA/'
    csv_file = f'{data_directory}{test_filename}.csv'
    data_cat = pd.read_csv(csv_file)

    print(arrival_time)




