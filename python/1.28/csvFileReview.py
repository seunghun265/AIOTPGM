import csv

f = open("weather.csv","r",encoding="utf-8")
data = csv.reader(f)
header = next(data)
temp = 1000.0
for row in data:
    if temp > float(row[3]):
        temp = float(row[3])
print(f"가장 추웠던 날은{temp}도 입니다")
f.close()
