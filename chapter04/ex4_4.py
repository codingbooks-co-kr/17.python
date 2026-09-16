# 점수를 5개 입력 후 합계 및 평균 계산

total = 0		# 합계를 저장할 변수 초기화
num = 5		# 전체 반복 횟수 설정
for i in range(num):
    score = int(input("점수: "))		# 점수 입력
    total += score			# 입력 점수 누적

average = total / num		# 평균 계산
print(f"합계: {total}, 평균: {average:.1f}")