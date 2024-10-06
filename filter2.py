from obspy.signal.trigger import classic_sta_lta, trigger_onset
from os.path import join
import os
import numpy as np
import pandas as pd
#import matplotlib as plt
import matplotlib.pyplot as plt
from matplotlib import cm
from datetime import datetime, timedelta
def filter2(trace):
    df = trace.stats.sampling_rate
    sta = 120 
    lta = 600
    cft = classic_sta_lta(trace, int(sta * df), int(lta * df))
    thr_on = 4
    thr_off = 1.5
    on_off = np.array(trigger_onset(cft, thr_on, thr_off))