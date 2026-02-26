itemPrice = int(input("물건값을 입력하시오: "))
won10000 = int(input("10000원 지폐개수 :"))
won1000 = int(input("1000원 지폐개수 : "))
won500 = int(input("500원 동전개수 : "))
won100 = int(input("100원 동전개수 : "))
change = won10000*10000 + won1000*1000 + won500*500 + won100*100 - itemPrice
# 거스름돈(1000원 개수)을 계산한다.
mWon1000 = change//1000
change = change%1000
# 거스름돈(500원 동전 개수)을 계산한다.
mWon500 = change//500
change = change%500
# 거스름돈(100원 동전 개수)을 계산한다.
mWon100 = change//100
change = change%100
# 거스름돈(10원 동전 개수)을 계산한다.
mWon10 = change//10
change = change%10
# 거스름돈(1원 동전 개수)을 계산한다.
mWon1 = change
print("1000원=", mWon1000, "500원=", mWon500, "100원=", mWon100, "10원=", mWon10, "1원=", mWon1)