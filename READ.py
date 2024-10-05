import numpy as np
import pandas as pd
from obspy import read
from datetime import datetime
import matplotlib.pyplot as plt
import os


cat_directory = './data/lunar/training/catalogs/'
cat_file = cat_directory + 'apollo12_catalog_GradeA_final.csv'
cat = pd.read_csv(cat_file)

row = cat.iloc[6]
arrival_time = datetime.strptime(row['time_abs(%Y-%m-%dT%H:%M:%S.↪%f)'],'%Y-%m-%dT%H:%M:%S.%f')
print(arrival_time)