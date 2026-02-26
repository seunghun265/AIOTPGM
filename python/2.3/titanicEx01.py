import pandas as pd

titanic = pd.read_csv("titanic.csv")
# print(titanic)
# print(titanic["Age"])         #field 뽑아서 보기  ["field"]
# print(titanic[["Name","Age","Sex"]])
# below20 = titanic[titanic["Age"] < 20]
# print(below20)
pClass12 = titanic[titanic["Pclass"].isin([1, 2])]
print(pClass12)

# print(titanic["Age"].max())
# print(titanic["Age"].mean())
# print(titanic["Age"].min())

# print("위5줄\n",titanic.head())
# print("아래 5줄\n",titanic.tail())
# print("컬럼,타입,결측치\n",titanic.info())
# print("통계요약\n",titanic.describe())
# print("행,열\n",titanic.shape)
# print("컬럼이름\n",titanic.columns)
# print("데이터타입\n",titanic.dtypes)
