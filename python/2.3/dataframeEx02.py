import pandas as pd
countries = pd.read_csv("countries.csv")
print(countries)

df = pd.DataFrame({"code":["CA"], "country":["Canada"],"area":[9984670],  "capital":["Ottawa"],"population":[34300000]}) 
df2 = pd.concat([countries, df], ignore_index=True)

print(df)
print(df2)

df2["density"] = df2["population"] / df2["area"]

print(df2)

