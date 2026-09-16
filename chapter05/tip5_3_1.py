# (함수 미사용) 누적합 계산

total = 0			# 변수 초기화
for num in range(1, 101):	# 1∼100 순회
    total += num		# 누적합 계산
print(f"누적합: {total}")