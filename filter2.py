from obspy.signal.invsim import cosine_taper
from obspy.signal.filter import highpass
from obspy.signal.trigger import classic_sta_lta, plot_trigger, trigger_onset
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
def filter2(trace):
    df = trace.stats.sampling_rate
    sta = 120 
    lta = 600
    cft = classic_sta_lta(trace, int(sta * df), int(lta * df))
    thr_on = 4
    thr_off = 1.5
    on_off = np.array(trigger_onset(cft, thr_on, thr_off))