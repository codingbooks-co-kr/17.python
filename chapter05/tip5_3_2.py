# (함수유형1) 누적합 계산 

def print_total():
    total = 0
    for num in range(1, 101):
        total += num
    print(f"누적합: {total}")

print_total()	# 항상 동일한 결과
print_total()	# 항상 동일한 결과