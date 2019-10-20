# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 13:15:20 2019

@author: DSU
"""

from stopwatch import stopwatch
from scipy.optimize import curve_fit, minimize
from tqdm import trange
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import fibonacci

# helper setting variables
TRIALS = 100
TIMEOUT = 1e8

# timer function (nanoseconds) and dictionary of times
clock = stopwatch()
records = dict()

# time each algorithm until it takes too long (or it hits 1000)
for algo in fibonacci.algorithms:
    times = list()
    
    # run algorithm for each number until timeout
    # run each algorithm trials times for each number
    for i in trange(1000, desc=algo.__name__):
        clock.start()
        for _ in range(TRIALS):
            algo(i)
        times.append(clock.time() / TRIALS)
        if times[-1] > TIMEOUT: break
    
    # add average time to records
    records[algo.__name__] = times

# create dataframe from times
df = pd.DataFrame.from_dict(records, orient='index').transpose()

# create list of names of algorithms
algorithms = [algo.__name__ for algo in algorithms]

# plot each algorithm
for algo in algorithms:
    df[[algo]].dropna().plot()
    plt.show()

# equations for each big o time
def lin_fit(x, a, b):
    return a*x+b

def exp_fit(x, a, b, c):
    phi = (1 + 5 ** 0.5) / 2
    return a*phi**x + b*x + c

def log_fit(x, a, b):
    return a * np.log2(x) + b

# type each algorithm to a predict function
lins = ['FibLoop', 'FibRecurDP', 'FibFormula']
exps = ['FibRecur', 'FibCassini']
logs = ['FibMatrix']

for algo in algorithms:
    # choose fit algorithm
    if algo in lins: fit=lin_fit
    elif algo in exps: fit=exp_fit
    elif algo in logs: fit=log_fit
    
    # curve fit
    series = df[algo].dropna().iloc[1:]
    var, _ = curve_fit(fit, series.index, series)

    # predict points
    y = [fit(x, *var) for x in series.index]
    
    # add to dataframe
    df[(algo, 'predict')] = pd.Series(y, index=series.index)

# plot each algorithm
for algo in algorithms:
    df[[algo, (algo, 'predict')]].dropna().plot()
    plt.show()