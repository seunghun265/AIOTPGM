import pandas as pd

dataS = ['Kim', 'Park', 'Lee', 'Choi']

ser= pd.Series(dataS)
print(ser)


dataDF = {'Name':['Kim', 'Park', 'Lee', 'Choi'],
 'Age':[20, 23, 21, 26]}
df= pd.DataFrame(dataDF, index=["학번1", "학번2", "학번3", "학번4"])
print(df)

df.to_excel('titanic.xlsx', sheet_name='passengers', index=False)  #index가 ture이며 0 1 2 3 이 붙음
