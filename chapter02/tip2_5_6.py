# 몫과 나머지 계산 응용-2
# 물품 구매 개수 및 잔돈 계산

money = 10000		# 가진 돈
price = 1500		# 구매 물품

num = money // price 
print("구매개수:", num)

change = money % price
print("잔액(원):", change)