# ❶ 3의 배수 건너뛰고 출력 (for문)

for i in range(11):		# 0∼100 순차반복
    if i % 3 == 0:		# 3의 배수인 경우
        continue		# 다음 루프로 이동
    print(i, end=" ")