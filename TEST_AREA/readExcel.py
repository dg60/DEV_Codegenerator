import pandas as pd
from pandas import Series,DataFrame



struct = pd.read_excel('/home/dgrill/Schreibtisch/Projects/00_CodeGenerator/data/structure.xlsx')
lines = struct.shape[0]
column = struct.shape[1]
items = list(struct.items())
keys = struct.keys()
values = struct.values
MSS = struct['MSS']

print(struct)
print('Items: ',items)
print('Lines: ',lines)
print('Colums: ', column)
print('Daten column MSS:', MSS)

'''
for key in keys:
    print('Keys: ', key)

for val in values:
    print('Values: ',values)
    
for val in MSS:
    print('Values: ',val)

'''
lstVal = []
for val in values:

    lstVal.append(val)
    print('Values: ',val)

print(lstVal)
