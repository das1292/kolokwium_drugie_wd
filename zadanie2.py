# Zestaw B
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xlrd
import openpyxl
from math import *
import seaborn as sns

x = np.arange(-100, 100, 0.1)
plt.subplot(3,1,1)
plt.plot(x, (-4)*x**2+(6*x/2)+20, 'ro', label='(-4)*x**2+(6*x/2)+20')
plt.axis([-2, 4, -25, 25])
plt.legend(loc='lower center')
plt.title('Pierwszy')

plt.subplot(3,1,2)
plt.plot(x, np.tan(x)-5, label='f(x) = 1/x')
plt.axis([-2, 6, -40, 80])
plt.legend(loc='lower left')
plt.title('Drugi')

x = np.arange(-100, 100, 0.1)
plt.subplot(3,1,3)
plt.plot(x, (-4)*x**2+(6*x/2)+20, 'ro', label='(-4)*x**2+(6*x/2)+20')
plt.plot(x, np.tan(x)-5, label='f(x) = 1/x')
plt.axis([-2, 6, -100, 100])
plt.title('Trzeci')
plt.legend(loc='upper left')
plt.show()