from matplotlib.font_manager import FontProperties
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from matplotlib.ticker import MultipleLocator, ScalarFormatter

import numpy as np
from IPython import display
import matplotlib.gridspec as gridspec
import sys

import math as math
import datetime
from datetime import timedelta, date

#import datetime as dt
import os
import glob
import matplotlib.dates as mdates
print (sys.path)
import pandas as pd
#import seaborn as sns
import matplotlib.dates as dates
from matplotlib.dates import MonthLocator, WeekdayLocator, DateFormatter, YearLocator
#from model_utils import *
import datetime as dt

def read_met_huancayo(filename):
    print(">>Reading data from;", filename)
    df = pd.read_csv(filename,delimiter=",",
                     parse_dates=[0], #usecols=['Date','Time', 'Bar'],
                     dayfirst=True
                     )
    #df.index
    return df

def read_met_piura(filename):
    print(">>Reading data from;", filename)
    df = pd.read_csv(filename,delimiter=",",
                  parse_dates=[0],
                  dayfirst=True,
                  skiprows=1)
    df["Bar"]= df["Bar  "]
    df.Date = pd.to_datetime(df["Date"], "%Y-%m-%d").dt.strftime("%Y-%m-%d")
    df["timestamps"] = pd.to_datetime(df["Date"] + ' ' + df["Time"]) + pd.Timedelta(hours=5)
    df.set_index('timestamps',inplace=True)
    df['Bar'] = df['Bar'].astype(float)
    return df

def read_met_jro(filename):
    print(">>Reading data from;", filename)
    df = pd.read_csv(filename,delimiter=",",usecols=['Date','Time', 'Bar'],parse_dates=[0],dayfirst=True)
    df.Date= pd.to_datetime(df["Date"], "%Y-%m-%d").dt.strftime("%Y-%m-%d")
    df["timestamps"] = pd.to_datetime(df["Date"] + ' ' + df["Time"]) + pd.Timedelta(hours=5)
    df.set_index('timestamps',inplace=True)
    df['Bar'] = df['Bar'].astype(float)
    return df
