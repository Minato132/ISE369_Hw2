import pandas as pd
import geopandas as gp
import matplotlib.pyplot as plt

map = gp.read_file('md_cong_adopted_2022.zip')

with open('md_2022_primary_cand_data.csv') as file:
    data = pd.read_csv(file)

data = data.loc[:, ['Party', 'District', 'Primary %']]
x = []
for i in data['Primary %']:
    i = i.replace('%', '')
    x.append(float(i)/ 100)

data['Primary Dec'] = x
data.dropna(inplace = True)

# The Dems

dems = data.loc[data['Party'] == 'DEM']
dems = dems.groupby(by = 'District', as_index = False).max()


# The Rep

reps = data.loc[data['Party'] == 'REP']
reps = reps.groupby(by = 'District', as_index = False).max()

diff = dems['Primary Dec'] - reps['Primary Dec']

map.plot(column = diff, cmap = 'Greens')
plt.show()
print(diff)
