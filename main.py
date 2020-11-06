# Challenge 1 (Statistics)

import numpy as np
from scipy import stats


numbers = np.arange(0, 20)

mean = np.mean(numbers)
standard_dev = np.std(numbers)
variance = np.var(numbers)

print("The mean is ", mean)
print("The standard deviation ", standard_dev)
print("The variance is ", variance)

