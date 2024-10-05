from os.path import join
import os
from obspy import read
import numpy as np
import pandas as pd
#import matplotlib as plt
import matplotlib.pyplot as plt
from scipy import signal
from matplotlib import cm
from datetime import datetime, timedelta
from os.path import join

data_directory = './data/lunar/training/data/S12_GradeA/'
cat_directory = './data/lunar/training/catalogs/'
cat_file = cat_directory + 'apollo12_catalog_GradeA_final.csv'
cat = pd.read_csv(cat_file)
print(cat.to_string())
for i in range(0, len(cat.index)):
    row = cat.iloc[i]
    test_filename = row.filename
    data_directory = './data/lunar/training/data/S12_GradeA/'
    csv_file = f'{data_directory}{test_filename}.csv'
    data_cat = pd.read_csv(csv_file)
def get_all_mseed_files(dir=""):
    return [join(dir, file) for file in os.listdir(dir) if file.endswith("mseed")]

def filter(trace):
    return trace

def main_compiler():
    all_mseed_files = get_all_mseed_files(dir="./data/mars/training/data")
    data_list = []

    for file in all_mseed_files:
        data_stream = read(file)
        traces = data_stream.traces
        stats = data_stream[0].stats
        channel = stats.channel

        data_list.append(
            {
                "channel": channel,
                "Trace": traces[0],
            }
        )
    for i in range(0,len(cat.index)):
        row = cat.iloc[i]
        test_filename = row.filename
        arrival_time_rel = row['time_rel(sec)']

        data_list.append(
            {
                "destination_relative": arrival_time_rel
                "Filtered_trace": 
            }
        )
main_compiler()