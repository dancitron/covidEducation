import pandas as pd
import numpy
import matplotlib.pyplot as plt
from scipy.stats import linregress
from scipy.stats import pearsonr




df = pd.read_csv('../extracts/mergedExtract.csv')

x = df['percentCases']
y = df['bachAndAbove']

corr, _ = pearsonr(x, y)
print('Pearsons correlation: %.3f' % corr)
corrB = linregress(x, y)
print(corrB)
plt.scatter(x, y)
plt.show()
