# (함수유형2) 누적합 계산 

def print_total(start, end):
    total = 0
    for num in range(start, end+1):
        total += num
    print(f"누적합: {total}")

print_total(1, 100)	# 입력값에 따라 다른 결과
print_total(1, 500)	# 입력값에 따라 다른 결과