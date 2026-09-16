# ❷ 1부터 임의의 정수(입력값)까지의 누적합 계산
# 원할 때까지 반복 계산하는 방식

while True:	# 무한 반복
    user_input = input("정수: ")
    if user_input == 'q':	# 'q'를 입력한 경우
        break		# 무한 루프 탈출
    num = int(user_input)	# 문자→정수 변환
    if num <= 0:
        print("양수를 입력하세요!")
        continue		# 아래코드 건너뛰기
    total = 0		# 누적 변수 초기화
    for i in range(1, num + 1):
        total += i
    print(f"1에서 {num}까지의 합: {total}")

print("누적합 계산 종료!")