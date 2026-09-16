# ❶ 1부터 임의의 정수(입력값)까지의 누적합 계산
# 딱 한 번 계산하고 끝내는 방식

num = 0		# 갱신할 변수 초기화
total = 0		# 갱신할 변수 초기화

# 1. 사용자 입력 유효성 검사
while True:	# 무한 반복
    num = int(input("정수: "))
    if num <= 0:	# 입력값이 0 이하인 경우
        print("양수를 입력하세요!")
        continue	# 아래코드 건너뛰기
    break		# 양수이면 무한 루프 탈출

# 2. 입력한 정수까지의 누적합 계산 및 출력
for i in range(1, num + 1):
    total += i
print(f"1에서 {num}까지의 합: {total}")