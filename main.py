# Zestaw B
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import openpyxl
import xlrd
import seaborn as sns

df = pd.read_csv('cars.csv', header=0, sep=';')
print(df)
print(df[df['Horsepower'] < 105])
x = df.groupby(['Model year']).agg({'Model year':['count']})
print(x)
wykres = x.plot.pie(subplots=True, autopct='%.2f %%', fontsize=15, figsize=(8, 8), legend=False)
plt.title('Roczniki aut')
plt.savefig('roczniki_kolowy.png')
plt.show()



