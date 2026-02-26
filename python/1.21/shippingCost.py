price = int(input("정가 입력하세요 :"))

if price > 40000:
    shippingCost = 0
else:
    shippingCost = 5000
    
print(f"배송비 = {shippingCost} 입니다.")

# price = int(input("정가 입력하세요 :"))
# shippingCost = 5000
# if price > 40000:
#     shippingCost = 0
    
# print(f"배송비 = {shippingCost} 입니다.")