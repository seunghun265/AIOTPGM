import matplotlib.pyplot as plt
from sklearn import linear_model
 # 선형회귀모델을생성한다. 
reg= linear_model.LinearRegression()
 # 데이터는파이썬의리스트로만들어도되고아니면넘파이의배열로만들어도됨
X = [[174], [152], [138], [128], [186]] # 학습예제
y = [71, 55, 46, 38, 88] # 정답
reg.fit(X, y)
print(reg.coef_)
print(reg.intercept_)
print(reg.score)
reg.predict([[178]])

# 학습 데이터를산포도로그린다. 
plt.scatter(X, y, color='black')
# 학습 데이터를입력으로하여예측값을계산한다. 직선을가지고예측하기때문에
#직선상의점이된다. 
y_pred = reg.predict(X)
# 예측값으로선그래프를그린다. 
# 직선이 그려진다. 
plt.plot(X, y_pred, color='blue', linewidth=3)
plt.show()

