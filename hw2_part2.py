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

def colors(arg):
    if arg < 0:
        if arg > -.05:
            x = [1,0,0,.2]
        elif -.1 > arg > -.05:
            x = [1,0,0,.5]
        else:
            x = [1,0,0,1]
        
    else:
        if arg < .05:
            x = [0,0,1,.2]
        elif .05 < arg < .1:
            x = [0,0,1,.5]
        else:
            x = [0,0,1,1]
    
    return x
    
def dis(arg):
    x = []
    for i in range(len(arg)):
        y = arg.loc[i:i, :]
        x.append(y)
    return x

def distr(arg1, arg2):
    base = arg1.plot(color = 'white', edgecolor = 'black')
    for i in range(len(arg1)):
        base = dis(arg1)[i].plot(ax = base, edgecolor = 'black', color = colors(arg2[i]))
    
    plt.title('Marginal Victory between Democrats & Republicans')
    plt.show()

print(diff)
print(distr(map, diff))
