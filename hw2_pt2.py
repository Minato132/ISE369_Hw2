#Steven Chen (112927567)

import pandas as pd
import geopandas as gp
import matplotlib.pyplot as plt

map = gp.read_file('md_cong_adopted_2022.zip')

dem = pd.Series([43.2, 59.3, 60.2, 90.3, 66.0, 54.8, 82.2, 80.3,])
rep = pd.Series([54.5, 40.7, 39.8, 9.7, 34.0, 45.2, 17.8, 18.2 ])
d = {'dem':dem, "rep":rep}
data = pd.DataFrame(d)
diff = data['dem'] - data['rep']
print(diff)

def colors(arg):
    if arg < 0:
        if arg > -5:
            x = [1,0,0,.2]
        elif -10 > arg > -5:
            x = [1,0,0,.5]
        else:
            x = [1,0,0,1]
        
    else:
        if arg < 5:
            x = [0,0,1,.2]
        elif 5 < arg < 10:
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
    
    plt.title('Marginal Victory between Democrats and Republicans \nIn Maryland')
    plt.show()


print(distr(map, diff))
