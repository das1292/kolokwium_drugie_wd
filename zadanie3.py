# Zestaw B
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import openpyxl
import xlrd
import seaborn as sns

df = pd.read_csv('cars.csv', header=0, sep=';')
print(df)
y = df[(df['Model year'] > 71) & (df['Model year'] < 78)].groupby(['Model year']).agg({'Model year': ['count']})
wykres = y.plot.bar()
plt.xticks(rotation=0)
plt.ylabel("Ilość aut")
plt.xlabel("Roczniki aut")
plt.title('Roczniki aut')
plt.show()