from random import sample
import numpy as np
from scipy import stats as sp

sample_data = [103,151,176,188,146,184,175,112,115,163]

mean = np.mean(sample_data)
median = np.median(sample_data)
mode = sp.mode(sample_data)
var = round(np.var(sample_data,ddof=1),2)
sdev = round(np.std(sample_data,ddof=1),2)
Range = np.ptp(sample_data)

print("Mean:",mean)
print("Median:",median)
print("Mode:",mode)
print("Var:",var)
print("sdev:",sdev)
print("range:",Range)

