fruits = {"apple": 1000, "kiwi": 2500, "cherry": 5000}

# ❾ 값 확인: 3000원 이하인 과일의 개수 출력
count = 0				# 누적할 변수 초기화
for fruit in fruits.values(): 		# 딕셔너리의 모든 값 순회
    if fruit <= 3000:		# 값이 3000원 이하라면
        count += 1			# count 누적
print(f"3000원 이하 과일: {count}개")