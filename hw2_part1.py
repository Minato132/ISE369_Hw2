import pandas as pd
import geopandas as gp
import matplotlib.pyplot as plt

map = gp.read_file('md_cong_adopted_2022.zip')

with open('weball22.txt') as file:
    data = pd.read_csv(file, sep = '|', header = None)

data = data.loc[data[18] == 'MD']
data = data.loc[data[19] > 0 ]
data = data.loc[:, [11, 17, 19, 25, 26]]
data = data.groupby(by = 19, as_index = False).sum()
data_sum = data.sum(axis = 1)
median = data_sum.median()

for i in range(len(data_sum)):
    data_sum[i] = (data_sum[i] - median)/ median

map['diff'] = data_sum

map.plot(column = 'diff', cmap = 'Greens', legend = True, 
         legend_kwds = {'label' : 'Contributions by District \n Normalized to median',
                        'orientation': 'horizontal'})
plt.title('Contributions by each MD Districts')
plt.show()
print(data_sum)
