# ❷ 3의 배수 건너뛰고 출력 (while문)

i = 0			# 변수 초기화
while True:		# 무한 반복
    i += 1		# 변수 증가
    if i >= 11:		# 11 이상인 경우
        break		# 즉시 루프 탈출
    if i % 3 == 0:		# 3의 배수인 경우
        continue		# 다음 루프로 이동
    print(i, end=" ")